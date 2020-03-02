#!/bin/bash

# Performs a shallow conversion from AGLDT XML format to CoNLL-U
# Uses the modules in the following files in the block folder:
# - read/agldt.py
# - agldt/setspaceafter.py


udapy read.Agldt files='!sample_files/*.xml' \
  agldt.SetSpaceAfter \
  util.Eval doc='doc.meta["docname"]=doc.meta["loaded_from"][:-4]+".conllu"' \
  write.Conllu docname_as_file=1