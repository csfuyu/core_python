# 3-10
'add exception handler to makeTextFile.py'

import os
ls = os.linesep

# get filename
while True:
    fname = 'D:/Python/core_python_2_mycode/core_python/ch03/'+raw_input('Enter the filename: ')
    try:
        fobj = open(fname, 'w')
    except IOError, e:
        print " *** file open error: ", e
    else:
        print 'file open ok'
        break
    
fobj.close()