#!/usr/bin/env python

from subprocess import check_call
import os
import sys

if len(sys.argv) != 2:
	sys.exit('the first and only argument has to be the name of the .tex file without the .tex ending')

outDir = 'out'

# create out direcotry if necessary
if os.path.exists(outDir):
	if not os.path.isdir(outDir):
		os.makedirs(outDir)
	else:
		sys.exit('directory ' + outDir + ' already exists')
else:
	os.makedirs(outDir)

if not os.path.isdir(outDir):
	sys.exit(outDir + ' was not be created')

# build 3 times
# after 1. time: bib is not in pdf
# after 2. time: bib bookmark is not present
# after 3. time: everything is present
for x in range(0, 3):
	check_call(['pdflatex', '-output-directory', 'out', sys.argv[1] + '.tex'])
	check_call(['bibtex', 'out/' + sys.argv[1] + '.aux'])