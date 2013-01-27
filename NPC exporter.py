#!/usr/bin/python

import csv
import argparse

parser = argparse.ArgumentParser(description="Generate an HTML character summary page. Great for NPC lists.")
parser.add_argument("fname", metavar='csv', type=str, help="Path to the CSV file to read. The file MUST start with a row of column names which match those in the example. Their order, however, is irrelevant. See example CSV for format.")
parser.add_argument("-o, --outfile", dest="ofile", default='-', type=str, help="File where the generated HTML will be saved. Passing '-' will print the output to stdout (default behavior).")
parser.add_argument("-i, --ignore", dest="ignore", type=str, help="Species name which should not be printed. If your game has mostly Changeling NPCs, for example, you can use '-i Changeling' to avoid printing \"Changeling\" for every single NPC. Other species are printed as normal.")
args = parser.parse_args()

try:
    npcReader = csv.DictReader(open(args.fname, 'rb'))
except IOError:
    print "Could not open %s for reading." % args.fname
    exit(-1)

labels = {
    'changeling': {'court': 'Court', 'seeming': 'Seeming', 'kith': 'Kith'},
    'werewolf': {'court': 'Lodge', 'seeming': 'Auspice', 'kith': 'Tribe'},
    'vampire': {'court': 'Court', 'seeming': 'Clan', 'kith': 'Bloodline'},
#    'geist': {'court': 'Concilium', 'seeming': 'Path', 'kith': 'Order'},
    'mage': {'court': 'Concilium', 'seeming': 'Path', 'kith': 'Order'}
}

html = ''
firstletter = ' '
for row in npcReader:
    newfirst = row['Last Name'][0]
    if firstletter != newfirst:
        html += "<h2>%s</h2>" %newfirst.upper()
        firstletter = newfirst
        
    charname = row['Last Name'] if row['First Name'] == '' else row['First Name']+' '+row['Last Name']
    html += "<h3 style=\"margin-bottom: 0;\">%s</h3>" %charname
    
    if row['Deceased'] == "TRUE":
        html += "<div><em>Deceased</em></div>"

    template = row['Species'].lower() #store species type (i.e. "supernatural template")
    
    if template != str(args.ignore).lower():
        html += "<div><em>%s</em></div>" %row['Species']
    
    if template in labels:
        if row['Court'] != '':
            html += "<div><em>%s:</em> %s</div>" %(labels[template]['court'], row['Court'])

        if row['Seeming'] != '':
            html += "<div><em>%s &amp; %s:</em> %s</div>" %(labels[template]['seeming'], labels[template]['kith'], row['Seeming']+' '+row['Kith'])

    if row['Appearance'] != '':
        html += "<div><em>Description:</em> %s</div>" %row['Appearance']

    html += "<div><em>Notes:</em> %s</div>" %row['Notes']

if args.ofile == '-':
    #default
    print html
else:
    try:
        of = open(args.ofile, 'w')
    except IOError:
        print "Could not open %s for writing." % args.ofile
        exit(-1)
    
    of.write(html)
    of.close()
