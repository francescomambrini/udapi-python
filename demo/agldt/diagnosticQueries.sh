#!/usr/bin/env bash

DAPHNEDATA="$HOME/Documents/work/Nextcloud/Documents/Projects/Daphne/data/annotation"

udapy read.Agldt files="$DAPHNEDATA/in_progress/tlg0085/tlg0085.tlg005.daphne_tb-grc1.xml" \
  agldt.diagnostics.PredicativePart \
  write.Conllu > "$HOME/Desktop/results.conllu"