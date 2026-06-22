import string

def is_palindrome(mystring: str) -> bool:
    mystring = mystring.lower()
    mystring = mystring.replace(' ', '')

    for char in string.punctuation:
        mystring = mystring.replace(char, '')

    mystring_reverse = mystring[::-1]
    return mystring_reverse == mystring


print('a.',is_palindrome('a.'))
print('A man, a plan, a canal: Panama',is_palindrome('A man, a plan, a canal: Panama'))
print('0P',is_palindrome('0P'))
print('aurora',is_palindrome('aurora'))
