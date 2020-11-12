from math import ceil ,floor

eps=1.0
while eps+1>1:
    eps/=2
eps*=2

def my_function(num1,num2,num3,num4,num5):

    result=float(num2)/float(num3)
    result=result-float(num4)
    result = result*(float(num1))
    result = result-float(num5)

    if(result+eps==ceil(result)):
        return ceil(result)

    if (result - eps == floor(result)):
        return floor(result)
    else:return result;



print(abs(my_function(3.0,4.0,3.0,1,1)))
