from dishka import Provider, Scope, provide

from app.application.interactors.acst import DownloadAcstFileInteractor, UploadAcstFileInteractor
from app.application.interactors.personal_naks_certification import DownloadPersonalNaksCertificationFileInteractor, UploadPersonalNaksCertificationFileInteractor
from app.application.interactors.personal_naks_protocol import DownloadPersonalNaksProtocolFileInteractor, UploadPersonalNaksProtocolFileInteractor


class AppProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_download_acst_file_interactor(self) -> DownloadAcstFileInteractor:
        return DownloadAcstFileInteractor()


    @provide(scope=Scope.REQUEST)
    def provide_upload_acst_file_interactor(self) -> UploadAcstFileInteractor:
        return UploadAcstFileInteractor()


    @provide(scope=Scope.REQUEST)
    def provide_download_personal_naks_certification_file_interactor(self) -> DownloadPersonalNaksCertificationFileInteractor:
        return DownloadPersonalNaksCertificationFileInteractor()


    @provide(scope=Scope.REQUEST)
    def provide_upload_personal_naks_certification_file_interactor(self) -> UploadPersonalNaksCertificationFileInteractor:
        return UploadPersonalNaksCertificationFileInteractor()


    @provide(scope=Scope.REQUEST)
    def provide_download_personal_naks_protocol_file_interactor(self) -> DownloadPersonalNaksProtocolFileInteractor:
        return DownloadPersonalNaksProtocolFileInteractor()


    @provide(scope=Scope.REQUEST)
    def provide_upload_personal_naks_protocol_file_interactor(self) -> UploadPersonalNaksProtocolFileInteractor:
        return UploadPersonalNaksProtocolFileInteractor()
