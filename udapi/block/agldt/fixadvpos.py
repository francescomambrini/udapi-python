from udapi.core.block import Block
import logging


class FixAdvPos(Block):
    """
    If an adverb is syntactically annotated as preposition, then
    it's a preposition!
    If it behaves as a conjuncion, it's a conjunction!
    """

    def process_node(self, node):
        if node.xpos[0] == 'd':
            if node.deprel == 'AuxP':
                node.xpos = "r--------"
                logging.info(f"Word {node.address()} changed to {node.xpos}")
            elif node.deprel == 'AuxC':
                node.xpos = 'c--------'
                logging.info(f"Word {node.address()} changed to {node.xpos}")
