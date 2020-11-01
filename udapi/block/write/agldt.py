"""A writer block for the AGLDT format.
A quick-and-dirty remapping of the logic of the other Udapi writers to 
the strucuture of the AGLDT XML files.
lxml.etree is used to insure that the XML string is properly escaped!
"""

import os
from udapi.core.basewriter import BaseWriter
from lxml import etree
import re
import logging

reg_speaker = re.compile(r'Speaker=((\w|\W)+$)')


class Agldt(BaseWriter):

    def __init__(self, files='-', cite_el='Ref', includeSpeakers=False, namespace="greekLit", **kwargs):
        """
        :param cite_el: name of the element holding the reference to passage in canonical format; default 'Ref', as
        produced by the reader.Agldt. Warning! cite_el must be an attribute of the misc column.
        """
        self._cite_el = cite_el
        self._include_speakers = bool(includeSpeakers)
        self._namespace = namespace
        super().__init__(files, **kwargs)

    def before_process_document(self, doc):
        super().before_process_document(doc)
        print('<treebank version="1.5" direction="ltr" format="aldt">\n')

    def process_tree(self, tree):
        file_name = os.path.split(tree.bundle.document().meta['loaded_from'])[-1]
        tree.misc['file_name'] = file_name
        doc_name = os.path.splitext(file_name)[0]
        doc_id = f'urn:cts:{self._namespace}:{doc_name}'
        subdoc = ''
        if self._cite_el:
            citable = [n.misc[self._cite_el] for n in tree.descendants if n.misc[self._cite_el]]
            if citable[0] == citable[-1]:
                subdoc = str(citable[0])
            else:
                subdoc = f'{citable[0]}-{citable[-1]}'

        if self._include_speakers:
            try:
                speaker = reg_speaker.search(tree.comment).group(1)
            except AttributeError:
                speaker = ''
            print(f'   <sentence id="{tree.sent_id}" document_id="{doc_id}" subdoc="{subdoc}" speaker="{speaker}">')

        else:
            print(f'   <sentence id="{tree.sent_id}" document_id="{doc_id}" subdoc="{subdoc}">')

        for node in tree.descendants:
            self.print_word(node)

        print('   </sentence>')

    def _get_prev_non_artif(self, node, i=0):
        prev = node.prev_node
        if prev.misc['NodeType'] != 'Artificial':
            p = prev
        else:
            i += 1
            p, i = self._get_prev_non_artif(prev, i)
        return p, i

    def _get_ins_point(self, node,):
        i = 0
        prev, i = self._get_prev_non_artif(node, i)
        index = chr(ord('e') + i)
        num = str(prev.ord)
        return f'{num.zfill(4)}{index}'

    def print_word(self, node):
        head = str(node.parent.ord)
        wid = str(node.ord)
        w = etree.Element("word")
        
        # we make sure to enforce the same attribute order: 
        # more verbose code, but much better for human readability!
        w.set("id", wid) 
        w.set("form", node.form)
        
        if node.misc['NodeType'] == 'Artificial':
            ipoint = self._get_ins_point(node)
            w.set("insertion_id", ipoint) # if ipoint else ''
            w.set("artificial",  "elliptic")
            if node.xpos != '_':
                w.set("postag", node.xpos)
            if node.lemma != "_":
                w.set("lemma", node.lemma)
        else:
            w.set("lemma", node.lemma)
            w.set("postag", node.xpos)
            w.set("cite", node.misc["Ref"])
            
        w.set("head", head)
        w.set("relation", node.deprel)
        s = "      " + etree.tostring(w, encoding="utf8").decode("utf8")
        print(s)

    def after_process_document(self, doc):
        print("</treebank>\n")
        super().after_process_document(doc)
