print abs(-4)

myString = "Hello World"
print myString[1:]

num = 2
print "%s value is: %d" % ("num",num)

# test if statement
if num > 1:
    print 'num > 1 is true'
else:
    print 'num > 1 is false'
    

# test while statement
count = 0
while count < 3:
    print 'loop %d' % count
    count+=1
    
# test for
print 'I like to use the Internet for:'
for item in ['e-mail', 'net-surfing', 'homework', 'char']:
    print item,
print

'''
logfile = open('D:/Python/core_python_2_mycode/core_python/ch02/log.txt','a')
print >> logfile, 'Fatal error, invalid input'
logfile.close()

user = raw_input('Enter user name: ')
print 'Your login is:', user

num = raw_input('Now enter a number:')
print 'Doubling your number: %d' % (int(num) * 2)
'''

#test advanced
squared = [x**2 for x in range(4)]
for i in squared:
    print i
print 'end'
    
sqdEvens = [x**2 for x in range(8) if not x % 2]
for i in sqdEvens:
    print i
    
# test read file
count = 1
fobj = open('D:/Python/core_python_2_mycode/core_python/ch02/log.txt','r')
for eachLine in fobj:
    print count, eachLine,
    count += 1
fobj.close()

# test function
def addMe2Me(x):
    return (x + x)

print addMe2Me(4.25)