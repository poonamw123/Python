class Numbers:
    #Constructor
    def __init__(self, value):
        self.Value = value
        
    # Check Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
    
    # Check perfect number
    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
                
        if sum == self.Value:
            return True
        else:
            return False
        
    # Display factors
    def Factors(self):
        print("Factors are : ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()
        
    # Sum of factors
    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i
                
        return sum
    
# Main program

obj1 = Numbers(6)

print("Prime : ", obj1.ChkPrime())
print("Perfect : ", obj1.ChkPerfect())
obj1.Factors()
print("Sum of factors : ", obj1.SumFactors())

print()

obj2 = Numbers(6)

print("Prime : ", obj2.ChkPrime())
print("Perfect : ", obj2.ChkPerfect())
obj2.Factors()
print("Sum of factors : ", obj2.SumFactors())