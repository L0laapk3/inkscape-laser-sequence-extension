#!/usr/bin/env python

# We will use the inkex module with the predefined Effect base class.
import inkex

import measure
import re
import cubicsuperpath
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
            paths = oldpathstring.replace("Z", "z").split("z ")
            if len(paths[-1].strip()) == 0:
                paths.pop()
            x = y = 0
            for i in range(len(paths)):
                result = re.search(r' ?(m|M) ?(-?[0-9.]+)(?:,| )(-?[0-9.]+) (.).*', paths[i])
                if result is None:
                    continue
                groups = result.groups()
                if groups[0] == "M":
                    x = y = 0
                x += float(groups[1])
                y += float(groups[2])
                paths[i] = re.sub(r' ?m ?(-?[0-9.]+),(-?[0-9.]+) ', "M " + str(x) + "," + str(y) + (" l" if (groups[3] in "0123456789.-") else " "), paths[i])
            
            paths = sorted(paths, key=getArea)

                
            newpathstring = "z ".join(paths) + "z "
            el.set('d', newpathstring)
        




# Create effect instance and apply it.
effect = LaserSort()
effect.affect()
