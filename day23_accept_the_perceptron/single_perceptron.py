#dont forget to explain it from very very basic!!!!!

import random
inp1=[1,0,1,0]
inp2=[1,1,0,0]
outp=[1,1,1,0] #bisa dari truth table dulu terus ganti class nya gitu deh wkkwkw bebas

w1=1.0
w2=1.0
b=1.0

best_param=[5,5,5]

def perceptron(in1, in2):
    return in1*w1 + in2*w2 + b

def activation_random():
    w1=random.random()
    w2=random.random()
    b=random.random()
    return w1,w2,b

def activation_little_bit_better(cur_loss,w1,w2,b):
    if cur_loss<0.0:
        w1=w1+random.random()
        w2=w2+random.random()
        b=b+random.random()
    elif cur_loss>0.0:
        w1=w1-random.random()
        w2=w2-random.random()
        b=b-random.random()
    return w1,w2,b

def activation_with_memory(cur_loss,w1,w2,b,best_loss):
    if(abs(cur_loss)>=abs(best_loss)):
        w1,w2,b=activation_little_bit_better(cur_loss,w1,w2,b)
    else:
        best_loss=cur_loss
        best_param[0]=w1
        best_param[1]=w2
        best_param[2]=b

    return w1,w2,b,best_loss

def activation_with_less_dukun(cur_loss,w1,w2,b,step):
    if cur_loss<0.0:
        w1=w1+step
        w2=w2+step
        b=b+step
    elif cur_loss>0.0:
        w1=w1-step
        w2=w2-step
        b=b-step
    return w1,w2,b

def less_dukun_memory(cur_loss,w1,w2,b,best_loss,step):
    if(abs(cur_loss)>=abs(best_loss)):
        w1,w2,b=activation_with_less_dukun(cur_loss,w1,w2,b,step)
    else:
        best_loss=cur_loss
        best_param[0]=w1
        best_param[1]=w2
        best_param[2]=b

    return w1,w2,b,best_loss

import math
def sigmoid(result):
    lala=1.0/1.0+math.exp(-1.0*result)
    return lala

def predict(a,s):
    return a*best_param[0] + s*best_param[1] + best_param[2]



epo=0
#best_loss=0.1
for epochs in range(20): #jumlah epoch
    print("epoch ",str(epo),"-=====================================-")
    epo=epo+1
    print("w1, w2, b: ",str(w1)," ",str(w2)," ",str(b)," ")
    acc_loss=0
    for x in range(len(inp1)):
        res=perceptron(inp1[x],inp2[x])
        target=outp[x]
        loss=(res-target)
        #acc_loss=acc_loss+abs(loss)
        acc_loss=acc_loss+loss
        print("batch: ",str(x))
        print("loss: ",str(loss))
        print()
    if epo==1 : best_loss=acc_loss/4
    print("epoch loss: ",str(abs(acc_loss/4)), " best loss: ",str((abs(best_loss)))) #ini pake mean absolute error (mae) kalo mau pake sum error biasa hapus aja abs sama bagi 4 nya
    #w1,w2,b=activation_random()
    #w1,w2,b=activation_little_bit_better(acc_loss,w1,w2,b)
    w1,w2,b,best_loss=activation_with_memory(acc_loss/4,w1,w2,b,best_loss)
    #w1,w2,b,best_loss=less_dukun_memory(acc_loss,w1,w2,b,best_loss,0.1)
    print()

print("predict a value!")
i=float(input("first input: "))
j=float(input("second input: "))
print("output")
print(predict(i,j))
#print("with sigmoid: ",str(sigmoid(predict(i,j))))
print("w1, w2, b: ",str(best_param[0])," ",str(best_param[1])," ",str(best_param[2])," ")