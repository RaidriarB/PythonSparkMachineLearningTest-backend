import csv
import os

walk_dir = "cicids2018"
lst =next(os.walk(walk_dir))[2]
kset = set({})

def read_csv(item):
	print("item:",item)
	reader = csv.reader(open(os.path.join(walk_dir,item)))
	for line in reader:
		kset.add(line[79])
		

for k in lst:
	if ".csv" in k:
		read_csv(k)

print(kset)