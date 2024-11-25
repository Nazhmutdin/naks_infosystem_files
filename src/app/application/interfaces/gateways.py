from naks_library.interfaces import ICrudGateway

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


class IAcstFilesGateway(ICrudGateway[AcstFilesDTO, CreateAcstFilesDTO, UpdateAcstFilesDTO]): ...


class IPersonalNaksCertificationFilesGateway(ICrudGateway[PersonalNaksCertificationFilesDTO, CreatePersonalNaksCertificationFilesDTO, UpdatePersonalNaksCertificationFilesDTO]): ...


class IPersonalNaksProtocolFilesGateway(ICrudGateway[PersonalNaksProtocolFilesDTO, CreatePersonalNaksProtocolFilesDTO, UpdatePersonalNaksProtocolFilesDTO]): ...
