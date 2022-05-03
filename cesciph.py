import sys

# take shift from user
shift = int(sys.argv[1]) 

# creates message variable
message = ""

# takes message from input
for line in sys.stdin:
  message = line
  break

# converts message to uppercase
message = message.upper()

# creates new message variable
new_message = ""

# creates variable to hold ascii value
asc_value = 0

# iterates through each character in message
for char in message:

  # converts character to ascii value
  asc_value = ord(char)

  # checks if character is not a special one
  if ((asc_value > 64) and (asc_value < 91)):

    # adds shift and subtracts 26 from value if it goes over the "Z" value
    if ((asc_value + shift) > 90):
      asc_value = (asc_value + shift) - 26

    # just adds shift if it does not go over "Z" value
    else:
      asc_value = (asc_value + shift)
  
  # does not shift if it's a special character
  else:
    asc_value = asc_value
  
  # adds new character to the new message
  new_message += chr(asc_value)

# prints the final message
print(new_message)


