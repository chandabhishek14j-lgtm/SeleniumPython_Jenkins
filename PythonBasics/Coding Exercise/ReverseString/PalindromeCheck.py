def check_palindrome(word):
    # Checking Number
    if type(word) == int:
        num = str(word)
        rev_num = num[::-1]
        if num == rev_num:
            print("Palindrome num")
        else:
            print("Not Palindrome num")
    else: # word is not int
        # using reversed iterator
        reverse = "".join(reversed(word))
        if word == reverse:
            print("Palindrome via reversed")
        else:
            print("Not Palindrome via reversed")

        # using string splicing
        s = word[::-1]
        if s == word:
            print("Palindrome via splicing")
        else:
            print("Not Palindrome via splicing")



check_palindrome("hello")
check_palindrome("madam")
check_palindrome(121)
check_palindrome(123)
