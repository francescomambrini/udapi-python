#!/usr/bin/env bash

udapy read.Agldt files="!$HOME/Documents/work/Nextcloud/Documents/Projects/Daphne/data/annotation/*/*/*.xml" \
  agldt.SetSpaceAfter \
  agldt.CreateUpos \
  agldt.CreateFeats \
  agldt.ReorderArtificials \
  agldt.agldt_util.SetSpeakers \
  util.Eval doc='doc.meta["docname"]=doc.meta["loaded_from"][:-4]+".conllu"' \
  write.Conllu docname_as_file=1