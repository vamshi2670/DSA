#fibnoci series means two numbers 0 and 1 next number is sum of those
# two numbers  ex : 0+1+1+2+3+5+8+13.....

#using loop
x=0
y=1
for i in range(10):
    z=x+y
    print(x)
    y=x
    x=z

# using recursion
count=2
def fib(prev1,prev2):
    global count
    if count<=20:
        new_num=prev1+prev2
        print(new_num)
        prev2=prev1
        prev1=new_num
        count+=1
        fib(prev1,prev2)
fib(0,1)

#using nth term f(x)=f(x-1)+(x-2)
def f(x):
    if x<1:
        return 1
    else:
        return f(x-1)+f(x-2)
print('nth term:',f(10))
