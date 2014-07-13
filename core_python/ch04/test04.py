# type
print type(43)
print type('a')
print type("a")
print type(1.0)
print type(True)
m_a = [1]
m_b = ()
print type(m_a)
print type(m_b)
print type(type(43))

# test bool
if None:
    print "None is False"
else:
    print True

if 0:
    print "0 is False"
else:
    print True
    
if (1-1):
    print "(1 - 1) is False"
else:
    print True
    
if 1.0:
    print "1.0 is False"
else:
    print True
    
a = ""
if a:
    print "'""' is False"
else:
    print True
    
m_array = []
print m_array,
if m_array:
    print " is False"
else:
    print True

b_array = ()
print b_array,
if b_array is False:
    print " is False"
else:
    print True

c_array = {}
print c_array,
if c_array is False:
    print " is False"
else:
    print True