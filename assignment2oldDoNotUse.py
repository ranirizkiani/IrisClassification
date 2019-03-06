import csv
import random
import math

with open('C:/Users/Rani Kim/Desktop/irisdata/dataset.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     spamreader = list(spamreader)
     
print(spamreader[1][0])     

Theta_1=random.random()
Theta_2=random.random()
Theta_3=random.random()
Theta_4=random.random()
Theta_5=random.random()
Theta_6=random.random()
Theta_7=random.random()
Theta_8=random.random()


Bias=random.random()
Bias_2=random.random()
print("Bias : %s" % Bias)
print("Bias_2: %s" % Bias_2)

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
      self.target1 = target1

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


print("Theta_1: %s" % (Theta_1))
print("Theta_2: %s" % (Theta_2))
print("Theta_3: %s" % (Theta_3))
print("Theta_4: %s" % (Theta_4))
print("Theta_5: %s" % (Theta_5))
print("Theta_6: %s" % (Theta_6))
print("Theta_7: %s" % (Theta_7))
print("Theta_8: %s" % (Theta_8))

# D_theta_1=
# D_theta_2=
# D_theta_3=
# D_theta_4=
# D_theta_5=
# D_theta_6=
# D_theta_7=
# D_theta_8=

# sigmoid=
# sigmoid_2=
# prediction=
# prediction_2=
