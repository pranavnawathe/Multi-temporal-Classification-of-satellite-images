import numpy as np
import pandas as pd
import pickle
from MLCFast import *

dataset1 = pd.read_csv('../Data/Training/ValidationDataImage1.csv')
dataset2 = pd.read_csv('../Data/Training/ValidationDataImage2.csv')
dataset3 = pd.read_csv('../Data/Training/ValidationDataImage3.csv')
dataset4 = pd.read_csv('../Data/Training/ValidationDataImage4.csv')

cols = dataset1.columns

dataset1.drop(cols[[0,1,2]], inplace=True, axis=1)
dataset2.drop(cols[[0,1,2]], inplace=True, axis=1)
dataset3.drop(cols[[0,1,2]], inplace=True, axis=1)
dataset4.drop(cols[[0,1,2]], inplace=True, axis=1)

#fselection = {1: [0,1,2,6,7], 2: [0,1,2,3,4,5,6,7], 3: [0,1,2,4,5,7], 4: [4,5,6,7]}
fselection = {1: [0,1,4,6,7], 2: [0,1,2,5,7], 3: [0,6], 4: [0,2,3,4,5,6,7]}

#cor = ['Blue', 'Red', 'SWNIR_2']

cols = dataset1.iloc[:,1:].columns

X1 = dataset1[cols[fselection[1]]]
X2 = dataset2[cols[fselection[2]]]
X3 = dataset3[cols[fselection[3]]]
X4 = dataset4[cols[fselection[4]]]

Y1 = dataset1['Class']
Y2 = dataset2['Class']
Y3 = dataset3['Class']
Y4 = dataset4['Class']

# dataset2.drop(cor, inplace=True, axis=1)
# dataset3.drop(cor, inplace=True, axis=1)
# dataset4.drop(cor, inplace=True, axis=1)

def calculateWeight (dataset, probs):
  weight = 1
  for i in range(len(dataset)):
    index = int(dataset.iloc[i])
    weight = weight*probs.iloc[i,(index-1)]
  return (weight)

def calculateLogWeight(dataset, probs):
  weight = 0
  for i in range(len(dataset)):
    index = int(dataset.iloc[i])
    weight = weight + np.log(1+probs.iloc[i,(index-1)])
    #print probs.iloc[i,(index-1)]
  return (weight)

def saveModel(model,dataset, filename):
  predProbs = model.predict(dataset.iloc[:,1:], type = 'raw')
  w = calculateLogWeight(dataset['Class'], predProbs)
  print(w)
  model.bmaweight = w
  with open(filename,'wb') as f:
    pickle.dump(model, f)

def saveModel2(model,X, Y, filename):
  predProbs = model.predict(X, type = 'raw')
  w = calculateLogWeight(Y, predProbs)
  print(w)
  model.bmaweight = w
  with open(filename,'wb') as f:
    pickle.dump(model, f)

def main1():
  with open('../TrainedModels/MLC/MLC_Image1.pkl','r') as f:
    model1 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image2.pkl','r') as f:
    model2 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image3.pkl','r') as f:
    model3 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image4.pkl','r') as f:
    model4 = pickle.load(f)

  saveModel(model1, dataset1,'../TrainedModels/BMA/image1.BMAmodel.LogWeighted.pkl')
  saveModel(model2, dataset2,'../TrainedModels/BMA/image2.BMAmodel.LogWeighted.pkl')
  saveModel(model3, dataset3,'../TrainedModels/BMA/image3.BMAmodel.LogWeighted.pkl')
  saveModel(model4, dataset4,'../TrainedModels/BMA/image4.BMAmodel.LogWeighted.pkl')

def main2():
  with open('../TrainedModels/MLC/MLC_Image1_FS.pkl','r') as f:
    model1 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image2_FS.pkl','r') as f:
    model2 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image3_FS.pkl','r') as f:
    model3 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image4_FS.pkl','r') as f:
    model4 = pickle.load(f)

  saveModel2(model1, X1, Y1,'../TrainedModels/BMA/image1.BMAmodelFS.LogWeighted.pkl')
  saveModel2(model2, X2, Y2,'../TrainedModels/BMA/image2.BMAmodelFS.LogWeighted.pkl')
  saveModel2(model3, X3, Y3,'../TrainedModels/BMA/image3.BMAmodelFS.LogWeighted.pkl')
  saveModel2(model4, X4, Y4,'../TrainedModels/BMA/image4.BMAmodelFS.LogWeighted.pkl')

def main3():
  with open('../TrainedModels/MLC/MLC_Image_PCA1.pkl','r') as f:
    model1 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image_PCA2.pkl','r') as f:
    model2 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image_PCA3.pkl','r') as f:
    model3 = pickle.load(f)
  with open('../TrainedModels/MLC/MLC_Image_PCA4.pkl','r') as f:
    model4 = pickle.load(f)

  d1 = pd.read_csv('../Data/Training/pcaImage1.csv')
  d2 = pd.read_csv('../Data/Training/pcaImage2.csv')
  d3 = pd.read_csv('../Data/Training/pcaImage3.csv')
  d4 = pd.read_csv('../Data/Training/pcaImage4.csv')

  saveModel(model1, d1,'../TrainedModels/BMA/pcaImage1.BMAmodel.LogWeighted.pkl')
  saveModel(model2, d2,'../TrainedModels/BMA/pcaImage2.BMAmodel.LogWeighted.pkl')
  saveModel(model3, d3,'../TrainedModels/BMA/pcaImage3.BMAmodel.LogWeighted.pkl')
  saveModel(model4, d4,'../TrainedModels/BMA/pcaImage4.BMAmodel.LogWeighted.pkl')

if __name__ == '__main__':
  main2()
