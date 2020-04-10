"""
Checks if the OBJ_AP tag is used for proleptic nouns/pronouns and clauses
"""

from udapi.block.agldt.query import Query


def _check_apos(node):
    if '_AP' in node.deprel:
        if node.xpos[0] == 'p':
            parent = node.parent
            if parent.deprel != 'APOS':
                parent = parent.parent
            for ch in parent.children:
                if '_AP' in ch.deprel and ch.xpos[0] == 'v':
                    return True
    return False


class AposClause(Query):
    def __init__(self):
        super().__init__(_check_apos, mark="AposClause")