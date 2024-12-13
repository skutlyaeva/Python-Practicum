def is_palindrome(s):
    if isinstance(s, int) or isinstance(s, float):
        s = str(abs(s))
    return s == s[::-1]