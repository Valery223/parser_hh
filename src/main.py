from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from api_v1 import router as router_v1
from core.config import settings
from errors.validation import ValidationError


app = FastAPI()

app.include_router(router_v1, prefix=settings.api_v1_prefix)



origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def top():
    return "This is top"

@app.get("/test/{text}")
def test(text: str):
    items = []
    items.append({'item':{"id":1, 'name': text,"value":33}})
    items.append({'item':{"id":1, 'name': text,"value":33}})
    return items

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail1": exc.detail}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)