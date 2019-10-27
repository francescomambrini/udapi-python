from udapi.block.write.conllu import Conllu
from udapi.block.agldt.agldt_util.listfiles import ListFiles


class WriteConlluList(Conllu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.files = ListFiles(fnames=kwargs['files'])
