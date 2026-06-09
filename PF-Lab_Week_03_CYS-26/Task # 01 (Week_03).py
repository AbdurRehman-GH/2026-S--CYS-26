def factorial(a):
    fac=1
    for i in range(fac,a+1):
            fac=fac*i
    return fac
num=int(input("Enter a number: "))
f=factorial(num)
print(f"The factorial of {num} is {f}")

def permutation(n,r):
      result=factorial(n)/factorial(n-r)
      return result

def combination(n,r):
      result=factorial(n)/factorial(r)*factorial(n-r)
      return result

n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
p=permutation(n,r)
c=combination(n,r)

print("Permutation (nPr)=", int(p))
print("Combination (nCr)=", int(c))