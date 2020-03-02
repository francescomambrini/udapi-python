#!/bin/bash

udapy read.Agldt files='/home/francesco/Documents/work/Nextcloud/Documents/Projects/Daphne/data/annotation/tlg0011/tlg003/tlg0011.tlg003.daphne_tb-grc1.xml' \
  agldt.SetSpaceAfter \
  agldt.CreateUpos \
  agldt.CreateFeats \
  agldt.ReorderArtificials \
  agldt.agldt_util.SetSpeakers \
  util.Eval doc='doc.meta["docname"]=doc.meta["loaded_from"][:-4]+".conllu"' \
  write.Conllu docname_as_file=1