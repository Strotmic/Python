#first neural network with keras make predictions
#Source https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense, Activation
from numpy.core.records import format_parser
import numpy as np

# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=750, batch_size=100, verbose=0)
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# make class predictions with the model
'''Vanaf hier heb ik dit stukje aangepast zodat de output mooier zou zijn'''
predictions = model.predict(X)
sl = predictions[1]
for i in range(5):
	print("-----------------------------------------------------------------------------------")
	sl = predictions[i]
	print(sl)
	x = np.round(sl, decimals = 0)
	print(str(X[i].tolist())+ '=> ' + str(x)+ ' (expected ' + str(y[i]) + ' )' )
	print("-----------------------------------------------------------------------------------")




