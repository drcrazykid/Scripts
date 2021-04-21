## initializing the lists
words = ["hi", "hello", "bye", "good"]
characters = ["h", "i", "b", "y", "e"]
## function which returns dictionary containing char counts
def char_count(word):
   ## initializing an empty dictionary
   char_count = {}
   ## loop to find the frequency of the chars
   for char in word:
      ## incrementing the char count by one
      char_count[char] = char_count.get(char, 0) + 1
   ## returning dictionary
   return char_count
## iterating through the words list
for word in words:
   ## initializing flag to one
   flag = 1
   ## getting the char count using char_count() function
   chars = char_count(word)
   ## iterating through the chars
   for key in chars:
      ## checking for the presence of key in the characters
      if key not in characters:
         ## updating the flag value to zero
         flag = 0
      else:
         ## comparing the count of chars in chars and characters
         if characters.count(key) != chars[key]:
            ## updating the flag value to zero
            flag = 0
      ## checking the flag value
      if flag == 1:
         print(word)