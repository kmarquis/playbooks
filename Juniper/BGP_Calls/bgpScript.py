#!/usr/bin/python

import json 
import re

p = re.compile("\[")
q = re.compile("^$")

def printBGP(host):

        with open  ("build/{0}/{0}.json".format(host),"r") as v:

		w = v.readlines()

        jw = json.loads(w[0])
	
        bw =  jw['bgp-information'][0]['bgp-peer']

        keys = ["peer-address","peer-state","peer-as","peer-group"]

        for i in bw:

                if i['peer-state'][0]['data'] != "Established":

                        outputString = "Peer address = {0}; Peer state = {1}, Peer AS = {2}, Peer Group = {3}".format(   i['peer-address'][0]['data'],
                                                                                                i['peer-state'][0]['data'],
                                                                                                i['peer-as'][0]['data'],
                                                                                                i['peer-group'][0]['data'])

			print outputString

	with open(str("build/{0}/{0}.txt".format(host)),"w") as x:

		x.write(outputString)
	


with open("inventories/hosts","r") as f:

	j = f.readlines()


for i in j:

	if bool(p.match(i)) or bool(q.match(i)):

		pass

	else:

		printBGP(i.strip("\n"))

