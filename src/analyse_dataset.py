import csv
import os

walk_dir = "../dataset/full_dataset/cicids2018"
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
'''
获取每个标签的样本数量
'''
def get_label_num():
	dic = {}
	for k in lst:
		if ".csv" in k:
			print("processing : "+k)
			reader = csv.reader(open(os.path.join(walk_dir,k)))
			try:
				for line in reader:
					word = line[79]
					if word not in dic:
						dic[word] = 1
					else:
						dic[word] += 1
			except:
				print(k)
	print(dic)

get_label_num()