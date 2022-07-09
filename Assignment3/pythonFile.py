
freq = {}                  # Create an empty dictionary
for c in text:             # Iterate over the characters in the text
    if c.isalpha():        # We count only letters
        c = c.lower()      # We consider 'a' and 'A' to be the same letter
        if c in freq:      # If c already is in the dictionary
            freq[c] += 1   # Add 1 to the value stored in freq[c]
        else:              # or, if c is not in freq
            freq[c] = 1    # Add c to freq and set its value to 1
print(freq)