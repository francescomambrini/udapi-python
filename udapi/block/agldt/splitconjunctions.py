#!/usr/bin/env python

"""WARNING! Not yet tested
"""

import re
from udapi.core.block import Block
import logging

oude = re.compile(r"(οὐ)(δ[έὲ'])")  # ["οὐδέ", "οὐδὲ", "οὐδ'"]
mhde = re.compile(r"(μη)(δ[έὲ'])")  # ["μηδέ", "μηδὲ", "μηδ'"]
eite = re.compile(r"(εἴ)(τε|θ'|τ')")  # ["εἴτε", "εἴτ'", "εἴθ'"]
oute = re.compile(r"(οὔ)(τε|θ'|τ')")  # ["οὔτε", "οὔτ'", "οὔθ'"]
mhte = re.compile(r"(μή)(τε|θ'|τ')")  # ["μήτε", "μήτ'", "μήθ'"]

conjs = ["οὐδέ", "οὐδὲ", "οὐδ'", "μηδέ", "μηδὲ", "μηδ'", "εἴτε", "εἴτ'", "εἴθ'",
         "οὔτε", "οὔτ'", "οὔθ'", "μήτε", "μήτ'", "μήθ'"]


class SplitConjunctions(Block):

    def process_node(self, node):
        if node.form in conjs:
            root = node.root

            newnode = root.create_child(xpos='c--------', afun='UNDEF')
            newnode.shift_before_node(node)

            moude = oude.search(node.form)
            mmhde = mhde.search(node.form)
            meite = eite.search(node.form)
            moute = oute.search(node.form)
            mmhte = mhte.search(node.form)

            if moude:
                newnode.form = moude.group(1)
                node.form = moude.group(2)
                newnode.lemma = "οὐδέ"
                node.lemma = "οὐδέ"
            elif mmhde:
                newnode.form = moude.group(1)
                node.form = moude.group(2)
                newnode.lemma = "μηδέ"
                node.lemma = "μηδέ"
            elif meite:
                newnode.form = moude.group(1)
                node.form = moude.group(2)
                newnode.lemma = "εἴτε"
                node.lemma = "εἴτε"
            elif moute:
                newnode.form = moude.group(1)
                node.form = moude.group(2)
                newnode.lemma = "οὔτε"
                node.lemma = "οὔτε"
            elif mmhte:
                newnode.form = moude.group(1)
                node.form = moude.group(2)
                newnode.lemma = "μήτε"
                node.lemma = "μήτε"

            logging.warning(f"Sent {root.sent_id}: new node created (id={newnode.ord}) by splitting {node.form}")
