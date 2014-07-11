# 2-11
def m_sum(array):
    result = 0.0
    for tmp in array:
        result += tmp
    return result

def m_avg(array):
    result = 0.0
    count = 0
    for tmp in array:
        result += tmp
        count += 1
    return result / count 

m_array = (1,4,6,49,59)

print 'm_array is',
print m_array

print '(1) sum'
print '(2) avg'
print '(3) quit'

op = raw_input('Enter your choice: ')

while int(op) != 3:
    if int(op) == 1:
        print 'sum is ',
        print m_sum(m_array)
    elif int(op) == 2:
        print 'average is ',
        print m_avg(m_array)
    else:
        print 'wrong chose, choose again.'
    op = raw_input('Enter your choice: ')
    
