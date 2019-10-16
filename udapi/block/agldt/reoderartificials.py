from udapi.core.block import Block
import re

art_re = re.compile(r'^E[0-9]+\.([0-9]+)$')

class ReoderArtificials(Block):

    def process_node(self, node):
        if node._misc == "type=artificial":
            node.shift_before_subtree(node)
        prec = node.prev_node(node)
        tok_ind = prec.ord
        m = art_re.search(prec.form)
        if m:
            art_ind = int(m.group(1))
        else:
            art_ind = 1
        node.form = f"E{tok_ind}.{art_ind}"
