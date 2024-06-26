from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from api_v1.user.shemas import UserCreate

async def get_one(db: AsyncSession, name: str) -> User | None:
    return await db.get(User, name)


async def get_all(db: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.name)
    result: Result = await db.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def create(db: AsyncSession, creature_in: UserCreate ) -> User: 
    user_model = User(**creature_in.model_dump())
    db.add(user_model)
    try:
        db.commit()
    except Exception as e:
        raise e

    # await db.refresh(creature_model) # if in psql data maybe rework
    return user_model

  