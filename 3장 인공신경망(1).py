import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_function(x): #항등함수
    return x

def init_network():
    network = {}
    network['W1'] = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) #첫번째 층에서 두번째 층으로 갈 때 더하는 가중치
    network['b1'] = np.array([0.1,0.2,0.3]) #첫번째 층에서 두번째 층으로 갈때 더하는 편향
    network['W2'] = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])
    network['W3'] = np.array([[0.1,0.3],[0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])

    return network


def forward(network, x): #순전파, 전기신호가 앞으로 가게 도와주는 함수
    W1, W2, W3 = network['W1'], network['W2'], network['W3'] #각 딕셔러리에 대한 벨류값을 저장
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1)+b1 #np.dot은 두 행렬끼리의 곱을 도와줌
    z1 = sigmoid(a1) #활성화함수를 거침
    a2 = np.dot(z1,W2)+b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3)+b3
    y = identity_function(a3)

    return y

network = init_network()
x = np.array([2,5])
y = forward(network, x)
print(y)
