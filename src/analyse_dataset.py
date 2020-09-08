import csv
import os

walk_dir = "../dataset/full_datasets/cicids2018"
lst =next(os.walk(walk_dir))[2]

def read_csv(item):
	kset = set({})
	print("item:",item)
	reader = csv.reader(open(os.path.join(walk_dir,item)))
	for line in reader:
		kset.add(line[79])
	return kset
'''
统计数据集中所有标签字段
'''
def get_all_labels():
	for k in lst:
		if ".csv" in k:
			read_csv(k)

	print(kset)
'''
统计数据集中所有字段名称
'''
def get_all_headers():
	for k in lst:
		if ".csv" in k:
			reader = csv.reader(open(os.path.join(walk_dir,k)))
			for line in reader:
				return line
			
with open("headers.txt",'w') as f:
	l = get_all_headers()
	index = 0
	for item in l:
		f.write(str(index)+" "+item+"\n")
		index += 1