def Minimum_Window(s, t):
    char_need = {}
    for ch in t:
        if ch in char_need:
            char_need[ch] += 1
        else:
            char_need[ch] = 1
    print(char_need)

    for ch in s:
        if ch not in char_need:
            char_need[ch] = 0
    print(char_need)

    missing = len(t)
    fin_start, fin_end, current_start = 0, 0, 0

    for current_end, ch in enumerate(s, 1):
        if char_need[ch] > 0:
            missing -= 1
        char_need[ch] -= 1

        if missing == 0:
            while char_need[s[current_start]] < 0:
                char_need[s[current_start]] += 1
                current_start += 1
            if fin_end == 0 or current_end - current_start < fin_end - fin_start:
                fin_start = current_start
                fin_end = current_end

            char_need[s[current_start]] += 1
            missing += 1
            current_start += 1
    print(char_need)
    return s[fin_start:fin_end]


s = "ADOBEABODEBANC"
t = "ABC"

print(Minimum_Window(s, t))
