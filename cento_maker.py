### Author: @drkndl
### Note: Some parts of this code were taken from https://github.com/aparrish/gutenberg-poetry-corpus/blob/master/quick-experiments.ipynb

import gzip, json
from gutenbergdammit.ziputils import loadmetadata
import random
import re


# List to store all the lines of poetry in the corpus
all_lines = []
for line in gzip.open("gutenberg-poetry-v001.ndjson.gz"):
    all_lines.append(json.loads(line.strip()))

# Load metadata of the Gutenberg literary corpus
metadata = loadmetadata("gutenberg-dammit-files-v002.zip")


def random_poem(numlines):
	"""
	Creates a random poem with 'numlines' number of lines from the corpus
	"""

	dics = random.sample(all_lines, numlines)
	lines = [l['s'] for l in dics]
	gids = [int(g['gid']) for g in dics]
	print(gids)
	return lines, gids


def retrieve_metadata(gids):
	"""
	Retrieves the title and author of each line of a generated poem using the 'gid'
	"""

	line_data = []
	for gid in gids:
		title = metadata[gid]['Title'][0]
		author = metadata[gid]['Author'][0]
		line_data.append((gid, title, author))

	return line_data


def find_themed_lines(theme):
	"""
	Finds all lines in poem that contain the 'theme' word and returns a list of these lines
	"""
	
	search_term = r'\b'+theme+r'\b'
	theme_lines = [line['s'] for line in all_lines if re.search(search_term, line['s'], re.I)]	
	return theme_lines


def print_poem(a_poem):
	"""
	Prints the poem line-by-line given a poem i.e. a list of lines
	"""

	for line in a_poem:
		print(line)

def pretty_print(theme_lines, theme):

	longest = max([len(x) for x in theme_lines])      # find the length of the longest line
	center = longest - len(theme)                     # and use it to create a "center" offset that will work for all lines
	search_term = r'\b'+theme+r'\b'

	sorted_theme_lines = sorted(
	    [line for line in theme_lines if re.search(search_term, line)],          # only lines with word following
	    key=lambda line: line[re.search(search_term, line).end():])              # sort on the substring following the match

	for line in sorted_theme_lines: 
	    offset = center - re.search(search_term, line, re.I).start()
	    print((" "*offset)+line)                                                 # left-pad the string with spaces to align on "flower"


# moon_lines = find_themed_lines('moon')
# pretty_print(moon_lines, 'moon')

num_lines = 4 			                     # Required number of lines in the cento
poem, ids = random_poem(num_lines)           # Retrieve poem
poem_data = retrieve_metadata(ids)
print_poem(poem)
print(poem_data)
title = metadata[2701]['Title']
print(title)