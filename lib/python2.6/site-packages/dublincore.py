#!/usr/bin/python

############################################################################
#    Copyright (C) 2006 by Jonathan E. Magen                               #
#    Student, The Evergreen State College                                  #
#    <yonkeltron@gmail.com> http://www.bluefacemonkey.com                  #
#                                                                          #
#    This program is free software; you can redistribute it and or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################

"""
This module is designed to enable the creation of metadata compliant with
the guidlines of the Dublin Core Metadata Initiative (DCMI). Learn more
at http://www.dublincore.org to get started.

This is written in pure python and should not require any additional
modules, libraries or other dependencies in order to function. It should
offer a drop-in solution for any application that needs to be able to write
Dublin Core metadata in either RDF or XML format. Either of these can then be 
linked to from a webpage or otherwise embedded in a document or database entry.
"""

import xml.sax.saxutils

class dublinCoreMetadata:
	"""
	This class represents the Dublin Core metadata itself. This follows 
	the "Dublin Core Metadata Element Set, Version 1.1" available online 
	at http://www.dublincore.org/documents/dces/ . It covers all 15 of the
	core metadata elements with the addition of one extra item (the about
	item which may be required when generating RDF) as class attributes.
	
	These are to be set before calling class methods to transform the
	data into a desired output format. There is no need to escape any 
	data as the transformation process does this to all non URL strings 
	automatically.
	"""
	def __init__(self):
		self.Title = ""
		self.Creator = ""
		#if the subject is a list, each term should be separated by semicolon
		self.Subject = ""
		self.Description = ""
		self.Publisher = ""
		self.Contributor = ""
		self.Date = ""
		self.Type = ""
		self.Format = ""
		self.Identifier = ""
		self.Source = ""
		self.Language = ""
		self.Relation = ""
		self.Coverage = ""
		self.Rights = ""
		self.about = ""
	def makeRDF(self):
		"""
		This method transforms the class attribute data into standards
		compliant RDF according to the guidlines laid out in "Expressing Simple 
		Dublin Core in RDF/XML" available online at
		http://www.dublincore.org/documents/2002/07/31/dcmes-xml/
		
		This method is passed no arguments and returns a string. The output can
		be directed to a file or standard output. This RDF data should be 
		suitable for marking most documents including webpages.
		"""
		#set XML declaration
		rdfOut = '<?xml version="1.0"?>\n'
		#Reference the XML DTD
		rdfOut += '<!DOCTYPE rdf:RDF PUBLIC "-//DUBLIN CORE//DCMES DTD 2002/07/31//EN" "http://dublincore.org/documents/2002/07/31/dcmes-xml/dcmes-xml-dtd.dtd">\n'
		#Declare the use of RDF
		rdfOut += '\t<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
		
		#Describe the resources
		#if the about element is set (reccomended) include it properly
		if self.about:
			if self.about.startswith('http://'):
				rdfOut += '\t<rdf:Description rdf:about="%s">\n' % self.about
			else:
				rdfOut += '\t<rdf:Description>\n'
		
		#if the Title element is set, make the dc:title tag
		if self.Title:
			rdfOut += '\t\t<dc:title>%s</dc:title>\n' % xml.sax.saxutils.escape(self.Title)
		
		#if the creator element is set, make the dc:title tag
		if self.Creator:
			rdfOut += '\t\t<dc:creator>%s</dc:creator>\n' % xml.sax.saxutils.escape(self.Creator)
		
		#if the subject element is set, make the dc:subject tag
		if self.Subject:
			rdfOut += '\t\t<dc:subject>%s</dc:subject>\n' % xml.sax.saxutils.escape(self.Subject)
		
		#if the description element is set, make the dc:description tag
		if self.Description:
			rdfOut += '\t\t<dc:description>%s</dc:description>\n' % xml.sax.saxutils.escape(self.Description)
			
		#if the publisher element is set, make the dc:publisher tag
		if self.Publisher:
			rdfOut += '\t\t<dc:publisher>%s</dc:publisher>\n' % xml.sax.saxutils.escape(self.Publisher)
			
		#if the contributor element is set, make the dc:contributor tag
		if self.Contributor:
			rdfOut += '\t\t<dc:contributor>%s</dc:contributor>\n' % xml.sax.saxutils.escape(self.Contributor)
			
		#if the date element is set, make the dc:date tag
		if self.Date:
			rdfOut += '\t\t<dc:date>%s</dc:date>\n' % xml.sax.saxutils.escape(self.Date)
			 
		#if the type element is set, make the dc:type tag
		if self.Type:
			rdfOut += '\t\t<dc:type>%s</dc:type>\n' % xml.sax.saxutils.escape(self.Type)
			
		#if the format element is set, make the dc:format tag
		if self.Format:
			rdfOut += '\t\t<dc:format>%s</dc:format>\n' % xml.sax.saxutils.escape(self.Format)
		
		#if the identifier element is set, make the dc:identifier tag
		if self.Identifier:
			rdfOut += '\t\t<dc:identifier>%s</dc:identifier>\n' % xml.sax.saxutils.escape(self.Identifier)
			
		#if the source element is set, deal with it properly
		if self.Source:
			if self.Source.startswith("http://"):
				rdfOut += '\t\t<dc:source rdf:resource="%s"/>\n' % self.Source
			else:
				rdfOut += '\t\t<dc:source>%s</dc:source>\n' % xml.sax.saxutils.escape(self.Source)
		
		#if the language element is set, make the dc:language tag
		if self.Language:
			rdfOut += '\t\t<dc:language>%s</dc:language>\n' % xml.sax.saxutils.escape(self.Language)
			
		#if the relation element is set, make the dc:relation tag
		if self.Relation:
			rdfOut += '\t\t<dc:relation>%s</dc:relation>\n' % xml.sax.saxutils.escape(self.Relation)
			
		#if the coverage element is set, make the dc:coverage tag
		if self.Coverage:
			rdfOut += '\t\t<dc:coverage>%s</dc:coverage>\n' % xml.sax.saxutils.escape(self.Coverage)
			
		#if the rights element is set, make the dc:rights tag
		if self.Rights:
			rdfOut += '\t\t<dc:rights>%s</dc:rights>\n' % xml.sax.saxutils.escape(self.Rights)
		
		
		#close the rdf description tag
		rdfOut += '\t</rdf:Description>\n'
		#close the rdf tag
		rdfOut += '</rdf:RDF>\n'
		
		return rdfOut
		
	def makeXML(self, schemaLocation, encapsulatingTag='metadata'):
		"""
		This method transforms the class attribute data into standards
		compliant XML according to the guidlines laid out in 
		"Guidelines for implementing Dublin Core in XML" available online 
		at http://www.dublincore.org/documents/2003/04/02/dc-xml-guidelines/
		
		This method takes one mandatory argument, one optional argument and
		returns a string. The mandatory argument is the location of the XML
		schema which should be a fully qualified URL. The option arguments
		is the root tag with which to enclose and encapsulate all of the
		DC elements. The default is "metadata" but it can be overridden if
		needed.
		
		The output can be directed to a file or standard output. This RDF 
		data should be suitable for marking most documents including webpages.
		"""
		#set XML declaration
		xmlOut = '<?xml version="1.0"?>\n'
		
		#open encapsulating element tag and deal with namespace and schema declarations
		xmlOut += '''\n<%s
    xmlns="http://example.org/myapp/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="%s"
    xmlns:dc="http://purl.org/dc/elements/1.1/">\n\n''' % (encapsulatingTag, schemaLocation)
		
		#if the Title element is set, make the dc:title tag
		if self.Title:
			xmlOut += '\t<dc:title>%s</dc:title>\n' % xml.sax.saxutils.escape(self.Title)
		
		#if the creator element is set, make the dc:title tag
		if self.Creator:
			xmlOut += '\t<dc:creator>%s</dc:creator>\n' % xml.sax.saxutils.escape(self.Creator)
		
		#if the subject element is set, make the dc:subject tag
		if self.Subject:
			xmlOut += '\t<dc:subject>%s</dc:subject>\n' % xml.sax.saxutils.escape(self.Subject)
		
		#if the description element is set, make the dc:description tag
		if self.Description:
			xmlOut += '\t<dc:description>%s</dc:description>\n' % xml.sax.saxutils.escape(self.Description)
			
		#if the publisher element is set, make the dc:publisher tag
		if self.Publisher:
			xmlOut += '\t<dc:publisher>%s</dc:publisher>\n' % xml.sax.saxutils.escape(self.Publisher)
			
		#if the contributor element is set, make the dc:contributor tag
		if self.Contributor:
			xmlOut += '\t<dc:contributor>%s</dc:contributor>\n' % xml.sax.saxutils.escape(self.Contributor)
			
		#if the date element is set, make the dc:date tag
		if self.Date:
			xmlOut += '\t<dc:date>%s</dc:date>\n' % xml.sax.saxutils.escape(self.Date)
			 
		#if the type element is set, make the dc:type tag
		if self.Type:
			xmlOut += '\t<dc:type>%s</dc:type>\n' % xml.sax.saxutils.escape(self.Type)
			
		#if the format element is set, make the dc:format tag
		if self.Format:
			xmlOut += '\t<dc:format>%s</dc:format>\n' % xml.sax.saxutils.escape(self.Format)
		
		#if the identifier element is set, make the dc:identifier tag
		if self.Identifier:
			xmlOut += '\t<dc:identifier>%s</dc:identifier>\n' % xml.sax.saxutils.escape(self.Identifier)
			
		#if the source element is set, deal with it properly
		if self.Source:
			xmlOut += '\t<dc:source>%s</dc:source>\n' % xml.sax.saxutils.escape(self.Source)
		
		#if the language element is set, make the dc:language tag
		if self.Language:
			xmlOut += '\t<dc:language>%s</dc:language>\n' % xml.sax.saxutils.escape(self.Language)
			
		#if the relation element is set, make the dc:relation tag
		if self.Relation:
			xmlOut += '\t<dc:relation>%s</dc:relation>\n' % xml.sax.saxutils.escape(self.Relation)
			
		#if the coverage element is set, make the dc:coverage tag
		if self.Coverage:
			xmlOut += '\t<dc:coverage>%s</dc:coverage>\n' % xml.sax.saxutils.escape(self.Coverage)
			
		#if the rights element is set, make the dc:rights tag
		if self.Rights:
			xmlOut += '\t<dc:rights>%s</dc:rights>\n' % xml.sax.saxutils.escape(self.Rights)
			
		#close encapsulating element tag
		xmlOut += '</metadata>\n'
		
		return xmlOut
		
		