#!/bin/python

import csv
import argparse

parser = argparse.ArgumentParser(description="Generate an HTML pledge summary in table form from a csv spreadsheet.")
parser.add_argument("fname", metavar='csv', type=str, help="Path to the CSV file to read. The file MUST start with a row of column names which match those in the example. Their order, however, is irrelevant. See example CSV for format.")
parser.add_argument("-o, --outfile", dest="ofile", default='-', type=str, help="File where the generated HTML will be saved. Passing '-' will print the output to stdout (default behavior).")
args = parser.parse_args()

try:
    csvReader = csv.DictReader(open(args.fname, 'rb'))
except IOError:
    print "Could not open %s for reading." % args.fname
    exit(-1)

cols = ['Party', 'Type', 'Duration', 'Task', 'Boon', 'Sanction']

output = '''<table border="1" bordercolor="#888" cellspacing="0" style="border-collapse:collapse;border-color:rgb(136,136,136);border-width:1px">
<thead>
<tr>'''

for col in cols:
    output += '<th>' + col + '</th>'

output += '</tr></thead><tbody>'

for row in csvReader:
    output += '<tr>'
    for col in cols:
        output += '<td>' + row[col] + '</td>'
    output += '</tr>'

output += '</tbody></table>'

if args.ofile == '-':
    #default
    print output
else:
    try:
        of = open(args.ofile, 'w')
    except IOError:
        print "Could not open %s for writing." % args.ofile
        exit(-1)
    
    of.write(output)
    of.close()
