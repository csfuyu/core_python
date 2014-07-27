#encoding:utf-8
#     5-2 运算符
#    (a) 写一个函数，计算并返回两个数的乘积
#    (b) 写一段代码调用这个函数，并显示它的结果
import math
import sys

def multi(a, b):
    return a * b

def test5_2():
    print multi(43,54)
    print multi(34.53, 34.6)
    print multi(-1.40, -324.84)

    
'''
    5-3 标准类型运算符. 写一段脚本，输入一个测验成绩，根据下面的标准，输出他的评分
成绩（A-F）。
A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: <60
'''

def score():
    num = int(raw_input("Enter the score number: "))
    while( num != -1):
        if(num < 60):
            print 'F'
        elif(num < 70):
            print 'D'
        elif(num < 80):
            print 'C'
        elif(num < 90):
            print 'B'
        elif(num <= 100):
            print 'A'
        else:
            print "Please enter a number <= 100"
        num = int(raw_input("Enter the score number: "))  

def test5_3():
    score()  
                
'''
5-4 取余。判断给定年份是否是闰年。使用下面的公式：
一个闰年就是指它可以被4 整除，但不能被100 整除， 或者它既可以被4 又可以被100 整
除。比如 1992，1996 和2000 年是闰年，但1967 和1900 则不是闰年。下一个是闰年的整世
纪是 2400 年。
'''
        
def leapyear(year):
    if(year % 4 == 0):
        if(year % 100 != 0):
            return True
        else:
            if(year % 400 == 0):
                return True
            else:
                return False
    return False

def test5_4():
    print "1992 is leap year: ", leapyear(1992)
    print "1996 is leap year: ", leapyear(1996)
    print "2000 is leap year: ", leapyear(2000)
    print "1990 is leap year: ", leapyear(1990)
    print "1967 is leap year: ", leapyear(1967)
    
'''
5-5 取余。取一个任意小于1 美元的金额，然后计算可以换成最少多少枚硬币。硬币有1
美分，5 美分，10 美分，25 美分四种。1 美元等于100 美分。举例来说，0.76 美元换算结果
应该是 3 枚25 美分，1 枚1 美分。类似76 枚1 美分，2 枚25 美分+2 枚10 美分+1 枚5 美分+1
枚1 美分这样的结果都是不符合要求的。
'''    
def coins(num):
    quar = int(num/25)
    ten = int((num-25*quar)/10)
    five = int((num-25*quar-10*ten)/5)
    head = num - 25*quar - 10*ten - 5*five
    return [quar,ten,five,head]
    
def test5_5():
    print coins(76)
                
'''
5-6 算术。写一个计算器程序 你的代码可以接受这样的表达式，两个操作数加一个运算符：
N1 运算符 N2. 其中 N1 和 N2 为整数或浮点数，运算符可以是+, -, *, /, %, ** 分别表示
加法，减法， 乘法， 整数除，取余和幂运算。计算这个表达式的结果，然后显示出来。提示：
可以使用字符串方法 split(),但不可以使用内建函数 eval().
'''
    
def calcu(exp):
    arr = exp.split(' ')
    #print arr
    n1 = int(arr[0])
    op = (arr[1])
    n2 = int(arr[2])
    #print n1,op,n2
    #return eval(op.join({str(n1),str(n2)}))
    if(op == '+'):
        return n1 + n2
    if(op == '-'):
        return n1 - n2
    if(op == '*'):
        return n1 * n2
    if(op == '/'):
        return n1 / n2
    if(op == '%'):
        return n1 % n2
    if(op == '**'):
        return n1 ** n2

def test5_6():
    print '+'.join({str(32),str(23)}), ": ",calcu('32 + 23')
    print '-'.join({str(32),str(23)}), ": ",calcu('32 - 23')
    print '*'.join({str(32),str(23)}), ": ",calcu('32 * 23')
    print '/'.join({str(32),str(23)}), ": ",calcu('32 / 23')
    print '%'.join({str(32),str(23)}), ": ",calcu('32 % 23')
    print '**'.join({str(32),str(2)}), ": ",calcu('32 ** 2')
       
'''
5-8 几何。计算面积和体积：
(a) 正方形 和 立方体
(b) 圆 和 球
'''
def area_square(line):
    return line ** 2

def volume_cubic(line):
    return line ** 3

def area_circle(r):
    return math.pi * r * r

def volume_ball(r):
    return 3.0 / 4 * math.pi * r * r * r
    
