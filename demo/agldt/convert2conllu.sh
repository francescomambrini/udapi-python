#!/bin/bash

# Performs a shallow conversion from AGLDT XML format to CoNLL-U
# Uses the modules in the following files in the block folder:
# - read/agldt.py :  loads the AGLDT trees
# - agldt/setspaceafter.py : guess tokens that are not followed by space in text
# - agldt/createupos.py : create the UD upos
# - agldt/createfeats.py : populate the feats colum
# - agldt/reorderartificials.py : reoder the artificial nodes before their subtree


udapy read.Agldt files='!sample_files/*.xml' \
  agldt.SetSpaceAfter \
  agldt.CreateUpos \
  agldt.CreateFeats \
  agldt.ReorderArtificials \
  util.Eval doc='doc.meta["docname"]=doc.meta["loaded_from"][:-4]+".conllu"' \
  write.Conllu docname_as_file=1