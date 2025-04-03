def is_palindrome(s):
    left: int = 0
    right: int = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


assert is_palindrome("hi") is False
assert is_palindrome("malayalam") is True
assert is_palindrome("a") is True
