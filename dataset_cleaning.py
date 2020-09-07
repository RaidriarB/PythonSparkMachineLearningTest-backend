import csv
import os

# usage: python3 dataset_cleaning.py src_dir target_dir

walk_dir = sys.argv[1]
new_dir = sys.argv[2]

lst = next(os.walk(walk_dir))[2]
for k in lst:
	if ".csv" in k:
		old_name = k
		new_name = k.split(".")[0]+".libsvm"
		cmd = "python3 csv2libsvm.py "+"./"+walk_dir+"/"+old_name+" ./"+new_dir+"/"+new_name+" 79"

		print(cmd)
		print("[INFO] cleaning "+old_name+" ...")
		os.system(cmd)
		print("[INFO] success.")