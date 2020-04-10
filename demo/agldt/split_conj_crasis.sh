#!/usr/bin/env bash

udapy read.Agldt files="!$HOME/Documents/work/Nextcloud/Documents/Projects/Daphne/data/annotation/in_progress/tlg0085/tlg0085.tlg003.daphne_tb-grc1.xml" \
  agldt.SplitCrasis \
  agldt.SplitConjunctions \
  write.Agldt files="$HOME/Desktop/tlg0085.tlg003.daphne_tb-grc1_TEST.xml"
