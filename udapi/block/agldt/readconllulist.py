from udapi.block.read.conllu import Conllu
from udapi.block.agldt.agldt_util.listfiles import ListFiles


class ReadConlluList(Conllu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.files = ListFiles(fnames=kwargs['files'])
