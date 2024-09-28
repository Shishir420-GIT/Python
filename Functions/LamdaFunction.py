# lamba function: An inplace function for functions that doesn't need to be stored for repetitive process.

def giveNameLenth(name):
    return len(name)

if __name__ == "__main__":
    name = "Programmatic.ly"
    name2 = "BablucBadmaash"
    print(giveNameLenth(name))  # Output: 13

    var = lambda n: len(n)
    print(var(name2))  # Output: 14

    
