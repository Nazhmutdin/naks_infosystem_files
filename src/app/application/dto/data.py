from uuid import UUID, uuid4

from pydantic.dataclasses import dataclass, Field


@dataclass
class AcstFilesDTO:
    acst_number: str
    ident: UUID


@dataclass
class CreateAcstFilesDTO(AcstFilesDTO):
    ident: UUID = Field(default_factory=uuid4)


@dataclass
class UpdateAcstFilesDTO(AcstFilesDTO): 
    acst_number: str | None


@dataclass
class PersonalNaksCertificationFilesDTO:
    certification_number: str
    ident: UUID


@dataclass
class CreatePersonalNaksCertificationFilesDTO(PersonalNaksCertificationFilesDTO):
    ident: UUID = Field(default_factory=uuid4)


@dataclass
class UpdatePersonalNaksCertificationFilesDTO(PersonalNaksCertificationFilesDTO): 
    certification_number: str | None


@dataclass
class PersonalNaksProtocolFilesDTO:
    protocol_number: str
    ident: UUID


@dataclass
class CreatePersonalNaksProtocolFilesDTO(PersonalNaksProtocolFilesDTO):
    ident: UUID = Field(default_factory=uuid4)


@dataclass
class UpdatePersonalNaksProtocolFilesDTO(PersonalNaksProtocolFilesDTO): 
    protocol_number: str | None