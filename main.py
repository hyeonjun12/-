import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2]) #array는 리스트의 안의 객체들의 연산을 도와줌
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b #sum운 리스트 안의 인덱스 끼리의 합
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2): #NAND는 AND게이트에서 가중치와 임계값의 등호만 바꾸면 됨
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = np.sum(w*x) + b
  if tmp <= 0:
      return 0
  else:
      return 1

def OR(x1, x2): #OR게이트는 AND게이트보다 허들(임계값)을 낮춤
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum(w*x) + b
  if tmp <= 0:
      return 0
  else:
      return 1

def XOR(x1, x2): #XOR게이트는 단층 퍼셉트론으로는 표현 불가 
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y= AND(s1, s2)
    return y

if __name__=='__main__': #그냥 하나의 파일 안에서는 있으나 마나이지만 다른 파일에서 불러올 때 이 이하의 코드는 무시됨
  for xs in [(0,0), (1,0),(0,1),(1,1)]:
    y=XOR(xs[0], xs[1])
    print(str(xs)+" -->  "+str(y)) #y의 값이 1이라는 정수형 이기때문에 바꿔줌
