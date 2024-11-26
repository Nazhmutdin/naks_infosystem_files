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


class IAcstFilesGateway(ICrudGateway[AcstFilesDTO, CreateAcstFilesDTO, UpdateAcstFilesDTO]): 

    async def get_by_acst_number(self, acst_number) -> AcstFilesDTO | None: ...


class IPersonalNaksCertificationFilesGateway(ICrudGateway[PersonalNaksCertificationFilesDTO, CreatePersonalNaksCertificationFilesDTO, UpdatePersonalNaksCertificationFilesDTO]): 

    async def get_by_certification_number(self, certification_number) -> PersonalNaksCertificationFilesDTO | None: ...


class IPersonalNaksProtocolFilesGateway(ICrudGateway[PersonalNaksProtocolFilesDTO, CreatePersonalNaksProtocolFilesDTO, UpdatePersonalNaksProtocolFilesDTO]):  

    async def get_by_protocol_number(self, protocol_number) -> PersonalNaksProtocolFilesDTO | None: ...
