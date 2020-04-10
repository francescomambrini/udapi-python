"""
Checks whether any given token is the half of a split conjunction.
The code is just a sanity check to see that:
- split conjunctions are tokenized as 2
- the lemmatization and pos tagging is coherent
"""

from udapi.block.agldt.query import Query
import re

conj_pattern = r'''^εἴ(τε|[τθ][᾽'])$  # conjunctions: εἴτε
            | ^(μη|μή|οὐ)(τε\b|δ[έὲ]\b|[τδθ][᾽'])$      #
            '''

conj_reg = re.compile(conj_pattern,
            flags=re.UNICODE | re.MULTILINE | re.DOTALL | re.VERBOSE)

def _is_compound_cojn(node):
    """Returns true only if first-element in a compound conjunction
    (εἴτε, μήτε, μηδέ, οὐδέ, οὔτε)
    """
    nf = ""
    if node.next_node:
        nf = node.next_node.form
    concat = node.form + nf
    if conj_reg.search(concat):
        return True
    return False

class CompoundConj(Query):
    def __init__(self):
        super().__init__(_is_compound_cojn, mark="CompConj")
