"""Reader for the AGLDT XML format
"""

from udapi.core.basereader import BaseReader
from udapi.core.root import Root
from udapi.block.agldt.agldt_util.agldtfiles import AgldtFiles


class Agldt(BaseReader):
    """A reader for plain-text sentences (one sentence per line) files."""

    def __init__(self, files='-', **kwargs):
        super().__init__(files, **kwargs)
        self.files = AgldtFiles(files)


    @staticmethod
    def is_multizone_reader():
        """Can this reader read bundles which contain more zones?.

        This implementation returns always False.
        """
        return False

    def read_tree(self, document=None):
        if self.filehandle is None:
            return None
        try:
            s = next(self.filehandle)
        except StopIteration:
            return None

        root = Root()
        nodes = [root]
        parents = [0]
        words = s.xpath("word")
        if len(words) == 0:
            return None
        root.sent_id = s.attrib.get("id")
        if s.xpath("word[@cite]"):
            has_cite = True
        else:
            has_cite = False

        for w in words:
            node = root.create_child()
            node.ord = int(w.attrib["id"])
            node.form = w.attrib["form"]
            node.feats = '_'
            parents.append(int(w.attrib["head"]))
            node.deprel = w.attrib["relation"]
            if has_cite:
                c = w.attrib.get("cite")
                if c:
                    node.misc["Ref"] = c.split(":")[-1]
            else:
                sub = s.attrib.get("subdoc")
                if sub:
                    node.misc["Ref"] = sub
            if w.attrib.get("insertion_id"):
                node.misc["NodeType"] = 'Artificial'
                node.upos = '_'
                node.xpos = '_'
                node.lemma = '_'
            else:
                tag = w.attrib["postag"]
                node.upos = tag[0]
                node.xpos = tag
                node.lemma = w.attrib["lemma"]
            nodes.append(node)

        for i, n in enumerate(nodes[1:], 1):
            n.parent = nodes[parents[i]]

        return root
