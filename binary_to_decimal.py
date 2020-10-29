List = list(map(int,input().split()))
print ("The List is : " + str(List))
# binary list to integer conversion
result = int("".join(str(i) for i in List),2)
# result
print ("The value is : " + str(result))
print(bin(result))
