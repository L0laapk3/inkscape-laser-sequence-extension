#!/usr/bin/env python

# We will use the inkex module with the predefined Effect base class.
import inkex

import measure
import re
import cubicsuperpath
from simplepath import parsePath
# The simplestyle module provides functions for style parsing.
from simplestyle import *





def getArea(path):
	return abs(measure.csparea(cubicsuperpath.parsePath(path + "z")))


class LaserSort(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)




		
	def effect(self):
		elements = self.document.xpath('//svg:path',namespaces=inkex.NSS)
		for el in elements:

			oldpathstring = el.attrib['d']

			nodes = parsePath(oldpathstring)

			currentSection = []
			sections = [currentSection]
			for node in nodes:
				command = node.pop(0)
				currentSection.append(command + ' ' + ' '.join(map(lambda c: ','.join(map(str, c)), node)))
				if command.lower() == 'z':
					currentSection = []
					sections.append(currentSection)
			
			sections = map(lambda n: ' '.join(n), filter(lambda n: len(n) > 0, sections))

			if (sections[-1][-2].lower() != 'z'):
				nonClosedSection = ' ' + sections.pop()
			else:
				nonClosedSection = ''

			
			sections = sorted(sections, key=getArea)

				
			newpathstring = "z ".join(sections) + nonClosedSection
			el.set('d', newpathstring)
		




# Create effect instance and apply it.
effect = LaserSort()
effect.affect()
