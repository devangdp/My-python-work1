class coputation:
    def __init__(self):
        pass

    def factorial(self, n):
        j=1
        for i in range(1, n+1):
            j=j*i
        return j

    def sum(self, n):
        j=1
        for i in range(1, n+1):
            j=j+i
        return j

    def mul(self, n):
        for i in range(1, 11):
            print(n,'x',i,'=', i*n)
       
c1=coputation()  

print(c1.factorial(6))
print(c1.sum(6))
print(c1.mul(6))