#!bin/python

# TSV to Dublin Core/McMaster Repository conversion tool
# Matt McCollow <mccollo@mcmaster.ca>, 2011
# Nick Ruest <ruestn@mcmaster.ca>, 2011

from DublinCore import DublinCore
import csv
from sys import argv
from xml.dom.minidom import Document
from os.path import basename

DC_NS = 'http://purl.org/dc/elements/1.1/'
XSI_NS = 'http://www.w3.org/2001/XMLSchema-instance'
MACREPO_NS = 'http://repository.mcmaster.ca/schema/macrepo/elements/1.0/'

class TabFile(object):
	""" A dialect for the csv.DictReader constructor """
	delimiter = '\t'

def parse(fn):
	""" Parse a TSV file """
	try:
		fp = open(fn)
		fields = fp.readline().rstrip('\n').split('\t')
		tsv = csv.DictReader(fp, fieldnames=fields, dialect=TabFile)
		for row in tsv:
			dc = makedc(row)
			writefile(row['dc:identifier'], dc)
			xml = makexml(row)
			writefile(row['dc:identifier'], xml)
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
	metadata.Relation = row.get('dc:relation', '').split('|')
	metadata.Rights = row.get('dc:rights', '')
	metadata.Source = row.get('dc:source', '')
	metadata.Subject = row.get('dc:subject', '')
	metadata.Title = row.get('dc:title', '')
	return metadata

def makexml(row):
	""" Generate an XML file conforming to the macrepo schema from a TSV """
	doc = Document()
	root = doc.createElement('metadata')
	root.setAttribute('xmlns:xsi', XSI_NS)
	root.setAttribute('xmlns:macrepo', MACREPO_NS)
	doc.appendChild(root)
	oldnid = doc.createElement('macrepo:oldNid')
	oldnid.appendChild(doc.createTextNode(row.get('macrepo:oldNid', '')))
	root.appendChild(oldnid)
	notes = doc.createElement('macrepo:notes')
	notes.appendChild(doc.createTextNode(row.get('macrepo:notes', '')))
	root.appendChild(notes)
	scale = doc.createElement('macrepo:scale')
	scale.appendChild(doc.createTextNode(row.get('macrepo:scale', '')))
	root.appendChild(scale)
	return doc

def writefile(name, obj):
	""" Writes Dublin Core or Macrepo XML object to a file """
	if isinstance(obj, DublinCore):
		fp = open(name + '-DC.xml', 'w')
		fp.write(obj.makeXML(DC_NS))
	elif isinstance(obj, Document):
		fp = open(name + '-macrepo.xml', 'w')
		fp.write(obj.toprettyxml())
	fp.close()

def chkarg(arg):
	""" Was a TSV file specified? """
	return False if len(arg) < 2 else True

def usage():
	""" Print a nice usage message """
	print "Usage: bin/python " + basename(__file__) + " <filename>.tsv"

if __name__ == "__main__":
	if chkarg(argv):
		parse(argv[1])
	else:
		usage()

