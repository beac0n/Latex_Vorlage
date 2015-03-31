#!/usr/bin/env python

from subprocess import check_call
import os
import sys

if len(sys.argv) != 3:
	sys.exit('the first argument has to be the name of the .tex file. The second argument has to be the name of the output directory')

texEnding = '.tex'
fileNameNoTex = os.path.splitext(sys.argv[1])[0]
outDir = sys.argv[2]

# check if tex file exists
if not os.path.exists(fileNameNoTex + texEnding):
	sys.exit(fileNameNoTex + texEnding + ' does not exist')

# create out direcotry if necessary
if os.path.exists(outDir) and not os.path.isdir(outDir):
		sys.exit(outDir + ' is a file, not a folder. Remove the file ' + outDir + ' or use a different output directory name')
else:
	os.makedirs(outDir)

if not os.path.isdir(outDir): # should never happen
	sys.exit('FATAL: ' + outDir + ' was not be created')

# build 3 times
# after 1. time: bib is not in pdf
# after 2. time: bib bookmark is not present
# after 3. time: everything is present
for x in range(0, 3):
	check_call(['pdflatex', '-output-directory', outDir, fileNameNoTex + texEnding])
	check_call(['bibtex', outDir + '/' + fileNameNoTex + '.aux'])