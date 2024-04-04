#def cipher(input: str):
  


#def cipher(input: str):
#  offset = 5
#  start_lower = ord('a') # 97
#  end_lower = ord('z')   # 122
#  start_upper = ord('A') # 65
#  end_upper = ord('Z') # 90
#  output = ""
#  for ch in input:
#    start = 0
#    end = 0
#    if ord(ch) >= start_lower and ord(ch) <= end_lower:
#      start = start_lower
#      end = end_lower
#    elif ord(ch) >= start_upper and ord(ch) <= end_upper:
#      start = start_upper
#      end = end_upper
#    else:
#      output = output + ch
#      continue
#    transform = start + ((ord(ch) - start + offset)%(end-start+1))
#    output = output + chr(transform)
#  print("FOOOOOOOOO")
#  print()
#  print()
#  print(output)
#  return output

#cipher("abcd Wxyz")
