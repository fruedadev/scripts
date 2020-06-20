#!/usr/bin/env python3

from pathlib import Path
import trello, yaml, argparse, os, sys, datetime

# Some constants
LABELS = {
    "ES": "Archivos",
    "EN": "Files",
    "FR": "Archives" 
}

# Get the options
parser = argparse.ArgumentParser(description='Manage Josue''s Trello cards')

parser.add_argument('-d', '--directory', default='.', help='Directory to check for files (default is the current directory)')
parser.add_argument('-l', '--language', default='es', help='Language to be used for the card (default = "es")')
parser.add_argument('NAME', help='The card name')

args = parser.parse_args()
directory = args.directory
language = args.language.upper()
name = args.NAME

# Get the card description
if not os.path.exists(directory):
    sys.exit('No se encontró el directorio {}'.format(directory))

files = '\n'.join(['- ' + f for f in os.listdir(directory)])
description = '{}:\n{}'.format(LABELS[language], files)

# Create the card
configFile = '{}/.config/trllmgr/josue.yml'.format(str(Path.home()))
config = yaml.safe_load(open(configFile))

listId = config['board']['lists'][language]
trll = trello.Trello(config['security']['key'], config['security']['token'])

response = trll.addCard(listId, name, description).json()
print(response)
