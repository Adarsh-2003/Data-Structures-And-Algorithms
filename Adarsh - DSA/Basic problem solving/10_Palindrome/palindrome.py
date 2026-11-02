num = int(input('Enter a number:'))
og_num = num
rev_num = 0
while (num >0):
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10

if rev_num == og_num:
    print('Yo dawg is palindrome')
else:
    print('Aint no way yo dawg a palindrome')