def is_palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

st = "A man, a plan, a canal: Panama"
print(is_palindrome(st))
