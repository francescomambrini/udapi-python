from udapi.core.files import Files


class ListFiles(Files):
    def __init__(self, fnames):
        super().__init__(filenames=fnames)

    def string_to_filenames(self, string):
        assert string[0] == '@', "File is not a list"
        return self._token_to_filenames(string)
