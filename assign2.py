import csv
import random
import math
import matplotlib

import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

with open('C:/Users/Rani Kim/Desktop/irisdata/dataset.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     spamreader = list(spamreader)
       
Theta_1=random.random()
print("Theta_1: %s" % (Theta_1))
Theta_2=random.random()
print("Theta_2: %s" % (Theta_2))
Theta_3=random.random()
print("Theta_3: %s" % (Theta_3))
Theta_4=random.random()
print("Theta_4: %s" % (Theta_4))
Theta_5=random.random()
print("Theta_5: %s" % (Theta_5))
Theta_6=random.random()
print("Theta_6: %s" % (Theta_6))
Theta_7=random.random()
print("Theta_7: %s" % (Theta_7))
Theta_8=random.random()
print("Theta_8: %s" % (Theta_8))
Bias=random.random()
print("Bias : %s" % Bias)
Bias_2=random.random()
print("Bias_2: %s" % Bias_2)

learningrate=0.1
learningrate2=0.8

class target:
    def __init__(self, Theta_1, Theta_2,Theta_3,Theta_4,spamreader,Bias):
      self.Theta_1 = Theta_1
      self.Theta_2 = Theta_2
      self.Theta_3 = Theta_3
      self.Theta_4 = Theta_4
      self.spamreader = spamreader
target = []
i=0
for i in range(149):
 target.append(i)
 target[i]=float(spamreader[i][0])*Theta_1+float(spamreader[i][1])*Theta_2+float(spamreader[i][2])*Theta_3+float(spamreader[i][3])*Theta_4+Bias
 print("target1: %s" % (target[i]))
 i = i+1

class target2:
    def __init__(self, Theta_5, Theta_6,Theta_7,Theta_8,spamreader,Bias_2):
      self.Theta_5 = Theta_5
      self.Theta_6 = Theta_6
      self.Theta_7 = Theta_7
      self.Theta_8 = Theta_8
      self.spamreader = spamreader
target2 = []
i=0
for i in range(149):
 target2.append(i)
 target2[i]=float(spamreader[i][0])*Theta_5+float(spamreader[i][1])*Theta_6+float(spamreader[i][2])*Theta_7+float(spamreader[i][3])*Theta_8+Bias_2
 print("target2: %s" % (target2[i]))
 i = i+1

class sigmoid:
    def __init__(self, target):
      self.target = target
sigmoid = []
i=0
for i in range(149):
 sigmoid.append(i)
 sigmoid[i]=1/(1+math.exp(-target[i]))
 print("sigmoid: %s" % (sigmoid[i]))
 i = i+1

class sigmoid_2:
    def __init__(self, target):
      self.target2 = target2
sigmoid2 = []
i=0
for i in range(149):
 sigmoid2.append(i)
 sigmoid2[i]=1/(1+math.exp(-target2[i]))
 print("sigmoid2: %s" % (sigmoid2[i]))
 i = i+1

class prediction:
    def __init__(self, sigmoid):
      self.sigmoid = sigmoid
prediction = []
i=0
for i in range(149):
 prediction.append(i)
 if(sigmoid[i]<float(0.5)):
    prediction[i]=0
    print("prediction: %s" % (prediction[i]))
 else:
    prediction[i]=1
    print("prediction: %s" % (prediction[i]))    
 i = i+1

class prediction2:
    def __init__(self, sigmoid):
      self.sigmoid2 = sigmoid2
prediction2 = []
i=0
for i in range(149):
 prediction2.append(i)
 if(sigmoid2[i]<float(0.5)):
    prediction2[i]=0
    print("prediction2: %s" % (prediction2[i]))
 else:
    prediction2[i]=1
    print("prediction2: %s" % (prediction2[i]))    
 i = i+1

class error:
    def __init__(self, sigmoid, spamreader):
      self.sigmoid = sigmoid
      self.spamreader = spamreader
error = []
i=0
for i in range(149):
 error.append(i)
 error[i]=(sigmoid[i]-float(spamreader[i][5]))*(sigmoid[i]-float(spamreader[i][5]))
 print("error: %s" % (error[i]))
 i = i+1

class Error_2:
    def __init__(self, sigmoid, spamreader):
      self.sigmoid2 = sigmoid2
      self.spamreader = spamreader
Error_2 = []
i=0
for i in range(149):
 Error_2.append(i)
 Error_2[i]=(sigmoid2[i]-float(spamreader[i][6]))*(sigmoid2[i]-float(spamreader[i][6]))
 print("Error_2: %s" % (Error_2[i]))
 i = i+1

class d_Theta_1:
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
d_Theta1 = []
i=0
for i in range(149):
 d_Theta1.append(i)
 d_Theta1[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][0])
 print("d_Theta_1: %s" % (d_Theta1[i]))
 i=i+1

