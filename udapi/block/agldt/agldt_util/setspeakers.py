from udapi.core.block import Block
import os
import csv
import logging


class SetSpeakers(Block):
    def process_document(self, document):
        dirname, fname = os.path.split(document.meta["loaded_from"])
        spfile = os.path.join(dirname, "speakers.csv")
        if not os.path.isfile(spfile):
            logging.error(f'No speaker file for {fname}')
        else:
            with open(spfile) as f:
                reader = csv.reader(f, delimiter="\t")
                speakers = list(reader)[1:]
                assert len(document.bundles) == len(speakers), \
                    f"List of sentences ({len(document.bundles)}) not in sync with list of speakers ({len(speakers)})"
                for speaker, bundle in zip(speakers, document.bundles):
                    tree = bundle.get_tree()
                    tree.add_comment(f"Speaker={speaker[-1]}")
