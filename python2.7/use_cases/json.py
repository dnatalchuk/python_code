#!/usr/bin/python

import json

from pprint import pprint

# open()

f = open("api_easy.txt")
val = json.loads(f.read())

#print val
#pprint(val)

# print val.keys()
# print val.values()[0].keys()[0]

# convert to json

dic = {
	"type":"fantasy",
	"title":"hobbit",
	"year":[12,13,14]
}

print json.dumps(dic)

pprint(json.dumps(dic))

# XML

#from xml.dom import minidom


