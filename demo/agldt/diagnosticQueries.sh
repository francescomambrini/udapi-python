#!/usr/bin/env bash

DAPHNEDATA="$HOME/Documents/work/Nextcloud/Documents/Projects/Daphne/data/annotation"

udapy read.Agldt files="$DAPHNEDATA/in_progress/tlg0085/tlg0085.tlg007.daphne_tb-grc1.xml" \
  agldt.diagnostics.AposClause \
  write.Conllu > "$HOME/Desktop/results.conllu" \

  ## agldt.diagnostics.PredicativePart \
  ## util.Filter mark="ClauseAP" keep_tree_if_node="'_AP'in node.deprel and node.xpos[0] == 'v'"
  ## util.Filter mark="OBJNoun" keep_tree_if_node="node.deprel=='OBJ' and node.parent.xpos[0] == 'n'"