from sqlalchemy.ext.asyncio import (create_async_engine, 
                                    async_sessionmaker,
                                    async_scoped_session,
                                    AsyncSession,
                                    )
from sqlalchemy.orm import sessionmaker
from asyncio import current_task
from typing import AsyncGenerator

from  core.config import settings

class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
    
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        # you can change it to get_scroped_session, but it not support "with"
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DatabaseHelper(settings.get_url(), echo=settings.db_echo)

