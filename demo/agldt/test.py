from udapi.block.write.agldt import Agldt as AgldtWriter
from udapi.block.read.pedalion import Pedalion
from udapi.block.read.agldt import Agldt as AgldtReader
from udapi.core.document import Document

pedpath = "/home/francesco/Documents/work/Nextcloud/Documents/Projects/Daphne/data/annotation/in_progress/tlg0011/tlg0011.tlg006.daphne_tb-grc1.xml"
gorman = '/home/francesco/Documents/work/Nextcloud/Documents/Projects/gorman-trees/public/xml/antiphon-1-bu2.xml'

doc = Document()
pedreader = Pedalion(pedpath)
pedreader.apply_on_document(doc)

# diagnostica varia
bun = doc.bundles[0]
tree = bun.trees[0]
nodes = tree.descendants
for n in nodes:
    print(n.form, n.xpos)

writer = AgldtWriter("/home/francesco/Desktop/test.xml")
writer.apply_on_document(doc)

# Test of test.xml!
agdltdoc = Document()
agdtreader = AgldtReader("/home/francesco/Desktop/test.xml")
agdtreader.apply_on_document(agdltdoc)
