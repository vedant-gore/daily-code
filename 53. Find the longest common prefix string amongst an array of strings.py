def longest_common_prefix(strs):
    if not strs:
        return ""
    
    shortest_str = min(strs, key=len)
    
    i = 0
    while i < len(shortest_str):
        for other in strs:
            if other[i] != shortest_str[i]:
                return shortest_str[:i]
        i += 1
    
    return shortest_str

print(longest_common_prefix(["flower","flow","flight"]))  # Output: "fl"
print(longest_common_prefix(["dog","racecar","car"]))  # Output: ""
