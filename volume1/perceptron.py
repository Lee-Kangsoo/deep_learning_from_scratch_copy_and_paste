import numpy as np


def ANDBase(x1, x2):
    w1,w2 , theta = 0.5,0.5,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    

def ANDWithBias(x1 , x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0 :
        return 0
    elif tmp > 0:
        return 1


def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <=0:
        return 0
    elif tmp > 0:
        return 1

def OR(x1 , x2):
    x = np.array([x1, x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(x * w) + b
    if tmp <= 0 :
        return 0
    elif tmp > 0:
        return 1

# XOR couldn`t be made single perceptron
# Because of NOT separated by straight line( linear line)
# Must stack 2 stage at least.
def XOR(x1 , x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = ANDWithBias(s1,s2)
    return y

if __name__ == "__main__":
    print("AND base , w1 = 0.5 , w2= 0.5 , theta = 0.7")
    print("AND base  ", ANDBase(0,0))
    print("AND base  ", ANDBase(0,1))
    print("AND base  ", ANDBase(1,0))
    print("AND base  ", ANDBase(1,1))


    print("ANDWithBias , w1 = 0.5 , w2= 0.5 , theta = 0.7")
    print("ANDWithBias  ", ANDWithBias(0,0))
    print("ANDWithBias  ", ANDWithBias(0,1))
    print("ANDWithBias  ", ANDWithBias(1,0))
    print("ANDWithBias  ", ANDWithBias(1,1))

    print(" XOR , w1 = 0.5 , w2= 0.5 , theta = 0.7")
    print(" XOR  ",  XOR(0,0))
    print(" XOR  ",  XOR(0,1))
    print(" XOR  ",  XOR(1,0))
    print(" XOR  ",  XOR(1,1))