string = input("Bir kelime giriniz: ")
ters=string[::-1]

if ters == string:
    print('The string you enter is a palindrome string.')
else:
    print('The string you enter is not a palindrome string.')