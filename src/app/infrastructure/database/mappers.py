from naks_library.crud_mapper import SqlAlchemyCrudMapper
from sqlalchemy import select

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

from app.infrastructure.database.models import AcstFilesModel, PersonalNaksCertificationFilesModel, PersonalNaksProtocolFilesModel


class AcstFilesMapper(SqlAlchemyCrudMapper[AcstFilesDTO, CreateAcstFilesDTO, UpdateAcstFilesDTO]):
    __model__ = AcstFilesModel


    async def get_by_acst_number(self, acst_number) -> AcstFilesDTO | None: 
        stmt = select(AcstFilesModel).where(
            AcstFilesModel.acst_number == acst_number
        )

        res = (await self.session.execute(stmt)).scalar_one_or_none()

        if res:
            return self._convert(res)


    def _convert(self, data: AcstFilesModel):
        return AcstFilesDTO(
            ident=data.ident,
            acst_number=data.acst_number
        )


class PersonalNaksCertificationFilesMapper(SqlAlchemyCrudMapper[PersonalNaksCertificationFilesDTO, CreatePersonalNaksCertificationFilesDTO, UpdatePersonalNaksCertificationFilesDTO]):
    __model__ = PersonalNaksCertificationFilesModel

    def _convert(self, data: PersonalNaksCertificationFilesModel):
        return PersonalNaksCertificationFilesDTO(
            ident=data.ident,
            certification_numbers=data.certification_numbers
        )


    async def get_by_certification_number(self, certification_number) -> PersonalNaksCertificationFilesDTO | None:
        stmt = select(PersonalNaksCertificationFilesModel).where(
            PersonalNaksCertificationFilesModel.certification_numbers.contains([certification_number])
        )

        res = (await self.session.execute(stmt)).scalar_one_or_none()

        if res:
            return self._convert(res)


class PersonalNaksProtocolFilesMapper(SqlAlchemyCrudMapper[PersonalNaksProtocolFilesDTO, CreatePersonalNaksProtocolFilesDTO, UpdatePersonalNaksProtocolFilesDTO]):
    __model__ = PersonalNaksProtocolFilesModel

    def _convert(self, data: PersonalNaksProtocolFilesModel):
        return PersonalNaksProtocolFilesDTO(
            ident=data.ident,
            protocol_number=data.protocol_number
        )


    async def get_by_protocol_number(self, protocol_number) -> PersonalNaksProtocolFilesDTO | None:
        stmt = select(PersonalNaksProtocolFilesModel).where(
            PersonalNaksProtocolFilesModel.protocol_number == protocol_number
        )

        res = (await self.session.execute(stmt)).scalar_one_or_none()

        if res:
            return self._convert(res)
