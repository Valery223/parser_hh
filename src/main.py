from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def top():
    return "This is top"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)