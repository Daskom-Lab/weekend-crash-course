inp1=[0,1,0,1]
inp2=[0,0,1,1]
outp=[0,0,0,1] #AND problem

w1=1.0
w2=1.0
b=1.0
best_param=[1,2,3]

def perceptron(in1,in2):
    return (in1*w1) + (in2*w2) + b

import random

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



epo=0
for epochs in range(20): #epoch starts here
    epo=epo+1 
    print("epoch: ",epo)
    print("w1, w2, b: ",str(w1)," ",str(w2)," ",str(b)," ")
    acc_loss=0 #epoch loss
    for x in range(len(inp1)): #batch starts here
        res=perceptron(inp1[x],inp2[x])
        target=outp[x]
        loss=res-target #batch loss
        acc_loss=acc_loss+loss
        print("batch: ",x)
        print("batch loss: ",str(loss))
        print()
    if epo==1 : best_loss=acc_loss/4
    #print("epoch loss: ",str(abs(acc_loss/4)), " best loss: ",str((abs(best_loss)))) #ini pake mean absolute error (mae) kalo mau pake sum error biasa hapus aja abs sama bagi 4 nya
    print("epoch loss: ",str(abs(acc_loss/4)))
    w1,w2,b,best_loss=activation_with_memory(acc_loss/4,w1,w2,b,best_loss)
    print()
    print()
print("train result: best loss = ",best_loss)
print("with parameters: ")
print("w1, w2, b: ",str(best_param[0])," ",str(best_param[1])," ",str(best_param[2])," ")