from uuid import UUID
import asyncio

import pytest
from naks_library.commiter import SqlAlchemyCommitter

from app.application.dto import CreateAcstFilesDTO, CreatePersonalNaksCertificationFilesDTO, CreatePersonalNaksProtocolFilesDTO
from app.infrastructure.database.models import Base
from app.infrastructure.database.mappers import AcstFilesMapper, PersonalNaksCertificationFilesMapper, PersonalNaksProtocolFilesMapper
from app.config import DBConfig

from funcs import session_maker, engine


@pytest.fixture(scope="session", autouse=True)
def prepare_db():
    assert DBConfig.DB_NAME() == "rhi_test_files"

    async def execute():

        async with engine.connect() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

            await conn.commit()

    asyncio.run(execute())


@pytest.fixture(scope="session")
def add_default_values():

    ident = "f6500b2b-9a05-4e5a-852f-bb7b88efee8b"

    create_acst_dto = CreateAcstFilesDTO(
        ident=UUID(ident),
        acst_number="test_number"
    )

    create_cert_dto = CreatePersonalNaksCertificationFilesDTO(
        ident=UUID(ident),
        certification_numbers=["test_number"]
    )

    create_prot_dto = CreatePersonalNaksProtocolFilesDTO(
        ident=UUID(ident),
        protocol_number="test_number"
    )

    async def execute():

        async with session_maker() as session:
            commiter = SqlAlchemyCommitter(session)

            acst_mapper = AcstFilesMapper(session)
            cert_mapper = PersonalNaksCertificationFilesMapper(session)
            prot_mapper = PersonalNaksProtocolFilesMapper(session)


            await acst_mapper.insert(create_acst_dto)
            await cert_mapper.insert(create_cert_dto)
            await prot_mapper.insert(create_prot_dto)

            await commiter.commit()

    asyncio.run(execute())