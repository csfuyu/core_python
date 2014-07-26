import random
import string

print "random(): ", random.random()
print "uniform(10.20): ", random.uniform(10,20)
print "randInt(10,20): ", random.randint(10,20)
print "randInt(20,20): ", random.randint(20,20) 
#print "randInt(102,20): ", random.randint(102,20)
print

print range(10,100,5)
print random.randrange(10,100,5)
print 

p = ["Python", "is", "powerful", "simple", "and so on..."]  
random.shuffle(p)  
print p   
print

mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
mslice = random.sample(mlist, 5)  
print mslice  
print mlist 

print "rand int: ", random.randint(0,99)
print "rand even: ", random.randrange(0,101,2)
print "rand float: ", random.random()
print "rand character: ", random.choice('abcdedf#$%#^h')
print "several rand characters: ", random.sample('abcdefghijklmn',3)
print "build new string by using rand characters: ", string.join(random.sample('abcdefg',3)).replace(" ","")
print ",".join({'a':2,'b':1,'c':3})
print "pick object randomly: ", random.choice(['apple','orange','peach','pear','lemon'])
items = [1,2,3,4,5,6]
random.shuffle(items)
print "shuffle: ",items