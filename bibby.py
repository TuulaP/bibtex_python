
import bibtexparser
import csv

# file to be processed, should be as input arg
inputfile = "sample.bib"
inputfilebase = inputfile.split(".")[0]


# Read the BibTeX file and parse it
with open(inputfile, 'r') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)



# Open the CSV file for writing
with open(inputfilebase + "_" + 'bibtex.csv', 'w', newline='') as csv_file:
    # Create a CSV writer
    writer = csv.writer(csv_file)

    # Write the column headers
    # writer.writerow(['Title', 'Author', 'Year', 'Journal', 'Volume', 'Number', 'Pages'])

    # Iterate over the BibTeX entries and write them to the CSV file
    for entry in bib_database.entries:
        title = entry.get('title', '')
        #author = entry.get('author', '')
        year = entry.get('year', '')
        journal = entry.get('journal', '')
        url = entry.get('url','')
        #volume = entry.get('volume', '')
        #number = entry.get('number', '')
        #pages = entry.get('pages', '')

        nbn = "-"
        # grab issn or nbn
        if "digi.kansalliskirjasto.fi" in url:
            nbn = url.split('/')[-1]

        #writer.writerow([title, author, year, journal, volume, number, pages])
        writer.writerow([title, year, url, nbn])

