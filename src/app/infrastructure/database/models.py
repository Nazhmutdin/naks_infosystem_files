import uuid

from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy.dialects.postgresql import ARRAY
import sqlalchemy as sa


class Base(DeclarativeBase): ...


class AcstFilesModel(Base):
    __tablename__ = "acst_files_table"

    ident: Mapped[uuid.UUID] = sa.Column(sa.UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    acst_number: Mapped[str] = sa.Column(sa.String(), nullable=False)


class PersonalNaksCertificationFilesModel(Base):
    __tablename__ = "personal_naks_certification_files_table"

    ident: Mapped[uuid.UUID] = sa.Column(sa.UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    certification_numbers: Mapped[str] = sa.Column(ARRAY(sa.String), nullable=False)


class PersonalNaksProtocolFilesModel(Base):
    __tablename__ = "personal_naks_protocol_files_table"

    ident: Mapped[uuid.UUID] = sa.Column(sa.UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    personal_number: Mapped[str] = sa.Column(sa.String(), nullable=False)