def find_first_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            print(f"First repeating character: {char}, Memory Address: {id(char)}")
            return char, id(char)
        else:
            char_count[char] = 1
    
    return None

# Test the function
input_string = "122"
result = find_first_repeating_character(input_string)
print(result)