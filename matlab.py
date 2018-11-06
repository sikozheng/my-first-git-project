import matplotlib.pyplot as plt
from random import choice
# imputvalue=[1,2,3,4,5]
# squ=[1,4,9,16,25]
# plt.plot(imputvalue,squ,linewidth=5)
# plt.title("Square numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Squares of value",fontsize=14)
# plt.tick_params(axis='both',labelsize=14)
# plt.show()


# xvalue=list(range(1001))
# yvalue=[x**2 for x in xvalue]
# plt.scatter(xvalue,yvalue,c=yvalue,cmap=plt.cm.Reds,s=40)
# plt.savefig('squreplot.png',bbox_inches='tight')

class randomwalk():
    def __init__(self,numpoints=5000):
        self.numpoints=numpoints
        self.xvalue=[0]
        self.yvalue=[0]
