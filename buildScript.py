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
if os.path.exists(outDir):
	if not os.path.isdir(outDir):
		sys.exit(outDir + ' is a file, not a folder. Remove the file ' + outDir + ' or use a different output directory name')
else:
	os.makedirs(outDir)

if not os.path.isdir(outDir): # should never happen
	sys.exit('FATAL: ' + outDir + ' was not be created')

# as descriped in http://stackoverflow.com/questions/2461905/compiling-latex-bib-source
check_call(['pdflatex', '-output-directory', outDir, fileNameNoTex + texEnding])
check_call(['bibtex', outDir + '/' + fileNameNoTex + '.aux'])
check_call(['pdflatex', '-output-directory', outDir, fileNameNoTex + texEnding])
check_call(['pdflatex', '-output-directory', outDir, fileNameNoTex + texEnding])