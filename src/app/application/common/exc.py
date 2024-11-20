


class FileNotFound(Exception):
    def __init__(self, mode: str, filename: str):
        self.mode = mode
        self.filename = filename
