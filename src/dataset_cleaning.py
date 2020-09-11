import csv
import os
import sys
# usage: python3 dataset_cleaning.py src_dir target_dir
# python3 dataset_cleaning.py ../dataset/full_dataset/cicids2018 ../dataset/full_dataset/clean
walk_dir = sys.argv[1]
new_dir = sys.argv[2]

lst = next(os.walk(walk_dir))[2]
for k in lst:
	if ".csv" in k:
		old_name = k
		new_name = k+".libsvm"
		cmd = "python3 csv2libsvm.py "+"./"+walk_dir+"/"+old_name+" ./"+new_dir+"/"+new_name+" 79"

		print(cmd)
		print("[INFO] cleaning "+old_name+" ...")
		os.system(cmd)
		print("[INFO] success.")