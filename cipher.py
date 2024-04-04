def cipher(text):
    shift = 5
    encrypted_text = ''
    # Dictionary mapping letters to their encrypted equivalents
    cipher_map = {
        'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j',
        'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o',
        'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't',
        'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y',
        'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd',
        'z': 'e',
        'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J',
        'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O',
        'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T',
        'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y',
        'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D',
        'Z': 'E'
    }

    # Encrypt each character in the text
    for char in text:
        # If the character is in the cipher map, append its encrypted lowercase equivalent
        if char in cipher_map:
            lower_ch = char.lower()
            encrypted_text += cipher_map[lower_ch]
        else:
            encrypted_text += char 
    #print(encrypted_text)
    return encrypted_text


# a dynamic way of solving it
# in a language that supports this, it would be possible to
# modify the string in-place, which has certain advantages
# this assumes ASCII-encoded letters and uses the corres-
# ponding ASCII code plus a little arithmetic to do the
# same thing as above without the extra storage overhead
# of a dictionary
# this does not convert the letters to lowercase, like 
# the above implementation, so the test would either have
# to change or you'd have to convert each letter to its
# lowercase equivalent to get the test to pass
def fancy_cipher2(input: str):
  offset = 5
  start_lower = ord('a') # 97
  end_lower = ord('z')   # 122
  start_upper = ord('A') # 65
  end_upper = ord('Z') # 90
  output = ""
  for ch in input:
    start = 0
    end = 0
    if ord(ch) >= start_lower and ord(ch) <= end_lower:
      start = start_lower
      end = end_lower
    elif ord(ch) >= start_upper and ord(ch) <= end_upper:
      start = start_upper
      end = end_upper
    else:
      output = output + ch
      continue
    transform = start + ((ord(ch) - start + offset)%(end-start+1))
    output = output + chr(transform)
#  print(output)
  return output

