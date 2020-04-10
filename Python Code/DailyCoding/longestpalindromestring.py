def longestsubstringpalindrome(s):
    modified_string = ''
    for ch in s:
        modified_string += '#' + ch

    modified_string = '$' + modified_string + '#%'

    palin_length = [0] * len(modified_string)
    center, right = 0, 0
    for i in range(1, len(modified_string) - 1):
        mirror = 2 * center - i
        if i < right:
            palin_length[i] = min(right - i, palin_length[mirror])
        while modified_string[i + (1 + palin_length[i])] == modified_string[i - (1 + palin_length[i])]:
            palin_length[i] += 1
        if i + palin_length[i] > right:
            center = i
            right = i + palin_length[i]

    max_length = max(palin_length)
    max_index = palin_length.index(max_length)
    lon_palind_substring = modified_string[max_index - max_length:max_index + max_length].replace('#', '')
    return lon_palind_substring

def lonpalindromesubstring(s):
    if len(s) < 2 or s[::-1] == s:
        return s
    start, maxlen = 0, 1
    for i in range(len(s)):
        s_kd = s[i - maxlen: i + 1]
        s_kd2 = s[i - maxlen - 1: i + 1]
        if i - maxlen >= 0 and s_kd == s_kd[::-1]:
            start = i - maxlen
            maxlen += 1
        if i - maxlen - 1 >= 0  and s_kd2 == s_kd2[::-1]:
            start = i - maxlen - 1
            maxlen += 2
        print(s_kd + " s_kd")
        print(s_kd2 + 's_kd2')
    #print(s_kd)
    #print(s_kd2)
    return s[start: start + maxlen]


s = 'babad'
print(longestsubstringpalindrome(s))
print(lonpalindromesubstring(s))
