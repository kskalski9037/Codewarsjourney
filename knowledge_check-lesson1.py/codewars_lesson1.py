# This is my solution for the first codewars assignment

def even_or_odd(number):
  if number % 2 == 0:
    return"Even"
  else:
    return "Odd"
  
# This is my second solution for the codewars assignment

def number_to_string(num):
    return str(num)
  

# Third solution for codewars assignment

def get_count(sentence):

    vowel_count = 0

    for char in sentence:
        print(char)
        if char == "a":
            vowel_count += 1
        if char == "e":
            vowel_count += 1
        if char == "i":
            vowel_count += 1
        if char == "o":
            vowel_count += 1
        if char == "u":
            vowel_count += 1

    return vowel_count