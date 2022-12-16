
# Extract an .bib file of bibtex entries and generate a csv of them

import sys
sys.path.append('C:\\dev\\biblib')


#import biblib.bib
#import argparse

from biblib.bib import Parser as BibParser
import requests

kirjabib = """
@book{
Solr-fikka.3776075,
title = {Ahjo : Työväen-opiston toimittama sosialistinen tieteellis-kaunokirjallinen kuukausijulkaisu},
address = {Duluth (Minn.)},
publisher = {Työväen-opisto},
year = {1916},
note = {Englanninkielinen julkaisijanimi: Work People's College, Duluth, Minn.},
url = {https://digi.kansalliskirjasto.fi/aikakausi/titles/fk34057}
}

@book{
Solr-fikka.3719615,
title = {Aika : the only Finnish newsspaper [!] in Canada},
address = {Nanaimo (B.C.)},
publisher = {[kustantaja tuntematon]},
year = {1901},
url = {https://digi.kansalliskirjasto.fi/aikakausi/titles/0845-7875}
}
"""


parser = BibParser()
parser.parse(kirjabib)
entries = parser.get_entries()

dix = dict(next(iter(entries.values())))

print (dix)

