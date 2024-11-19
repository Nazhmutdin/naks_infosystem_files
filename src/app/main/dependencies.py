from dishka import Provider, Scope, provide

from app.application.interactors.acst import DownloadFileInteractor


class AppProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def provide_download_file_interactor(self) -> DownloadFileInteractor:
        return DownloadFileInteractor()
