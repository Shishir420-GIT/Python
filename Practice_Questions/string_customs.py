def custom_lower(string):
    result = ''
    for char in string:
        if 'A' <= char <= 'Z':  # Check if the character is uppercase
            result += chr(ord(char) + 32)  # Convert to lowercase by adding 32 to its ASCII value
        else:
            result += char
    return result

def custom_upper(string):
    result = ''
    for char in string:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase by subtracting 32 from its ASCII value
        else:
            result += char
    return result

def custom_title(string):
    result = ''
    capitalize_next = True  # Flag to capitalize the first character of each word
    for char in string:
        if char == ' ':  # When a space is encountered, the next character should be capitalized
            capitalize_next = True
            result += char
        elif capitalize_next and 'a' <= char <= 'z':  # If lowercase and needs to be capitalized
            result += chr(ord(char) - 32)  # Convert to uppercase
            capitalize_next = False
        elif not capitalize_next and 'A' <= char <= 'Z':  # Convert subsequent characters to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char
            capitalize_next = False  # For non-space characters that don't need to be capitalized
    return result

def custom_capitalize(string):
    result = ''
    capitalize_next = True  # Flag to capitalize the first character
    for char in string:
        if capitalize_next and 'a' <= char <= 'z':  # If lowercase and needs to be capitalized
            result += chr(ord(char) - 32)  # Convert to uppercase
            capitalize_next = False
        elif not capitalize_next and 'A' <= char <= 'Z':  # Convert subsequent characters to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char
            capitalize_next = False
    return result

def custom_swapcase(string):
    result = ''
    for char in string:
        if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char  # Non-alphabetical characters remain the same
    return result

def custom_replace(string, old, new):
    result = ''
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:  # Check if the substring matches 'old'
            result += new  # Replace with 'new'
            i += len(old)  # Skip ahead by the length of 'old'
        else:
            result += string[i]  # Keep the current character if it doesn't match
            i += 1
    return result

# Example usage
input_str = "Hello World!  Python is Fun."

# Custom lower() implementation
print("Lower:", custom_lower(input_str))

# Custom upper() implementation
print("Upper:", custom_upper(input_str))

# Custom title() implementation
print("Title:", custom_title(input_str))

# Custom capitalize() implementation
print("Capitalize:", custom_capitalize(input_str))

# Custom swapcase() implementation
print("Swapcase:", custom_swapcase(input_str))

# Custom replace() implementation
print("Replace 'Python' with 'Coding':", custom_replace(input_str, 'Python', 'Coding'))
