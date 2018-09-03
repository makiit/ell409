import numpy as np 
import matplotlib.pyplot as plt
from numpy import genfromtxt

def dataProcessing(d,k):
	N = np.size(d,axis=0)
	dtrain = d[0:2*N/3,:]
	dtest = d[2*N/3:,:]
	xtrain=dtrain[:,1:]
	ytrain=dtrain[:,0]
	xtest = dtest[:,1:]
	ytest = dtest[:,0]
	x = []
	for i in range(0,k):
		t = dtrain[dtrain[:,0]==i,:]
		x.append(t[:,1:])

	return [xtrain,ytrain,xtest,ytest,x]


def MLEGaussian(x):
	mean = np.mean(x,axis=0)
	var = np.var(x,axis=0)
	return [mean,var]

def gaussian(x,mu,var):
	d = np.size(x,axis=1)
	n = np.size(x,axis=0)
	sig = np.eye((d))
	sigma = sig*var
	sigmainv=sig/var
	det = np.product(np.sum(sigma,axis=0))
	z = np.dot(x-mu,sigmainv)
	z = np.dot(z,(x-mu).transpose())
	z = z * np.eye(n)
	z = np.sum(z,axis=0)
	z = np.exp(-1*z)
	z = z/(((2*3.14)**(d/2))*det)
	return z

def classify(x,xtest,ytest,N):
	theta = []
	cc = []
	prior = []
	posterior = []
	for i in range(0,k):
		t = MLEGaussian(x[i])
		ccond = gaussian(xtest,t[0],t[1])
		p = np.size(x[i],axis=0)*1.0/N
		pos = ccond*p
		theta.append(t)
		cc.append(ccond)
		prior.append(p)
		posterior.append(pos)

	bayes = np.argmax(posterior,axis=0)
	err = bayes-ytest
	err = np.where(err==0)
	acc = np.size(err)*1.0/np.size(bayes)*100
	print "Accuracy on test set is ",acc

def DataVisualization(x0,x1,x2):
	plt.figure(0)
	plt.scatter(x0[:,0],x0[:,1],marker='o')
	plt.scatter(x1[:,0],x1[:,1],marker='^')
	plt.scatter(x2[:,0],x2[:,1],marker='X')
	plt.figure(1)
	plt.hist(x2[:,0],bins=100)
	plt.figure(2)
	plt.hist(x2[:,1],bins=100)
	plt.show()




d = genfromtxt('medicalData.txt')
k = 3 # Number of classes
dp = dataProcessing(d,k)
xtrain = dp[0]
ytrain = dp[1]
xtest = dp[2]
ytest = dp[3]
x = dp[4]
N = np.size(xtrain,axis=0)




classify(x,xtest,ytest,N)
