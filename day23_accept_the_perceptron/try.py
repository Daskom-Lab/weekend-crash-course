import random
inp1=[1,0,1,0]
inp2=[1,1,0,0]
outp=[1,1,1,0]

w1=1.0
w2=1.0
b=1.0

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
    if(abs(cur_loss)>abs(best_loss)):
        w1,w2,b=activation_little_bit_better(cur_loss,w1,w2,b)
    else:
        best_loss=cur_loss

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
    if(abs(cur_loss)>abs(best_loss)):
        w1,w2,b=activation_with_less_dukun(cur_loss,w1,w2,b,step)
    else:
        best_loss=cur_loss

    return w1,w2,b,best_loss


acc_loss=0
epo=0
best_loss=0.1
for epochs in range(20):
    print("epoch ",str(epo),"-=====================================-")
    epo=epo+1
    print("w1, w2, b: ",str(w1)," ",str(w2)," ",str(b)," ")
    for x in range(len(inp1)):
        res=perceptron(inp1[x],inp2[x])
        target=outp[x]
        loss=(res-target)
        #acc_loss=acc_loss+abs(loss)
        acc_loss=acc_loss+loss
        print("batch: ",str(x))
        print("loss: ",str(loss))
        print()
    print("epoch loss: ",str(acc_loss), " best loss: ",str(best_loss))
    #w1,w2,b=activation_random()
    w1,w2,b=activation_little_bit_better(acc_loss,w1,w2,b)
    #w1,w2,b,best_loss=less_dukun_memory(acc_loss,w1,w2,b,best_loss,0.1)
    acc_loss=0
    print()
print("predict a value!")
i=float(input("first input: "))
j=float(input("second input: "))
print("output")
print(perceptron(i,j))
    
    # if loss_new<loss:
    #     loss=loss_new
