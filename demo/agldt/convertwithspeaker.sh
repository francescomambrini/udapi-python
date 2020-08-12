#!/bin/bash

udapy read.Agldt files="$1" \
  agldt.SetSpaceAfter \
  agldt.CreateUpos \
  agldt.CreateFeats \
  agldt.ReorderArtificials \
  agldt.agldt_util.SetSpeakers \
  util.Eval doc='doc.meta["docname"]=doc.meta["loaded_from"][:-4]+".conllu"' \
  write.Conllu files="tlg0011.tlg00{$2}.daphne_tb-grc1.conllu"
