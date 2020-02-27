"""Heavily inspired by https://github.com/ufal/treex/blob/master/lib/Treex/Block/HamleDT/Udep.pm

It performs just a very coarse-grained conversion, being just a preliminary step in the workflow:
- convert AGLDT format to CoNLL-U
- generate UPOS and FEATS
- **shallo convert** the deprels [this script]
- use Treex to restructure the trees based on UD conventions
- post-process and adjust the converted trees

"""
from udapi.core.block import Block


class ConvertDeprel(Block):

    def process_tree(self, tree):
        descs = tree.descendants
        for node in descs:
            node.misc["original"] = node.deprel

        for node in descs:
            deprel = node.misc["original"].split("_")[0]
            if '_CO' in node.deprel:
                node.misc["isMember"] = '1'
            if '_AP' in node.deprel:
                node.misc["isAposMember"] = '1'
            parent = node.parent

            # punctuation
            if node.xpos[0] == 'u':
                if deprel == 'COORD':
                    node.deprel = 'coord'
                else:
                    node.deprel = 'punct'

            elif deprel == "COORD" :
                node.deprel = 'coord'
            elif deprel == 'AuxP' :
                node.deprel = 'case'
            elif deprel == 'AuxC':
                node.deprel = 'mark'
            elif deprel == 'PRED':
                node.deprel = 'root'
            elif deprel == 'SBJ':
                # subject: clausal or nominal?
                if node.xpos[0] == ['v']:
                    newdp = 'csubj'
                else:
                    newdp = 'nsubj'
                # subject of passive or active verb?
                if parent.feats["Voice"] == 'Passive' and node.lemma.endswith('μαι') == False:
                    node.deprel = f'{newdp}:pass'
                else:
                    node.deprel = newdp
            elif deprel == 'OBJ':
                # let us start by making verbal clauses always ccomp;
                # control (xcomp) in Greek is a more complicated matter
                if node.xpos[0] == 'v':
                    node.deprel = 'ccomp'
                else:
                    if parent.feats["Voice"] == 'Passive' and node.lemma.endswith('μαι') == False:
                        node.deprel = 'obj:agent'
                    else:
                        if parent.misc["original"] == 'AuxP':
                            node.deprel = 'obl:arg'
                        else:
                            node.deprel = 'obj'
            elif deprel == 'PNOM':
                if node.xpos[0] == 'v' and node.feats['VerbForm'] != 'Part':
                    node.deprel = 'ccomp'
                else:
                    node.deprel = 'pnom'
            elif deprel == 'ADV':
                if node.xpos in ['v', 't']:
                    node.deprel = 'advcl'
                if node.xpos in ['n', 'a', 'm']:
                    node.deprel = 'obl'
                else:
                    node.deprel = 'advmod'

            elif deprel == 'ATR':
                if node.upos == 'DET':
                    node.deprel = 'det'
                elif node.xpos[0] in ['a', 't']:
                    node.deprel = 'amod'
                elif node.xpos[0] == 'd':
                    node.deprel = 'advmod'
                elif node.xpos[0] == 'v':
                    if node.xpos[4] == 'p':
                        node.deprel = 'amod'
                    else:
                        node.deprel = 'acl'
                else:
                    node.deprel = 'nmod'
            elif deprel in ['ATV', 'AtvV', 'OCOMP']:
                node.deprel = 'xcomp'
            elif deprel == 'AuxY':
                if parent.misc["original"] == 'COORD':
                    node.deprel = 'cc'
                elif parent.misc['original'] in ['AuxC', 'ATV', 'AtvV']:
                    node.deprel = 'mark'
                elif parent.upos[0] in ['v', 't']:
                    node.deprel = 'advmod'
            elif node.xpos != '_' and node.xpos[7] == 'v':
                node.deprel = 'vocative'
            elif deprel == 'APOS':
                node.deprel = 'appos'
            else:
                # fallback deprel
                node.deprel = f"dep:{deprel}"

        for node in descs:
            node.misc["original"] = None