class d_Theta_2:
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
d_Theta2 = []
i=0
for i in range(149):
 d_Theta2.append(i)
 d_Theta2[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][1])
 print("d_Theta_2: %s" % (d_Theta2[i]))
 i=i+1

class d_Theta_3:
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
d_Theta3 = []
i=0
for i in range(149):
 d_Theta3.append(i)
 d_Theta3[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][2])
 print("d_Theta_3: %s" % (d_Theta3[i]))
 i=i+1

class d_Theta_4:
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
d_Theta4 = []
i=0
for i in range(149):
 d_Theta4.append(i)
 d_Theta4[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][3])
 print("d_Theta_4: %s" % (d_Theta4[i]))
 i=i+1

class d_Theta_5:
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
d_theta5 = []
i=0
for i in range(149):
 d_theta5.append(i)
 d_theta5[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][0])
 print("d_Theta_5: %s" % (d_theta5[i]))
 i=i+1

class d_Theta_6:
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
d_theta6 = []
i=0
for i in range(149):
 d_theta6.append(i)
 d_theta6[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][1])
 print("d_Theta_6: %s" % (d_theta6[i]))
 i=i+1

class d_Theta_7:
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
d_theta7 = []
i=0
for i in range(149):
 d_theta7.append(i)
 d_theta7[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][2])
 print("d_Theta_7: %s" % (d_theta7[i]))
 i=i+1

class d_Theta_8:
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
d_theta8 = []
i=0
for i in range(149):
 d_theta8.append(i)
 d_theta8[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][3])
 print("d_Theta_8: %s" % (d_theta8[i]))
 i=i+1