def test5_8():
    print "square 5 area: ", area_square(5)
    print "cubic 5 volume: ", volume_cubic(5)
    print "are 6 circle: ", area_circle(6)
    print "volume 9 ball: ", volume_ball(9)
       
'''
Python中二进制是以0b开头的: 
   例如: 0b11 则表示十进制的3 
8进制是以0开头的: 
   例如: 011则表示十进制的9 
16进制是以0x开头的: 
   例如: 0x11则表示十进制的17 
'''
def test5_9():
    print 017, 032
    print 17 + 32
    print 017 + 32
    print 017 + 032
    print 561 + 781
    
'''
5-10 转换。写一对函数来进行华氏度到摄氏度的转换。转换公式为C = (F - 32) * (5 / 9)
应该在这个练习中使用真正的除法， 否则你会得到不正确的结果
'''
def f_to_c(myf):
    return (myf-32) * (5.0/9)
    
def test5_10():
    print round(f_to_c(32),1)
    print round(f_to_c(33),1)
    print round(f_to_c(42),1)
    
'''
5-11 取余。
(a) 使用循环和算术运算，求出 0－20 之间的所有偶数
(b) 同上，不过这次输出所有的奇数
(c) 综合 (a) 和 (b)， 请问辨别奇数和偶数的最简单的方法是什么？
(d) 使用(c)的成果，写一个函数，检测一个整数能否被另一个整数整除。 先要求用户输
入两个数，然后你的函数判断两者是否有整除关系，根据判断结果分别返回 True 和 False;
'''
def find_even(maxnumber):
    returnlist = []
    i = 0
    while(i < maxnumber):
        returnlist.append(i)
        i = i + 2
    return returnlist

def find_odd(maxnumber):
    returnlist = []
    i = 1
    while(i < maxnumber):
        returnlist.append(i)
        i = i + 2
    return returnlist

def test5_11():
    print find_even(20)
    print find_odd(20)
          
'''
5-12 系统限制。写一段脚本确认一下你的Python 所能处理的整数，长整数，浮点数和复
数的范围
'''
def test5_12():
    print sys.maxint
    print sys.float_info.max
    print sys.float_info.min
          
'''
5–15. 最大公约数和最小公倍数。请计算两个整数的最大公约数和最小公倍数。
'''
def gc_divisor(a,b):
    if a > b:
        pivot = b
    else:
        pivot = a
    i = 1
    divisor = 1
    while(i <= pivot):
        if(a % i == 0 and b % i == 0):
            divisor = i
        i = i + 1
    return divisor

def lc_multiple(a,b):
    if a > b:
        bro = a
        sis = b
    else:
        sis = a
        bro = b
    
    common_multiple = bro
        
    while(common_multiple % sis != 0):
        common_multiple = bro + common_multiple
    
    return common_multiple
    
def test5_15():
    print gc_divisor(20,40)    
    print gc_divisor(12,28)
    print gc_divisor(120,55)
    print gc_divisor(-309,139)
    print lc_multiple(20,40)    
    print lc_multiple(12,28)
    print lc_multiple(120,55)
    print lc_multiple(309,139)
    
    
'''
5-16 家庭财务。给定一个初始金额和月开销数， 使用循环，确定剩下的金额和当月的支
出数， 包括最后的支出数。 Payment() 函数会用到初始金额和月额度， 输出结果应该类似下
面的格式（例子中的数字仅用于演示）：
Enter opening balance:100.00
Edit By Vheavens
Edit By Vheavens
Enter monthly payment: 16.13
Amount Remaining
Pymt# Paid Balance
----- ------ ---------
0 $ 0.00 $100.00
1 $16.13 $ 83.87
2 $16.13 $ 67.74
3 $16.13 $ 51.61
4 $16.13 $ 35.48
5 $16.13 $ 19.35
6 $16.13 $ 3.22
7 $ 3.22 $ 0.00
'''
def payment(balance, paid):
    returnBalance = [balance]
    while((balance - paid) > 0):
        balance = balance - paid
        returnBalance.append(balance)
    returnBalance.append(0.0)
    return returnBalance

def test5_16(balance,paid):
    print "Pymt#     Paid        Balance"
    print "-----     ------      -------"
    print "0         $ 0.00      $", balance
    
    #print payment(balance,paid)
    balanceResult = payment(balance,paid)
    i = 1
    while(i < len(balanceResult)):
        print i, "        $", paid, "    $ ", balanceResult[i]
        i = i + 1
    

if __name__ == "__main__":
    test5_16(100,16.13)
    