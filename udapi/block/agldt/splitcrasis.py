#/usr/bin/env python

import re
from udapi.core.block import Block


reg_krasis = re.compile(r"[κχ](?=\w?[ὐὖὔἰἴἀἂἄἈὠᾀᾆἠὢὤὦᾦ])")
reg_artkras = re.compile(r"[τθκχ](?=\w?[ὐὖὔἰἴἀἂἄἈὠᾀᾆἠὢὤὦᾦ])")


class SplitCrasis(Block):
    def __init__(split_article=False):
        self.regexp = reg_krasis if not split_article else reg_artkras

    def process_tree(self, tree):
        pass
