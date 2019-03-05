class error:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
i=0
error = []
for i in range(149):
 error.append(i)
 error[i]=(sigmoid[i]-float(spamreader[i][5]))*(sigmoid[i]-float(spamreader[i][5]))
 print("error: %s" % (error[i]))
 i=i+1
  
class error_2:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
i=0
error2 = []
for i in range(149):
 error2.append(i)
 error2[i]=(sigmoid2[i]-float(spamreader[i][5]))*(sigmoid2[i]-float(spamreader[i][5]))
 print("error2: %s" % (error2[i]))
 i=i+1

class D_theta_1:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
i=0
D_theta1 = []
for i in range(149):
 D_theta1.append(i)
 D_theta1[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][0])
 print("D_theta_1: %s" % (D_theta1[i]))
 i=i+1

class D_theta_2:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
i=0
D_theta2 = []
for i in range(149):
 D_theta2.append(i)
 D_theta2[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][1])
 print("D_theta_2: %s" % (D_theta2[i]))
 i=i+1

class D_theta_3:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
i=0
D_theta3 = []
for i in range(149):
 D_theta3.append(i)
 D_theta3[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][2])
 print("D_theta_3: %s" % (D_theta3[i]))
 i=i+1

class D_theta_4:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
i=0
D_theta4 = []
for i in range(149):
 D_theta4.append(i)
 D_theta4[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*float(spamreader[i][3])
 print("D_theta_4: %s" % (D_theta4[i]))
 i=i+1

class D_theta_5:
 """docstring for error"""
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
i=0
D_theta5 = []
for i in range(149):
 D_theta5.append(i)
 D_theta5[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][0])
 print("D_theta_5: %s" % (D_theta5[i]))
 i=i+1

class D_theta_6:
 """docstring for error"""
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
i=0
D_theta6 = []
for i in range(149):
 D_theta6.append(i)
 D_theta6[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][1])
 print("D_theta_6: %s" % (D_theta6[i]))
 i=i+1

class D_theta_7:
 """docstring for error"""
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
i=0
D_theta7 = []
for i in range(149):
 D_theta7.append(i)
 D_theta7[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][2])
 print("D_theta_7: %s" % (D_theta7[i]))
 i=i+1

class D_theta_8:
 """docstring for error"""
 def __init__(self, sigmoid_2, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
i=0
D_theta8 = []
for i in range(149):
 D_theta8.append(i)
 D_theta8[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*float(spamreader[i][3])
 print("D_theta_8: %s" % (D_theta8[i]))
 i=i+1

class D_bias:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid = sigmoid
  self.spamreader= spamreader
i=0
D_bias = []
for i in range(149):
 D_bias.append(i)
 D_bias[i]=2*(sigmoid[i]-float(spamreader[i][5]))*(1-sigmoid[i])*sigmoid[i]*1
 print("D_bias: %s" % (D_bias[i]))
 i=i+1 

class D_bias_2:
 """docstring for error"""
 def __init__(self, sigmoid, spamreader):
  self.sigmoid2 = sigmoid2
  self.spamreader= spamreader
i=0
D_bias2 = []
for i in range(149):
 D_bias2.append(i)
 D_bias2[i]=2*(sigmoid2[i]-float(spamreader[i][6]))*(1-sigmoid2[i])*sigmoid2[i]*1
 print("D_bias_2: %s" % (D_bias2[i]))
 i=i+1