input = "d5_input.txt"

nice_words = 0
vowels  =  ["a","e","i","o","u"]
double_letter = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]

with open(input, "r") as f:
    for line in f:

        contains_double_letter = False
        if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
            print(f"{line.strip()} is naughty because it contains ab, cd, pq, or xy")
        else:
            for i in range(len(double_letter)):
                if double_letter[i] in line:
                    print(f"{line.strip()} contains double letter {double_letter[i]}")
                    contains_double_letter = True
            vowel_count = 0
            for i in range(len(vowels)):
                line.count(vowels[i])
                vowel_count += line.count(vowels[i])
            if vowel_count >= 3 and contains_double_letter:
                print(f"{line.strip()} is nice because it contains at least 3 vowels and has a double letter")
                nice_words += 1

print(nice_words)