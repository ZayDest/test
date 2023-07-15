import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from FS.pso import jfs   # change this to switch algorithm 
import matplotlib.pyplot as plt




#Load Data
X = pd.read_csv("data.csv")
Y = pd.read_csv("labels.csv")

s=0
rem = []
for x in X.columns:
    flag=1
    for i in X[x]:
        try:
            if float(i)>0:
                flag=0

                break
        except:
            pass
            #print("ERR",x)

    if flag==1:
        rem.append(x)
        s=s+1

X.drop(rem,axis=1,inplace=True)

Y = Y['Class']

print("ZZZ")

# load data
# data  = pd.read_csv('ionosphere.csv')
# data  = data.values
# feat  = np.asarray(data[:, 0:-1])
# label = np.asarray(data[:, -1])

feat =np.asarray(X)
label = np.asarray(Y)

print(label)
# split data into train & validation (70 -- 30)
xtrain, xtest, ytrain, ytest = train_test_split(feat, label, test_size=0.3, stratify=label)

print(xtrain.shape,ytrain.shape)
fold = {'xt':xtrain, 'yt':ytrain, 'xv':xtest, 'yv':ytest}

# parameter
k    = 5     # k-value in KNN
N    = 10    # number of particles
T    = 100   # maximum number of iterations
opts = {'k':k, 'fold':fold, 'N':N, 'T':T}

# perform feature selection
fmdl = jfs(feat, label, opts)
sf   = fmdl['sf']

# # model with selected features
# num_train = np.size(xtrain, 0)
# num_valid = np.size(xtest, 0)
# x_train   = xtrain[:, sf]
# y_train   = ytrain.reshape(num_train)  # Solve bug
# x_valid   = xtest[:, sf]
# y_valid   = ytest.reshape(num_valid)  # Solve bug

# x_train   = xtrain
# y_train   = ytrain
# x_valid   = xtest
# y_valid   = ytest


# mdl       = KNeighborsClassifier(n_neighbors = k) 
# mdl.fit(x_train, y_train)

# # accuracy
# y_pred    = mdl.predict(x_valid)
# Acc       = np.sum(y_valid == y_pred)  / num_valid
# print("Accuracy:", 100 * Acc)

# # number of selected features
# num_feat = fmdl['nf']
# print("Feature Size:", num_feat)

# # plot convergence
# curve   = fmdl['c']
# curve   = curve.reshape(np.size(curve,1))
# x       = np.arange(0, opts['T'], 1.0) + 1.0

# fig, ax = plt.subplots()
# ax.plot(x, curve, 'o-')
# ax.set_xlabel('Number of Iterations')
# ax.set_ylabel('Fitness')
# ax.set_title('PSO')
# ax.grid()
# plt.show()

