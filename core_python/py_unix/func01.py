# def function
def pyfunc(m_i):
    print "Hello Function: ", m_i, 0XFF
    
def loopfunc():
    for i in range(5):
        pyfunc(i)
        
def mainfunc():
    loopfunc()
    
if __name__ == "__main__":
    mainfunc()