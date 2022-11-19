#converte de decimal para binario

def decimalToBinary(x):
    x=abs(x) #obtem o valor absoluto de x
    binary=""
    while(x>=2):
        binary+=("0"if x % 2 == 0 else "1")
        x = x//2
    binary+=f"{x}"
    return binary[::-1] if len(binary)>4 else (4-len(binary))*"0"+binary[::-1] 
print(decimalToBinary(182))
print(decimalToBinary(72))
print(decimalToBinary(20))
print(decimalToBinary(32))
print(decimalToBinary(4))
print(decimalToBinary(2))
print(decimalToBinary(1))
print(decimalToBinary(0))



