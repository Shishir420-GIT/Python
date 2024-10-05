def calc(num1,num2,*chachis):
    output = 1
    print(chachis)
    for num in chachis:
        output *= num
    return output

if __name__ == "__main__":
    result = calc(1,2,3,4,5)
    print("Result: ", result)