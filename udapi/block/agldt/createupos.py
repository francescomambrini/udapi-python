from udapi.core.block import Block


parts = ['ἆρα', 'αὖ', 'γάρ', 'γε', 'γοῦν', 'δή', 'εἶτα', 'καίπερ',
             'καίτοι', 'μά', 'μέν', 'μέντοι', 'μήν', 'μῶν',
             'οὖν', 'ποθι', 'περ', 'ποτέ', 'πού', 'πω', 'τοίνυν', 'τοι', 'τοιγάρ',
             'ἀτάρ', 'ἄν', 'ἄν1', 'ἄρα', 'ἆρα', 'ἤτοι', 'ἦ']

cord_conjs =  ['-δέ', '-τε', 'δέ', 'εἴτε', 'εἶτα', 'ἤ1', 'ἤ', 'ἠέ1', 'καί', 'καίτοι', 'καί', 'μέντοι', 'μήτε', 'μηδέ', 'οὐδέ',
         'οὐδέ', 'οὐδέ', 'οὔτε', 'τε', 'ἀλλά', 'ἀλλά', 'ἠδέ', 'ἠδέ1',  'ἤτε1', 'ἰδέ', 'ἰδέ1', 'ἔπειτα']

dets = ['ἐμός', 'σός', 'ἡμέτερος','ὑμέτερος', 'νωΐτερος', 'σφέτερος', 'ἐμαυτοῦ', 'σαυτοῦ', 'ἑαυτοῦ',
        'ἄλλος', 'ὅδε', 'οὗτος', 'ἐκεῖνος', 'τόσος', 'τοσόσδε', 'ὁ',
        'τοσοῦτος', 'τοῖος', 'τοιόσδε', 'τοιοῦτος', 'τήλικος', 'τηλικόσδε',
        'τηλικοῦτος', 'τίς', 'πότερος', 'πόσος', 'ποῖος', 'πηλίκος', 'πᾶς',
        'ὁποῖος', 'ὅσος', 'ὁπόσος', 'ὁπότερος', 'ἡλίκος', 'ὁπηλίκος', 'τις',
        'ὅστις', 'ἑκάτερος', 'ἕκαστος', 'ποσός', 'ποιός', 'οἷος']


class CreateUpos(Block):

    def process_node(self, node):
        newupos = 'X'
        if node.xpos[0] == "a":
            newupos = "ADJ"
        elif node.xpos[0] == 'l':
            newupos = 'DET'
        elif node.xpos[0] == 'i':
            newupos = 'INTJ'
        elif node.xpos[0] == 'r':
            newupos = 'ADP'
        elif node.xpos[0] == 'p':
            newupos = "PRON"
        elif node.xpos[0] in ["d", 'g']:
            newupos = "ADV"
        elif node.xpos[0] == "n":
            if node.form.istitle():
                newupos = "PROPN"
            else:
                newupos = 'NOUN'
        elif node.xpos[0] == 'u':
            newupos = 'PUNCT'
        elif node.xpos[0] == 'c':
            if newupos in cord_conjs:
                newupos = "CCONJ"
            else:
                newupos[0] = 'SCONJ'
        elif node.xpos[0] in ['v', 't']:
            if node.deprel == "AuxV":
                newupos = "AUX"
            else:
                newupos = "VERB"

        if node.lemma in dets:
            newupos = 'DET'

        node.upos = newupos
