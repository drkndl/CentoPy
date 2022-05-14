import csv 
import pandas as pd
import random

# List to store all the poems and related metadata (titles, poets, tags)
rows = []

with open("PoetryFoundationData.csv", 'r') as file:

    csvreader = csv.reader(file)		# Reading the file
    header = next(csvreader) 			# Saving the column names to header

    for row in csvreader:
        rows.append(row) 				# Saving the poems and related metadata


# Splitting the poems into multiple lines by iterating through each poem
for entry in rows:

	entry[2].replace("\n", "\n\n") 				
	lines = entry[2].split("\n\n")
	lines = [y for y in lines if y != '']		# Removing blank lines from the poem
	entry.insert(2, lines) 						# Inserting the line-by-line split poem into the original list
	del entry[3]  								# Removing old unsplit poem
	entry.insert(3, len(lines))  				# Inserting a new column indicating the number of lines in the poem


header.insert(3, 'Poem Lines') 			# Inserting title for the new column of poem lines created above
print(header)

# Saving list as a pandas dataframe
df = pd.DataFrame(rows)
df.columns = header

# Removing poems with no lines (possibly a glitch on the Poetry Foundation website)
df.drop(df.index[df['Poem Lines'] == 0], inplace=True)
lines = df.groupby('Poem Lines')
# print(lines.first())

num_lines = 4 			# Required number of lines in the cento


def cento(data):
	"""
	Creates a new line in the cento by randomly picking a poem out of the dataframe, and randomly picking a line from the poem

	Parameters:
	data:  		Dataframe of poems that consists of the following columns- index, Title, Poem, Poem Lines, Poet, Tags

	Returns a random line from a random poem
	"""

	random_poem = random.randint(0, len(data)-1)
	random_line = random.randint(0, data['Poem Lines'][random_poem]-1)
	
	return data['Poem'][random_poem][random_line]

# Creating the cento
for n in range(num_lines):
	line = cento(df)
	print(line)