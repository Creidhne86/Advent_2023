import hashlib

test1 = "abcdef"
test2 = "pqrstuv"
input = "iwrupvqb"


num = 0
five_zeros = False
while num < 1000000000:
    
    hash = input + str(num)
    result = hashlib.md5(hash.encode())
    str_result = str(result.hexdigest())
    for i in range(6):
        
        if str_result[i] == "0":
            if i == 5: 
                print(f"i got here {str_result}, {num}")
                five_zeros = True
            
        else: 
            break
    if five_zeros:
        break
    num +=1

print(num)


