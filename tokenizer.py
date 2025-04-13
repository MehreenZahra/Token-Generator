def tokenizer (text):
    tokens = []
    for char in text:
        code_point = ord(char)
        hex_code = f"0x{code_point:04x}"
#This line converts a character's Unicode code point into a standardized 4-digit hexadecimal string prefixed with '0x'. This consistent formatting is particularly useful when tokenizing text at the character level, as it ensures uniform representation of each character, which is beneficial for tasks like building vocabularies or analyzing text data.​

# Example
#If char = 'A', then:​
#code_point = ord('A') → 65​
#hex_code = f"0x{code_point:04x}" → '0x0041'​
#This results in the hexadecimal representation '0x0041' for the character 'A'.
        tokens.append(hex_code)
    return tokens

# Example usage:
english_text = "Hello, world! Welcome to AI world. Get Ready for the fun !"
hindi_text = "नमस्ते दुनिया!"

# Tokenize English text
english_tokens = tokenizer(english_text)
print("English Tokens:")
print(english_tokens)

# Tokenize Hindi text
hindi_tokens = tokenizer(hindi_text)
print("\nHindi Tokens:")
print(hindi_tokens)