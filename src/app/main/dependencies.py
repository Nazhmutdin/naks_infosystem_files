from typing import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from naks_library.commiter import SqlAlchemyCommitter

from app.application.interfaces.gateways import IAcstFilesGateway, IPersonalNaksCertificationFilesGateway, IPersonalNaksProtocolFilesGateway
from app.application.interactors.acst import DownloadAcstFileInteractor, UploadAcstFileInteractor
from app.application.interactors.personal_naks_certification import DownloadPersonalNaksCertificationFileInteractor, UploadPersonalNaksCertificationFileInteractor
from app.application.interactors.personal_naks_protocol import DownloadPersonalNaksProtocolFileInteractor, UploadPersonalNaksProtocolFileInteractor

from app.infrastructure.database.mappers import AcstFilesMapper, PersonalNaksCertificationFilesMapper, PersonalNaksProtocolFilesMapper
from app.infrastructure.database.setup import create_engine, create_session_maker


class AppProvider(Provider):

    @provide(scope=Scope.APP)
    def provide_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(engine)


    @provide(scope=Scope.APP)
    def provide_engine(self) -> AsyncEngine:
        return create_engine()


    @provide(scope=Scope.REQUEST)
    async def provide_committer(
        self, session_pool: async_sessionmaker[AsyncSession]
    ) -> AsyncIterator[SqlAlchemyCommitter]:
        async with session_pool() as session:
            yield SqlAlchemyCommitter(session)
    

    @provide(scope=Scope.REQUEST)
    async def get_acst_files_gateway(
        self,
        committer: SqlAlchemyCommitter,
    ) -> IAcstFilesGateway:
        return AcstFilesMapper(committer.session)
    

    @provide(scope=Scope.REQUEST)
    async def get_personal_naks_certification_files_gateway(
        self,
        committer: SqlAlchemyCommitter,
    ) -> IPersonalNaksCertificationFilesGateway:
        return PersonalNaksCertificationFilesMapper(committer.session)
    

    @provide(scope=Scope.REQUEST)
    async def get_personal_naks_protocol_files_gateway(
        self,
        committer: SqlAlchemyCommitter,
    ) -> IPersonalNaksProtocolFilesGateway:
        return PersonalNaksProtocolFilesMapper(committer.session)


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
        gateway: IAcstFilesGateway
    ) -> UploadAcstFileInteractor:
        return UploadAcstFileInteractor(
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
        gateway: IPersonalNaksCertificationFilesGateway
    ) -> UploadPersonalNaksCertificationFileInteractor:
        return UploadPersonalNaksCertificationFileInteractor(
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
        gateway: IPersonalNaksProtocolFilesGateway
    ) -> UploadPersonalNaksProtocolFileInteractor:
        return UploadPersonalNaksProtocolFileInteractor(
            gateway=gateway
        )
