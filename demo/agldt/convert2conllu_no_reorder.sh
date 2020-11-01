#!/bin/bash

# Performs a shallow conversion from AGLDT XML format to CoNLL-U
# Uses the modules in the following files in the block folder:
# - read/agldt.py :  loads the AGLDT trees
# - agldt/setspaceafter.py : guess tokens that are not followed by space in text
# - agldt/createupos.py : create the UD upos
# - agldt/createfeats.py : populate the feats colum

PASSED=$1
OUTDIR=$2

if [ -d "${PASSED}" ] ; then
  FS="!$PASSED/*.xml";
# elif [ -f "${PASSED}" ]; then
#   FS=$PASSED ;
else
  FS=$PASSED ;
fi
    
    
udapy read.Agldt files="$FS" fix_cycles=True \
  agldt.CreateUpos \
  agldt.CreateFeats \
  agldt.SetSpaceAfter \
  util.Eval doc='doc.meta["docname"]=doc.meta["loaded_from"].split("/")[-1][:-4]+".conllu"' \
  write.Conllu docname_as_file=1
  
mv -v *.conllu $OUTDIR
