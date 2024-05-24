import numpy as np

def init_network():
  network = {}
  network['W1'] = np.array([[-1,-2,-3],[4,5,6]]) 
  network['b1'] = np.array([0,0,0]) 
  network['W2'] = np.array([[3,1],[5,5],[9,6]])
  network['b2'] = np.array([0,0])

  return network

def softmax(x):
  return np.exp(x)/np.sum(np.exp(x))

def sigmoid(x):
  return 1/(1+np.exp(-x))

def forward(network,x):
  W1,W2= network['W1'],network['W2']
  b1,b2=network['b1'],network['b2']
  h1=np.dot(x,W1)+b1
  z1=sigmoid(h1)
  h2=np.dot(z1,W2)+b2
  z2=sigmoid(h2)
  y=softmax(z2)
  return y

network=init_network()
x=np.array([np.log2,0])
y=forward(network,x)
print(y)