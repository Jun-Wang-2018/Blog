Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
Acurve = 0; Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible

#Individual Transaction/Personal Information
privKey = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E #replace with any private key
def inverse_mod(a,n=Pcurve): #Extended Euclidean Algorithm/'division' in elliptic curves. (modinv)
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high//low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n

def ECadd(a,b): # Not true addition, invented for EC. Could have been called anything.
    LamAdd = ((b[1]-a[1]) * inverse_mod(b[0]-a[0],Pcurve)) % Pcurve
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def ECdouble(a): # This is called point doubling, also invented for EC.
    Lam = ((3*a[0]*a[0]+Acurve) * inverse_mod((2*a[1]),Pcurve)) % Pcurve
    x = (Lam*Lam-2*a[0]) % Pcurve
    y = (Lam*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def EccMultiply(GenPoint,ScalarHex): #Double & add. Not true multiplication
    if ScalarHex == 0 or ScalarHex >= N: raise Exception("Invalid Scalar/Private Key")
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)): # This is invented EC multiplication.
        Q=ECdouble(Q); # print "DUB", Q[0]; print
        if ScalarBin[i] == "1":
            Q=ECadd(Q,GenPoint); # print "ADD", Q[0]; print
    return (Q)

import numpy as np
import matplotlib.pyplot as plt
a=1
b=1
plt.figure(figsize=(18,4))
plt.subplot(131)
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0],colors='black')
plt.annotate('${y^2={x^3+x+1}}$', [-2,4],fontsize=16)
plt.grid()
plt.subplot(132)
initialpoint= (3,10)
Pcurve = 23
#px=[]
#py=[]
for i in range(1,20):
    P = EccMultiply(initialpoint,i)
    plt.scatter(P[0],P[1],color="b")
    #plt.annotate(i,P)
    #px.append(P[0])
    #py.append(P[1])
plt.grid()
#plt.plot(px,py)
plt.annotate('${y^2=({x^3+x+1})mod 23}$', [5,20],fontsize=16,color="b")
plt.subplot(133)
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0],colors='black')
initialpoint= (3,10)
Pcurve = 23
for i in range(1,20):
    P = EccMultiply(initialpoint,i)
    plt.scatter(P[0],P[1],color="b")
plt.grid()
plt.annotate('${y^2=({x^3+x+1})mod 23}$', [5,20],fontsize=16,color="b")
plt.annotate('${y^2={x^3+x+1}}$', [-2,4],fontsize=16)
plt.show()
