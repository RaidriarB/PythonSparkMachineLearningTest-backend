from __future__ import print_function

from pyspark import SparkContext
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils

import os
'''
Arklight Mac python env
This var shouldd be changed to conform to your python runtime
'''
os.environ['PYSPARK_PYTHON']='/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python'

'''
global vars

'''
TEST_DATA_PATH = "./dataset/test"
TEST_MODEL_PATH = "./model"
NUM_OF_FUTURE = 80
NUM_OF_CLASSES = 14

def train():
	data = MLUtils.loadLibSVMFile(sc,TEST_DATA_PATH)
	print("[INFO] load complete.")
	# 划分训练集
	(trainingData, testData) = data.randomSplit([0.8, 0.3])

	# Train a RandomForest model.
	#  Empty categoricalFeaturesInfo indicates all features are continuous.
	#  Note: Use larger numTrees in practice.
	#  Setting featureSubsetStrategy="auto" lets the algorithm choose.
	model = RandomForest.trainClassifier(trainingData, numClasses= NUM_OF_CLASSES, categoricalFeaturesInfo={},
										 numTrees=3, featureSubsetStrategy="auto",
										 impurity='gini', maxDepth=4, maxBins=32)

	# Evaluate model on test instances and compute test error
	predictions = model.predict(testData.map(lambda x: x.features))
	labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
	testErr = labelsAndPredictions.filter(
		lambda lp: lp[0] != lp[1]).count() / float(testData.count())
	print('[INFO] Test Error = ' + str(testErr))
	print('[INFO] Learned classification forest model:')
	print(model.toDebugString())

	# Save and load model
	model.save(sc,TEST_MODEL_PATH)
	sameModel = RandomForestModel.load(sc,TEST_MODEL_PATH)

if __name__ == "__main__":
	sc = SparkContext(appName="PyRandomForestTest")
	train()