#!bin/python

from dublincore import dublinCoreMetadata
import csv
from sys import argv
from xml.dom.minidom import Document

DC_NS = 'http://purl.org/dc/elements/1.1/'

class DublinCore(dublinCoreMetadata):
	""" Add toprettyxml() func so we can treat this like an xml.dom.minidom.Document """
	def toprettyxml():
		self.makeXML(DC_NS)

class TabFile(object):
	""" A dialect for the csv.DictReader constructor """
	delimiter = '\t'

def usage():
	""" Print a nice usage message """
	print "Usage: " + os.path.basename(__file__) + " <filename>.tsv"

def parse(fn):
	""" Parse a TSV file """
	try:
		fp = open(fn)
		fields = fp.readline().rstrip('\n').split('\t')
		tsv = csv.DictReader(fp, fieldnames=fields dialect=TabFile)
		while row = tsv.next():
			makedc(row)
			makexml(row)
	except IOError as (errno, strerror):
		print "Error ({0}): {1}".format(errno, strerror)
		raise SystemExit
	fp.close()

def makedc(row):
	""" Generate a Dublin Core XML file from a TSV """
	metadata = DublinCore()
	metadata.Contributor = row.get('dc:contributor', '')
	metadata.Coverage = row.get('dc:coverage', '')
	metadata.Creator = row.get('dc:creator', '')
	metadata.Date = row.get('dc:date', '')
	metadata.Description = row.get('dc:description', '')
	metadata.Format = row.get('dc:format', '')
	metadata.Identifier = row.get('dc:identifier', '')
	metadata.Language = row.get('dc:language', '')
	metadata.Publisher = row.get('dc:publisher', '')
	metadata.Relation = row.get('dc:relation', '')
	metadata.Rights = row.get('dc:rights', '')
	metadata.Source = row.get('dc:source', '')
	metadata.Subject = row.get('dc:subject', '')
	metadata.Title = row.get('dc:title', '')
	return metadata

def makexml(row):
	""" Generate a custom XML file from a TSV """
	doc = Document()
	return doc

def writefile(name, obj):
	pass

def chkarg(arg):
	""" Was a TSV file specified? """
	return False if arg[0] == '' else True

if __name__ == "__main__":
	if chkarg(argv[0]):
		parse(argv[0])
	else:
		usage()

