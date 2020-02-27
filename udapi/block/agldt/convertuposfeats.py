from udapi.core.block import Block
import udapi
import re
import os


def verb2part(tag):
    if re.search(r'^v...p', tag):
        tag = 't' + tag[1:]
    return tag

def pronNoPers(tag):
    if re.search(r'^p[123]', tag):
        tag = 'p-' + tag[2:]
    return tag

def normalize_tag(tag):
    tag = verb2part(tag)
    tag = pronNoPers(tag)
    tag = tag.replace('_', '-')
    return tag

conv = {}
cpath = os.path.join(os.path.dirname(udapi.__file__), "lib/conversion_table.csv")
with open(cpath) as f:
    for l in f:
        tag, upos, feats, _ = l.split('\t')
        conv[tag] = (upos, feats)

class ConvertUposFeats(Block):

    def process_node(self, node):
        t = normalize_tag(node.xpos)
        convtag = conv.get(t)
        if not convtag:
            convtag = ('X', '_')
            node.misc = "ConversionError=true"
        node.upos = convtag[0]
        node.feats = convtag[1]
