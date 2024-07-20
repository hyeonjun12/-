class mulLayer:
  def __init__(self):
    self.x=None
    self.y=None

  def forward(self, x, y):
    self.x=x
    self.y=y
    out=x*y

    return out

  def backward(self, dout):
    dx=dout*self.y
    dy=dout*self.x

    return dx, dy


class AddLayer:
  def __init__(self) -> None:
    pass

  def forward(self, x, y):
    self.x=x
    self.y=y
    out=x+y

    return out

  def backward(self, dout):
    dx=dout*1
    dy=dout*1

    return dx, dy

mul_apple_Layer=mulLayer()
mul_tax_Layer=mulLayer()


apple=100
num=2
tax=1.1

#순전파
apple_prise=mul_apple_Layer.forward(apple, num)
prise=mul_tax_Layer.forward(apple_prise, tax)
print(prise)

#역전파
dprise=1
dapple_prise, dtax=mul_tax_Layer.backward(dprise)
dapple,dapple_num=mul_apple_Layer.backward(dapple_prise)

print(dapple, dapple_num, dtax)