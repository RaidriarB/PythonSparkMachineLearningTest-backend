"""
Decision Tree to Json
"""
from __future__ import print_function

from pyspark import SparkContext
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils

import sys
import json
import os
os.environ['PYSPARK_PYTHON']='/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python'

TEST_MODEL_PATH = "../new_model"
MAX_DEPTH = 7
USE_TREE = 3


# Parser
def parse(lines,depth):
	if depth > MAX_DEPTH:
		return []
	block = []
	while lines :
		
		if lines[0].startswith('If') or lines[0].startswith('Tree'):
			bl = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
			block.append({'name':bl, 'children':parse(lines,depth+1)})
			
			if lines[0].startswith('Else'):
				be = ' '.join(lines.pop(0).split()[1:]).replace('(', '').replace(')', '')
				block.append({'name':be, 'children':parse(lines,depth+1)})
		elif not lines[0].startswith(('If','Else','Tree')):
			block2 = lines.pop(0)
			block.append({'name':block2})
		else:
			break	
	return block

# Convert Tree to JSON
def tree2json(tree):

	trees = tree.split("Tree")

	trees.pop(0)
	trees.pop(0)

	outstr = ""
	tree = trees[USE_TREE]
	data = []
	lines = tree.splitlines()
	head = lines[0]
	lines.pop(0)

	print("Tree "+head+"is converting...")

	for line in tree.splitlines(): 
		if line.strip():
			line = line.strip()
			data.append(line)
		else : continue
		if not line : break
	res = []
	res.append({'name':'Root'+head, 'children':parse(data[1:],0)})
	outstr += json.dumps(res[0])
	with open('../vis/data/structure.json', 'w') as outfile:
		outfile.write(outstr)

	print ('Conversion Success !')


if __name__ == "__main__":

	# debug
	# treeStr = open("../vis/data/modelString",'r').read()
	# python3 vis.py ../model 7 3

	try:
		MAX_DEPTH = int(sys.argv[1])
	except: print("default depth is 7.")

	try:
		USE_TREE = int(sys.argv[2])
	except: print("default tree to convert is num 3")

	sc = SparkContext(appName="RandomForest2Json")
	trees = RandomForestModel.load(sc,TEST_MODEL_PATH)
	treeStr = trees.toDebugString()
	with open("../vis/data/modelString",'w') as f:
		f.write(treeStr)

	tree2json(treeStr)