from naks_library.crud_mapper import SqlAlchemyCrudMapper

from app.application.dto import (
    AcstFilesDTO,
    CreateAcstFilesDTO,
    UpdateAcstFilesDTO,
    PersonalNaksCertificationFilesDTO,
    CreatePersonalNaksCertificationFilesDTO,
    UpdatePersonalNaksCertificationFilesDTO,
    PersonalNaksProtocolFilesDTO,
    CreatePersonalNaksProtocolFilesDTO,
    UpdatePersonalNaksProtocolFilesDTO
)


class AcstFilesMapper(SqlAlchemyCrudMapper[AcstFilesDTO, CreateAcstFilesDTO, UpdateAcstFilesDTO]): ...


class PersonalNaksCertificationFilesMapper(SqlAlchemyCrudMapper[PersonalNaksCertificationFilesDTO, CreatePersonalNaksCertificationFilesDTO, UpdatePersonalNaksCertificationFilesDTO]): ...


class PersonalNaksProtocolFilesMapper(SqlAlchemyCrudMapper[PersonalNaksProtocolFilesDTO, CreatePersonalNaksProtocolFilesDTO, UpdatePersonalNaksProtocolFilesDTO]): ...
