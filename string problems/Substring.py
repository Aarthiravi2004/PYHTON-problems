str1 = "abcd"
substring = [str1[i:j] for i in range(len(str1)) for j in range(i+1,len(str1)+1)] 
print(substring)

OUTPUT:
['a','ab','abc','abcd','b','bc','bcd','c','cd','d']
