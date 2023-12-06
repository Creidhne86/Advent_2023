import hashlib

test1 = "abcdef"
test2 = "pqrstuv"
input = "iwrupvqb"


num = 0
while num < 609044:
    
    hash = test1 + str(num)
    result = hashlib.md5(hash.encode())
    
    num +=1
print(hash)
print(result.hexdigest())
