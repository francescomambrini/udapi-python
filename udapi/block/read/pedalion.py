"""Reader for the AGLDT-based XML file used by the Pedalion.
The files are conformant with the version 2 of the Arethusa template.
"""

from udapi.core.basereader import BaseReader
from udapi.core.root import Root
from udapi.block.agldt.agldt_util.agldtfiles import AgldtFiles


class Pedalion(BaseReader):
    """A reader for plain-text sentences (one sentence per line) files."""

    def __init__(self, files='-', cite_el='line', **kwargs):
        self._cite_el = cite_el
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
        xpth = f"word[@{self._cite_el}]"
        if s.xpath(xpth):
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
            postag = w.attrib.get("postag")
            lemma = w.attrib.get("lemma")
            if has_cite:
                c = w.attrib.get(self._cite_el)
                if c:
                    node.misc["Ref"] = c
            else:
                sub = s.attrib.get("subdoc")
                if sub:
                    node.misc["Ref"] = sub
            if w.attrib.get("insertion_id"):
                node.misc["NodeType"] = 'Artificial'
                if postag:
                    node.upos = postag[0]
                    node.xpos = postag
                else:
                    node.upos = '_'
                    node.xpos = '_'
                node.lemma = lemma if lemma else '_'
            else:
                node.upos = postag[0]
                node.xpos = postag
                node.lemma = lemma
            if w.attrib.get("speaker"):
                node.misc["Speaker"] = w.attrib['speaker']
            if w.attrib.get("section"):
                node.misc["Section"] = w.attrib['section']
            nodes.append(node)

        for i, n in enumerate(nodes[1:], 1):
            n.parent = nodes[parents[i]]

        return root
