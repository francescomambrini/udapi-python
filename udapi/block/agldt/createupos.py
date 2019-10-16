from udapi.core.block import Block

prons = ['ἐγώ', 'σύ', 'ἡμεῖς', 'ὑμεῖς', 'σφεῖς', 'ἐμός', 'σός', 'ἡμέτερος',
            'ὑμέτερος', 'ὅς', 'νωΐτερος', 'σφέτερος', 'ἐμαυτοῦ', 'σαυτοῦ', 'ἑαυτοῦ',
            'ἀλλήλων', 'ἄλλος', 'ὅδε', 'αὐτός', 'οὗτος', 'ἐκεῖνος', 'τόσος', 'τοσόσδε',
            'τοσοῦτος', 'τοῖος', 'τοιόσδε', 'τοιοῦτος', 'τήλικος', 'τηλικόσδε',
            'τηλικοῦτος', 'τίς', 'πότερος', 'πόσος', 'ποῖος', 'πηλίκος', 'ὅς',
            'ὁποῖος', 'ὅσος', 'ὁπόσος', 'ὁπότερος', 'ἡλίκος', 'ὁπηλίκος', 'τις',
            'ὅστις', 'ἑκάτερος', 'ἕκαστος', 'ποσός', 'ποιός', 'οἷος']
parts = ['ἆρα', 'αὖ', 'γάρ', 'γε', 'γοῦν', 'δή', 'εἶτα', 'καίπερ',
             'καίτοι', 'μά', 'μέν', 'μέντοι', 'μήν', 'μῶν',
             'οὖν', 'ποθι', 'περ', 'ποτέ', 'πού', 'πω', 'τοίνυν', 'τοι', 'τοιγάρ',
             'ἀτάρ', 'ἄν', 'ἄν1', 'ἄρα', 'ἆρα', 'ἤτοι', 'ἦ']

cord_conjs = ['καί', 'δέ', "τε", "οὔτε", "μήτε", "μηδέ", "οὐδέ", "εἴτε"]

class CreateUpos(Block):

    def process_node(self, node):
        newupos = 'X'
        if node.upostag == "a":
            newupos = "ADJ"
        if node.upostag == 'p':
            newupos = "PRON"
        if node.upostag == "d":
            newupos = "ADV"
        if node.upostag == "n":
            if node.form.istitle():
                newupos = "PROPN"
            else:
                newupos = 'NOUN'
        if node.lemma in cord_conjs:
            newupos = "CCONJ"
        if node.upostag == 'c' and newupos != 'CCONJ':
            newupos = "SCONJ"
        if node.upostag in ['v', 't']:
            if node.deprel == "AuxV":
                newupos = "AUX"
            else:
                newupos = "VERB"

        node.upos = newupos
