#!bin/pyton

import dublincore as dc
import csv
from sys import argv
from xml.dom.minidom import Document

class TabFile(object):
	delimiter = '\t'

def usage():
	""" Print a nice usage message """
	print "Usage: " + os.path.basename(__file__) + " <filename>.tsv"

def parse(fn):
	""" Parse a TSV file """
	try:
		fp = open(fn)
		tsv = csv.reader(fp, TabFile)
	except IOError as (errno, strerror):
		print "Error ({0}): {1}".format(errno, strerror)
		raise SystemExit
	return tsv

def makedc(tsv):
	""" Generate a Dublin Core XML file from a TSV """
	metadata = dc.dublinCoreMetadata()
	return metadata

def makexml(tsv):
	""" Generate a custom XML file from a TSV """
	doc = Document()
	return doc

def chkarg(arg):
	""" Was a TSV file specified? """
	return False if arg[0] == '' else True

if __name__ == "__main__":
	if chkarg(argv[0]):
		tsv = parse(argv[0])
		makedc(tsv)
		makexml(tsv)
	else:
		usage()

