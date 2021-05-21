# -*- coding: utf-8 -*-
"""
Created on Fri May 21 05:12:44 2021

@author: NEW LAP
"""
import numpy as np

import threading
import time

class Vector:
    vector1 = np.array(np.random.randint(0,1000,1000))

    vector2 = np.array(np.random.randint(0,1000,1000))

    v1, v2 ,v3, v4, v5 = np.array_split(vector1 , 5)
    v6 , v7 , v8 , v9 ,v10 = np.array_split(vector2 , 5)
    
    threads_list = []
    def add(self,v1,v6):
        sum = []
        
        for i in range(len(v1)):
            sum.append(v1[i] + v6[i])   
        
        print(sum)
    def threads (self, target ,args1 ,args2 ):
        for i in range(5):
            t = threading.Thread(target=self.add ,  name = "thread{}".format(i),args = (args1,args2))
            self.threads_list.append(t)
            t.start()
            for t in self.threads_list:
                t.join()
            return t


v = Vector()

#l = [ v.v1, v.v2 ,v.v3, v.v4, v.v5 , v.v6 , v.v7 , v.v8 , v.v9 ,v.v10]
#len(l)
#for i  in l:
 #   s = v.add(l[i] ,v[ )
start = time.time()

#Final_sum = []
t1 = v.threads(v.add, v.v1, v.v6)
#Final_sum.append(s1)
t2 = v.threads(v.add, v.v2, v.v7)
#Final_sum.append(s2)
t3 = v.threads(v.add, v.v3, v.v8)
#Final_sum.append(s3) 
t4 =v.threads(v.add, v.v4, v.v9)
#Final_sum.append(s4) 
t5 =v.threads(v.add, v.v5, v.v10)
#Final_sum.append(s5)
#print(Final_sum)  
end = time.time()
print('Taken time{}'.format(end-start))
 #return the present time.
#for t in v.threads_list:
 #   t.join()
#print(Final_sum)  
'''    
#threads_list = []

start = time.time()
#for i in range(5):
t = threading.Thread(target=add1 ,  name = "thread1",args = (v1,v6))
threads_list.append(t)
t.start()
t2 = threading.Thread(target=add2 ,  name = "thread2",args = (v2,v7))
threads_list.append(t2)
t2.start()
t3 = threading.Thread(target=add3 ,  name = "thread3",args = (v3,v8))
threads_list.append(t3)
t3.start()
t4 = threading.Thread(target=add4 ,  name = "thread4",args = (v4,v9))
threads_list.append(t4)
t4.start()
t5 = threading.Thread(target=add5 ,  name = "thread5",args = (v5,v10))
threads_list.append(t5)
t5.start()
print("{} has started".format(t.name))



end = time.time() #return the present time.

print('Taken time{}'.format(end-start))

      
print("All five threads have finisheed thier tasks")

for 



def sleeper(n , name):
    print("Hi {}, i will sleep for 5 seconds \n".format(name))
    time.sleep(n)
    print("{} has to wake up from sleep \n".format(name))


t = threading.Thread(target=sleeper ,name='thread1' , args=(5,'thread1'))

t.start() #Start thread as independent command.
#t.join() #Wait until the thread terminates.

threads_list = []


# creation  of 5 theards.
start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper ,  name = "thread{}".format(i),args= (5, "thread{}".format(i)))
    threads_list.append(t)
    t.start()
    print("{} has started".format(t.name))


for t in threads_list:
    t.join()

end = time.time() #return the present time.

"""
vector1 = np.array(np.random.randint(0,1000,1000))

vector2 = np.array(np.random.randint(0,1000,1000))

v1, v2 ,v3, v4, v5 = np.array_split(vector1 , 5)
v6 , v7 , v8 , v9 ,v10 = np.array_split(vector2 , 5)  

def add(v1,v6):
    sum = []
    for i in range(len(v1)):
        sum.append(v1[i] + v6[i])
    
    return sum

    
    
    print("Vector Addition = ", sum)
    # This is how we can print a vector in python

def add2(v2,v7):
    
    sum = []
    for i in range(len(v1)):
        sum.append(v2[i] + v7[i])
    
    print("Vector Addition = ", sum)
    
def add3(v3,v8):
    
    sum = []
    for i in range(len(v1)):
        sum.append(v3[i] + v8[i])
    
    print("Vector Addition = ", sum)
def add4(v4,v9):
    
    sum = []
    for i in range(len(v1)):
        sum.append(v3[i] + v8[i])
    
    print("Vector Addition = ", sum)
def add5(v5,v10):
    
    sum = []
    for i in range(len(v1)):
        sum.append(v5[i] + v10[i])
    
    print("Vector Addition = ", sum)
    
#print('Taken time{}'.format(end-start))

      
print("All five threads have finisheed thier tasks")


print("Although From this thread  is not finished we can print this command")
print("Steps again")'''