class d_Bias:
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
d_Bias = []
i=0
for i in range(149):
 d_Bias.append(i)
 d_Bias[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*1
 print("d_Bias: %s" % (d_Bias[i]))
 i=i+1 

class d_Bias_2:
 def __init__(self, sigmoid, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
d_Bias2 = []
i=0
for i in range(149):
 d_Bias2.append(i)
 d_Bias2[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*1
 print("d_Bias_2: %s" % (d_Bias2[i]))
 i=i+1

 class new_Theta1:
  def __init__(self, Theta_1, learningrate, d_Theta1):
    self.Theta_1 = Theta_1
    self.learningrate = learningrate
    self.d_Theta1 = d_Theta1
new_Theta1 = []
i=0
for i in range(149):
 new_Theta1.append(i)
 new_Theta1[i]=(Theta_1-learningrate*d_Theta1[i])
 i=i+1

class new_Theta2:
 def __init__(self, Theta_2, learningrate, d_Theta2):
  self.Theta_2 = Theta_2
  self.learningrate = learningrate
  self.d_Theta2 = d_Theta2
new_Theta2 = []
i=0
for i in range(149):
 new_Theta2.append(i)
 new_Theta2[i]=(Theta_2-learningrate*d_Theta2[i])
 i=i+1

class new_Theta3:
 def __init__(self, Theta_3, learningrate, d_Theta3):
  self.Theta_3 = Theta_3
  self.learningrate = learningrate
  self.d_Theta3 = d_Theta3
new_Theta3 = []
i=0
for i in range(149):
 new_Theta3.append(i)
 new_Theta3[i]=(Theta_3-learningrate*d_Theta3[i])
 i=i+1

class new_Theta4:
 def __init__(self, Theta_4, learningrate, d_Theta4):
  self.Theta_4 = Theta_4
  self.learningrate = learningrate
  self.d_Theta4 = d_Theta4
new_Theta4 = []
i=0
for i in range(149):
 new_Theta4.append(i)
 new_Theta4[i]=(Theta_4-learningrate*d_Theta4[i])
 i=i+1

class new_theta5:
 def __init__(self, Theta_5, learningrate, d_theta5):
  self.Theta_5 = Theta_5
  self.learningrate = learningrate
  self.d_theta5 = d_theta5
new_theta5 = []
i=0
for i in range(149):
 new_theta5.append(i)
 new_theta5[i]=(Theta_5-learningrate*d_theta5[i])
 i=i+1

class new_theta6:
 def __init__(self, Theta_6, learningrate, d_theta6):
  self.Theta_6 = Theta_6
  self.learningrate = learningrate
  self.d_theta6 = d_theta6
new_theta6 = []
i=0
for i in range(149):
 new_theta6.append(i)
 new_theta6[i]=(Theta_6-learningrate*d_theta6[i])
 i=i+1

class new_theta7:
 def __init__(self, Theta_7, learningrate, d_theta7):
  self.Theta_7 = Theta_7
  self.learningrate = learningrate
  self.d_theta7 = d_theta7
new_theta7 = []
i=0
for i in range(149):
 new_theta7.append(i)
 new_theta7[i]=(Theta_7-learningrate*d_theta7[i])
 i=i+1

class new_theta8:
 def __init__(self, Theta_8, learningrate, d_theta8):
  self.Theta_8 = Theta_8
  self.learningrate = learningrate
  self.d_theta8 = d_theta8
new_theta8 = []
i=0
for i in range(149):
 new_theta8.append(i)
 new_theta8[i]=(Theta_8-learningrate*d_theta8[i])
 i=i+1

class new_bias:
 def __init__(self, Bias, learningrate, d_Bias):
  self.Bias = Bias
  self.learningrate = learningrate
  self.d_Bias = d_Bias
new_bias = []
i=0
for i in range(149):
 new_bias.append(i)
 new_bias[i]=(Bias-learningrate*d_Bias[i])
 i=i+1

class new_bias2:
 def __init__(self, Bias_2, learningrate, d_Bias2):
  self.Bias_2 = Bias_2
  self.learningrate = learningrate
  self.d_Bias2 = d_Bias2
new_bias2 = []
i=0
for i in range(149):
 new_bias2.append(i)
 new_bias2[i]=(Bias_2-learningrate*d_Bias2[i])
 i=i+1

class error_avg:
 def __init__(self, error):
  self.error = error
error_avg = []
i=0
for i in range(149):
 error_avg.append(i)
 error_avg[i]=(error[i]/150)
 print("Error Average: %s" % (error_avg[i]))
 i=i+1

class error_avg2:
 def __init__(self, Error_2):
  self.Error_2 = Error_2
error_avg2 = []
i=0
for i in range(149):
 error_avg2.append(i)
 error_avg2[i]=(Error_2[i]/150)
 print("Error Average2: %s" % (error_avg2[i]))
 i=i+1

class accuracy:
 def __init__(self, spamreader, prediction, prediction2):
  self.spamreader = spamreader
  self.prediction = prediction
  self.prediction2 = prediction2
accuracy = []
i=0
for i in range(149):
 accuracy.append(i)
 accuracy[i]=(spamreader[i][5] == prediction and spamreader[i][6] == prediction2)
 i=i+1

class accu_avg:
 def __init__(self, accuracy):
  self.accuracy = accuracy
accu_avg = []
i=0
for i in range(149):
 accu_avg.append(i)
 accu_avg[i]=(accuracy[i]/150)
 print("accuracy Average: %s" % (accu_avg[i]))
 i=i+1


plt.figure('error')
plt.plot(i,error_avg,'-o')
plt.figure('Error_2')
plt.plot(i,error_avg2,'-o')
plt.figure('Accurate')
plt.plot(i,accuracy,'-o')

plt.show()
plt.savefig("temp.png")