#########################################################################
# File Name: dict2.py
# Author: WangWeilong
# Company: Baidu
#########################################################################
#!/home/work/safe_psqa/python/bin/python
# coding=utf-8

import json

path = "this"

with open(path, "rb") as fp:
	for line in fp:
		content = line.split("\t")[1]
		s = json.loads(content)
		print len(s.keys())
		for key in s.keys():
			#if s.get(key) is None:
#			if s.get(key) != "":
#				print "xxx"
			if type(s.get(key)) is list:
				for inner in s.get(key):
					#print "%s\t%s\t%s" % (type(inner), inner, key)
					for inside in inner:
						if inner.get(inside) == "":
							print "aaaaaaaaaa %s" % inside
			#print "%s\t%s\t%s" % (type(s.get(key)),key, s.get(key))
#			print type(key)
