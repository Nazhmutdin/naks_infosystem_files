from typing import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from naks_library.commiter import SqlAlchemyCommitter
from naks_library.interfaces import ICommitter

from app.application.interfaces.gateways import IAcstFilesGateway, IPersonalNaksCertificationFilesGateway, IPersonalNaksProtocolFilesGateway
from app.application.interactors.acst import (
    DownloadAcstFileInteractor, 
    UploadAcstFileInteractor,
    GetAcstFileDataByNumberInteractor
)
from app.application.interactors.personal_naks_certification import (
    DownloadPersonalNaksCertificationFileInteractor, 
    UploadPersonalNaksCertificationFileInteractor,
    GetPersonalNaksCertificationFileDataByNumberInteractor
)
from app.application.interactors.personal_naks_protocol import (
    DownloadPersonalNaksProtocolFileInteractor, 
    UploadPersonalNaksProtocolFileInteractor,
    GetPersonalNaksProtocolFileDataByNumberInteractor
)

from app.infrastructure.database.mappers import AcstFilesMapper, PersonalNaksCertificationFilesMapper, PersonalNaksProtocolFilesMapper
from app.infrastructure.database.setup import create_engine, create_session_maker


class AppProvider(Provider):

    @provide(scope=Scope.APP)
    def provide_engine(self) -> AsyncEngine:
        return create_engine()


    @provide(scope=Scope.APP)
    def provide_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(engine)


    @provide(scope=Scope.REQUEST)
    async def provide_session(
        self,
        session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterator[AsyncSession]:
        async with session_maker() as session:
            yield session


    @provide(scope=Scope.REQUEST)
    async def provide_committer(
        self, 
        session: AsyncSession
    ) -> ICommitter:
        return SqlAlchemyCommitter(session)
    

    @provide(scope=Scope.REQUEST)
    async def get_acst_files_gateway(
        self,
        session: AsyncSession,
    ) -> IAcstFilesGateway:
        return AcstFilesMapper(session)
    

    @provide(scope=Scope.REQUEST)
    async def get_personal_naks_certification_files_gateway(
        self,
        session: AsyncSession,
    ) -> IPersonalNaksCertificationFilesGateway:
        return PersonalNaksCertificationFilesMapper(session)
    

    @provide(scope=Scope.REQUEST)
    async def get_personal_naks_protocol_files_gateway(
        self,
        session: AsyncSession,
    ) -> IPersonalNaksProtocolFilesGateway:
        return PersonalNaksProtocolFilesMapper(session)


    @provide(scope=Scope.REQUEST)
    def provide_download_acst_file_interactor(
        self,
        gateway: IAcstFilesGateway
    ) -> DownloadAcstFileInteractor:
        return DownloadAcstFileInteractor(
            gateway=gateway
        )


    @provide(scope=Scope.REQUEST)
    def provide_upload_acst_file_interactor(
        self,
        gateway: IAcstFilesGateway,
        committer: ICommitter
    ) -> UploadAcstFileInteractor:
        return UploadAcstFileInteractor(
            gateway=gateway,
            committer=committer
        )


    @provide(scope=Scope.REQUEST)
    def provide_get_acst_file_data_interactor(
        self,
        gateway: IAcstFilesGateway
    ) -> GetAcstFileDataByNumberInteractor:
        return GetAcstFileDataByNumberInteractor(
            gateway=gateway
        )


    @provide(scope=Scope.REQUEST)
    def provide_download_personal_naks_certification_file_interactor(
        self,
        gateway: IPersonalNaksCertificationFilesGateway
    ) -> DownloadPersonalNaksCertificationFileInteractor:
        return DownloadPersonalNaksCertificationFileInteractor(
            gateway=gateway
        )


    @provide(scope=Scope.REQUEST)
    def provide_upload_personal_naks_certification_file_interactor(
        self,
        gateway: IPersonalNaksCertificationFilesGateway,
        committer: ICommitter
    ) -> UploadPersonalNaksCertificationFileInteractor:
        return UploadPersonalNaksCertificationFileInteractor(
            gateway=gateway,
            committer=committer
        )


    @provide(scope=Scope.REQUEST)
    def provide_get_personal_naks_certification_file_data_interactor(
        self,
        gateway: IPersonalNaksCertificationFilesGateway
    ) -> GetPersonalNaksCertificationFileDataByNumberInteractor:
        return GetPersonalNaksCertificationFileDataByNumberInteractor(
            gateway=gateway
        )


    @provide(scope=Scope.REQUEST)
    def provide_download_personal_naks_protocol_file_interactor(
        self,
        gateway: IPersonalNaksProtocolFilesGateway
    ) -> DownloadPersonalNaksProtocolFileInteractor:
        return DownloadPersonalNaksProtocolFileInteractor(
            gateway=gateway
        )


    @provide(scope=Scope.REQUEST)
    def provide_upload_personal_naks_protocol_file_interactor(
        self,
        gateway: IPersonalNaksProtocolFilesGateway,
        committer: ICommitter
    ) -> UploadPersonalNaksProtocolFileInteractor:
        return UploadPersonalNaksProtocolFileInteractor(
            gateway=gateway,
            committer=committer
        )


    @provide(scope=Scope.REQUEST)
    def provide_get_personal_naks_protocol_file_data_interactor(
        self,
        gateway: IPersonalNaksProtocolFilesGateway
    ) -> GetPersonalNaksProtocolFileDataByNumberInteractor:
        return GetPersonalNaksProtocolFileDataByNumberInteractor(
            gateway=gateway
        )
