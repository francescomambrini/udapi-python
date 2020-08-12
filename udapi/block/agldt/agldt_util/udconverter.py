"""
Deprecated! I am starting a whole new project for a converter

"""


from udapi.core.block import Block
from udapi.block.agldt.agldt_util.subtrees import *
import logging


class UDConverter(Block):
    """
    Convert AGLDT-style trees to UD by re-designing the tree structure when necessary (e.g. coordination,
    preposition/conjunction, ellipsis, copula...).
    It works bottom-up, ordering the structures in each trees using `the get_subtree_depth` function
    defined in `udapi.block.agldt.agldt_util.subtrees`.
    This function sorts the subtrees bottom-up, i.e. from the lowest depth up to the children of the sentence root.
    A subtree is nothing more than a non-leaf node in the dependency tree. Only the subtree-root
    (i.e. the non-leaf node) is returned; children and descendants can be easily obtained using the `Node` methods and
    attributes.

    Note that, as we process bottom-up, we don't need to worry about situations like AuxP governing two coordinated
    nouns. When the transformation reaches the root of the prepositional phrase (the AuxP-node), the coordination at the
    lower level has already been taken care of and appropriately converted.

    """

    def process_tree(self, tree):
        subtrees = get_subtree_depth(tree)

        # subrtrees is a list ofs tuple (subtree_root, depth level) ordered bottom-up
        # i.e. from the
        for subtree in subtrees:
            if is_prague_bridge_subtree(subtrees):
                # what to do if subtree is AuxP/AuxC?
                pass
            elif is_coord_subtree(subtrees):
                # what to do if subtree is COORD?
                pass
            elif is_copula_subtree(subtree):
                # what to do if subtree is the head of a nominal predicate (PNOM)?
                pass
            elif is_ellipsis_subtree(subtree):
                # what to do if subtree is an artificial node?
                pass



