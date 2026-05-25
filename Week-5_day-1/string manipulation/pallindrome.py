def is_paalindrome(text):
    """Check if a string is a palindrome"""
    return text == text[::-1]
print(is_paalindrome("madam"))