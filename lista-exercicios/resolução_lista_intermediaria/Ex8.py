def palindrome(s):
    return s == s[::-1]

s = input("Digite uma string: ")
print(palindrome(s))