strl = input("Enter your own string :")
vowels = 0
for i in strl:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'O' or i == 'I' or i == 'U'):
        vowels = vowels + 1
print("Total no of vowels in string =", vowels)
