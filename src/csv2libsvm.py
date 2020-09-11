"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[2]) if there are no labels in your file.
"""

# label = 80
# usage: python3 csv2libsvm.py xxx.csv 79
import sys
import csv
from collections import defaultdict

def parse_label(label):
	labels = {'Benign':0,
	'Brute Force -Web':1,
	'Bot':2,
	'FTP-BruteForce':3,
	'DoS attacks-SlowHTTPTest':4,
	'DDOS attack-HOIC':5,
	'DDOS attack-LOIC-UDP':6,
	'Infilteration':7,
	'DoS attacks-Slowloris':8,
	'DoS attacks-Hulk':9,
	'DoS attacks-GoldenEye':10,
	'SSH-Bruteforce':11,
	'Brute Force -XSS':12,
	'SQL Injection':13
	}

	return str(labels[label])


def construct_line( label, line ):
	new_line = []

	try:
		if float( label ) - 0 <= 0.1:
			label = "0"
		else:
			#label = "1"
			pass
	except ValueError:
		pass

	new_line.append( label )

	for i, item in enumerate( line ):

		# convert TimeString to TimeStamp
		try:
			if item == '' or float( item ) - 0 <= 0.00001:
				continue
		except ValueError:
			import time
			timeArray = time.strptime(item, "%d/%m/%Y %H:%M:%S")
			timeStamp = int(time.mktime(timeArray))
			item = timeStamp

		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

def conv_csv():
	i = open( input_file, 'r' )
	o = open( output_file, 'w' )
	reader = csv.reader( i )
	for line in reader:
		# exclude header
		try:
			assert float(line[0]) is not None
		except:
			continue
		# parse label
		if label_index == -1:
			label = '1'
		else:
			label = line.pop( label_index )
			label = parse_label( label)
		# parse line
		new_line = construct_line( label, line )
		o.write( new_line )
	print("[INFO] convert finished.")

if __name__ == "__main__":

	input_file = sys.argv[1]
	output_file = sys.argv[2]

	try:
		label_index = int( sys.argv[3] )
	except IndexError:
		label_index = 0
	
	conv_csv()
