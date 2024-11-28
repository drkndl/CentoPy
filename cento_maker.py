### Author: @drkndl
### Note: Some parts of this code were taken from https://github.com/aparrish/gutenberg-poetry-corpus/blob/master/quick-experiments.ipynb

import gzip, json
import random
import re


# List to store all the lines of poetry in the corpus
all_lines = []
for line in gzip.open("gutenberg-poetry-v001.ndjson.gz"):
    all_lines.append(json.loads(line.strip()))


def random_poem(numlines):
	"""
	Creates a random poem with 'numlines' number of lines from the corpus
	"""
	
	dics = random.sample(all_lines, numlines)
	lines = [l['s'] for l in dics]
	for line in lines:
		print(line)


def find_theme(theme):
	"""
	Finds all lines in poem that contain the 'theme' word and returns a list of these lines
	"""
	
	search_term = r'\b'+theme+r'\b'
	theme_lines = [line['s'] for line in all_lines if re.search(search_term, line['s'], re.I)]	
	return theme_lines


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


# moon_lines = find_theme('moon')
# pretty_print(moon_lines, 'moon')

num_lines = 8 			# Required number of lines in the cento
random_poem(num_lines)
