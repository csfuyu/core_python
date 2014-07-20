# slice object
foostr = 'abcde'

print foostr
print foostr[::-1]
print

print foostr
print foostr[::-2]
print

# compare
print [3, 'abc'] == ['abc', 3]
print [3, 'abc'] == [3, 'abc']
print 3 < 4 < 7
print 5 > 4 == 4

# object
a = b = 4.3
c = 3.3 + 1

print id(a)
print id(b)
print "a is b:",
print a is b
print id(c)
print "c is b:",
print c is b
print "c == b:",
print c == b
print isinstance(a,type("a"))
print dir(a)

# cmp
a, b = 'abc', 'aby'
print cmp(a,b)
print cmp(b,a)
b = 'abc'
print cmp(a,b)