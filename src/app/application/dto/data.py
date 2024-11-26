from uuid import UUID

from pydantic.dataclasses import dataclass


@dataclass
class AcstFilesDTO:
    ident: UUID
    acst_number: str


@dataclass
class CreateAcstFilesDTO(AcstFilesDTO): ...


@dataclass
class UpdateAcstFilesDTO(AcstFilesDTO): 
    acst_number: str | None


@dataclass
class PersonalNaksCertificationFilesDTO:
    ident: UUID
    certification_numbers: list[str]


@dataclass
class CreatePersonalNaksCertificationFilesDTO(PersonalNaksCertificationFilesDTO): ...


@dataclass
class UpdatePersonalNaksCertificationFilesDTO(PersonalNaksCertificationFilesDTO): 
    certification_numbers: list[str] | None


@dataclass
class PersonalNaksProtocolFilesDTO:
    ident: UUID
    protocol_number: str


@dataclass
class CreatePersonalNaksProtocolFilesDTO(PersonalNaksProtocolFilesDTO): ...


@dataclass
class UpdatePersonalNaksProtocolFilesDTO(PersonalNaksProtocolFilesDTO): 
    protocol_number: str | None