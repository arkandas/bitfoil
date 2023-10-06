class ShopIndex:
    def __init__(self, success):
        self.success = success
        self.files: list[dict] = []
        self.directories: list[str] = []

    def to_json_dict(self):
        return self.__dict__


class IndexFile:
    def __init__(self, url, size):
        self.url = url
        self.size = size

    def to_json_dict(self):
        return self.__dict__
