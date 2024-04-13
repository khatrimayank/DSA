def longestSubstringWithoutRepeatingChars(s):
    n = len(s)
    max_length = 0
    left = 0
    right = 0
    chars_set = set()

    while right < n:
        if s[right] not in chars_set:
            chars_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            chars_set.remove(s[left])
            left += 1

    return max_length
print(longestSubstringWithoutRepeatingChars('bbb'))

''' print substring code
def longestSubstringWithoutRepeatingChars(s):
    n = len(s)
    max_length = 0
    start = 0
    end = 0
    chars_set = set()

    while end < n:
        if s[end] not in chars_set:
            chars_set.add(s[end])
            if end - start + 1 > max_length:
                max_length = end - start + 1
                substring = s[start:end+1]
            end += 1
        else:
            chars_set.remove(s[start])
            start += 1
        print(substring)
        print(chars_set)
    return substring

s = "crgcer"
print(longestSubstringWithoutRepeatingChars(s))  # Output: "abc"
