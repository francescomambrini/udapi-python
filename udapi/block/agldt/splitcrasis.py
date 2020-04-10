#!/usr/bin/env python

"""WARNING! Not yet tested
"""


import re
from udapi.core.block import Block
import logging


reg_krasis = re.compile(r"([κχ])(?=\w?[ὐὖὔἰἴἀἂἄἈὠᾀᾆἠὢὤὦᾦ])")
reg_artkras = re.compile(r"([τθκχ])(?=\w?[ὐὖὔἰἴἀἂἄἈὠᾀᾆἠὢὤὦᾦ])")


class SplitCrasis(Block):
    def __init__(self, split_article=False, **kwargs):
        self.regexp = reg_krasis if not split_article else reg_artkras
        super().__init__(**kwargs)

    def process_node(self, node):
        m = self.regexp.search(node.form)
        if m:
            root = node.root
            cj = m.group(1)
            if cj in ['κ', 'χ']:
                newnode = root.create_child(form=cj, lemma='καί', xpos='c--------', afun='UNDEF')
            elif cj in ['τ', 'θ']:
                newnode = root.create_child(form=cj, lemma='ὁ', xpos='l--------', afun='UNDEF')
            else:
                raise ValueError(f"{cj}: unknown crasis!")
            newnode.shift_before_node(node)
            cite = node.misc['Ref']
            if cite:
                newnode.misc['Ref'] = cite
            node.form = node.form.replace(cj, '')
            logging.warning(f"Sent {root.sent_id}: new node created (id={newnode.ord}) by splitting {node.form}")
