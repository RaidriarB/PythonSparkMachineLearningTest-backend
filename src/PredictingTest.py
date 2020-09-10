from __future__ import print_function

from pyspark import SparkContext
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils
from pyspark.mllib.evaluation import BinaryClassificationMetrics

import os
import time
'''
Arklight Mac python env
This var shouldd be changed to conform to your python runtime
'''
os.environ['PYSPARK_PYTHON']='/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python'

'''
global vars

'''
INPUT_DATA_PATH = "../dataset/useful_dataset/test2"
TEST_MODEL_PATH = "../model"
TEST_PREDICT_PATH = "../predict"
NUM_OF_FUTURE = 80
NUM_OF_CLASSES = 14
NUM_OF_TREES = 3

def isunfit(lp):

	a,b = lp[0],lp[1]
	if a - 0 >= 0.1:
		a = 1
	if b - 0 >= 0.1:
		b = 1

	if a - b <= 0.1:
		return False
	else:
		return True

def tobin(num):
	if num - 0 >= 0.1:
		num = 1.0
	else:
		num = 0.0
	return num

def predict():

	testData = MLUtils.loadLibSVMFile(sc,INPUT_DATA_PATH)
	print("[INFO] load complete.")

	model = RandomForestModel.load(sc,TEST_MODEL_PATH)

	# Evaluate model on test instances and compute test error
	predictions = model.predict(testData.map(lambda x: x.features))

	lst = predictions.collect()
	with open(TEST_PREDICT_PATH+"/"+time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+".txt",'w') as f:
		for k in lst:
			f.write(str(k)+"\n")

	labelsAndPredictions = testData.map(lambda lp: tobin(lp.label)).zip(predictions.map(lambda lp: tobin(lp)))

	#print(labelsAndPredictions.collect())

	metrics = BinaryClassificationMetrics(labelsAndPredictions)

	# Area under precision-recall curve
	print("Area under PR = %s" % metrics.areaUnderPR)

	# Area under ROC curve
	print("Area under ROC = %s" % metrics.areaUnderROC)
	#print(labelsAndPredictions.collect())

	testErr = labelsAndPredictions.filter(lambda lp: lp[0] != lp[1]).count() / float(testData.count())
	print('[INFO] Test Error = ' + str(testErr))


if __name__ == "__main__":
	sc = SparkContext(appName="PyRandomForestPridictingTest")
	predict()