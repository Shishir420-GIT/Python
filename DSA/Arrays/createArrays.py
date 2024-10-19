import array

arr = array.array('i',[1,2,3,4])


print(arr[0])
print(type(arr))

print(arr.append(5)) #correct
print(arr.append("i")) #notcorrect

print(arr[4])