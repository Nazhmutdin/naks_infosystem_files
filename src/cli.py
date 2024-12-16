import pathlib
import json
import asyncio

import click
from naks_library.commiter import SqlAlchemyCommitter

from app.application.dto import AcstFilesDTO, PersonalNaksCertificationFilesDTO, PersonalNaksProtocolFilesDTO
from app.infrastructure.database.setup import create_engine, create_session_maker
from app.infrastructure.database.mappers import AcstFilesMapper, PersonalNaksCertificationFilesMapper, PersonalNaksProtocolFilesMapper


@click.group()
def cli(): ...


engine = create_engine()
session_maker = create_session_maker(engine)


async def add_acst_files_data(data: list[AcstFilesDTO]):
    async with session_maker() as session:
        committer = SqlAlchemyCommitter(session)
        mapper = AcstFilesMapper(session)

        for el in data:
            await mapper.insert(el)

        await committer.commit()


@cli.command("add-acst-files-data")
@click.option("--src-path", "-sp", type=str)
def add_acst_files_data_command(
    src_path: str,
):
    path = pathlib.Path(src_path)

    if not path.exists():
        raise ValueError(f"path ({src_path}) not exists")
    
    data = [AcstFilesDTO(**el) for el in json.load(open(path, "r", encoding="utf-8"))]

    asyncio.run(add_acst_files_data(data))


async def add_personal_naks_certification_files_data(data: list[PersonalNaksCertificationFilesDTO]):
    async with session_maker() as session:
        committer = SqlAlchemyCommitter(session)
        mapper = PersonalNaksCertificationFilesMapper(session)

        for el in data:
            await mapper.insert(el)

        await committer.commit()


@cli.command("add-personal-naks-certification-files-data")
@click.option("--src-path", "-sp", type=str)
def add_personal_naks_certification_files_data_command(
    src_path: str,
):
    path = pathlib.Path(src_path)

    if not path.exists():
        raise ValueError(f"path ({src_path}) not exists")
    
    data = [PersonalNaksCertificationFilesDTO(**el) for el in json.load(open(path, "r", encoding="utf-8"))]

    asyncio.run(add_personal_naks_certification_files_data(data))


async def add_personal_naks_protocol_files_data(data: list[PersonalNaksProtocolFilesDTO]):
    async with session_maker() as session:
        committer = SqlAlchemyCommitter(session)
        mapper = PersonalNaksProtocolFilesMapper(session)

        for el in data:
            await mapper.insert(el)

        await committer.commit()


@cli.command("add-personal-naks-protocol-files-data")
@click.option("--src-path", "-sp", type=str)
def add_personal_naks_protocol_files_data_command(
    src_path: str,
):
    path = pathlib.Path(src_path)

    if not path.exists():
        raise ValueError(f"path ({src_path}) not exists")
    
    data = [PersonalNaksProtocolFilesDTO(**el) for el in json.load(open(path, "r", encoding="utf-8"))]

    asyncio.run(add_personal_naks_protocol_files_data(data))


if __name__ == "__main__":
    cli()
