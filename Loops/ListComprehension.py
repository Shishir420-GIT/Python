def square(num):
    return num * num

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    newList = [ i*i for i in nums]
    print(newList)
