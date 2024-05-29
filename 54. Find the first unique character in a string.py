def first_unique_char(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1

print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode"))  # Output: 2
