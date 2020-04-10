"""
Checks the annotation of the so called predicative participles.
The PP are checked against a couple of annotation structures that I recall:
- ATV / AtvV (some files in the AGDT 1.x)
- OBJ (sometimes in Homer)
"""

from udapi.block.agldt.query import Query
import re

reg = re.compile(r'(^A[Tt]v?V)|(OBJ)')
atv = re.compile(r'^A[Tt]v?V')

def _get_part_pred(node):
    try:
        mood = node.xpos[4]
    except IndexError:
        return False
    if mood == 'p' and reg.search(node.deprel):
        if atv.search(node.deprel):
            return True
        if node.deprel[:3] == 'OBJ':
            hasart = False
            for ch in node.children:
                if ch.xpos[0] == 'l':
                    hasart = False
            if not hasart:
                return True
    return False


class PredicativePart(Query):
    def __init__(self):
        super().__init__(_get_part_pred, mark="PartPred")
