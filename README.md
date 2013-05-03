# RPG Assist

These tools are scripts I've developed over the years to help me both play and run tabletop role-playing games. The scripts each have their own built-in help text (use the --help option from the command line), and below is an overview of what each one does.

## Dice Roller (roll.py)

*Requirements:* Python 2.7

*Type:* CLI

This script is an extremely powerful dice roller, able to handle arbitrary numbers and types of dice, roll-again rules, failure rules (subtract 1's, for example), counting dice over a threshold, etc. It can also apply formulas to each die roll.

## NPC Exporter (npc_export.py)

*Requirements:* Python 2.7, spreadsheet software

*Type:* CLI

Creates pretty html from a spreadsheet of NPC statistics. The spreadsheet should look like the example sheet (NPC database.ods) and must be saved in the CSV format.

## Pledge Summary Creator (pledgesum.py)

*Requirements:* Python 2.7, spreadsheet software

*Type:* CLI

Creates very basic html for a table of pledge stats, for use with White Wolf's *Changelinge: the Lost* game system. The spreadsheet should look like the example sheet (pledge summary - template.ods) and must be saved in the CSV format.
