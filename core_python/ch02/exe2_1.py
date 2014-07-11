# 2-5 
count = 0
while count <= 10:
    print count,
    count += 1

print

count = 0
while count in range(11):
    print count,
    count += 1
    
print 

# 2-6
num = raw_input('Enter a number if you want to test, or enter q to quit: ')
while num!='q':
    if int(num) > 0:
        print 'The num is positive'
    elif int(num) < 0:
        print 'The num is negative'
    else:
        print 'The num is zero'
    num = raw_input('Enter a number: ')

print
    
# 2-7
m_str = raw_input('enter a string:')
index = 0
while index < len(m_str):
    print m_str[index]
    index += 1

print

for ch in m_str:
    print ch
    
print

# arrays or list
m_array = (1,3,4,5,8)
#m_array = raw_input('enter an array:')

result = 0

for num in m_array:
    result += int(num)
print result, result/5.0
print

index = 0
result = 0
while index < len(m_array):
    result += m_array[index]
    index += 1
print result, result/5.0
print

# 2-10
while True:
    m_in = raw_input('Enter a number between 1 and 100:')
    if(float(m_in)>=1.0 and float(m_in)<=100.0):
        print 'success'
        break
    