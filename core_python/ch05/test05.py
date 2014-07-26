import subprocess
import time
import math

anInt = 1
print id(anInt)
anInt += 1
print id(anInt)
print anInt
del anInt
anInt = True
print anInt

print

print 2 << 32
print 8898 ** 8

print divmod(10,3)

for eachNum in range(3):
    print round(math.pi, eachNum)
    
print "floor(0.51): ", math.floor(0.51)
print "floor(-1.2): ", math.floor(-1.2)
print "round(-1.2): ", round(-1.2)
print "round(0.3): ", round(0.3)    

'''
p=subprocess.Popen("notepad.exe")
t = 1
while(t <= 5):
    time.sleep(1)
    t +=1
    p.kill()
    #p.terminate()
    print ("new process was killed")
'''