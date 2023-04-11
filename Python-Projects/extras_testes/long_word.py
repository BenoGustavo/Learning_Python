proibido = '!@#$%^&*()|\][{'';.,></?`~}]'

blabla = 'somet!hing$#'

for letter in blabla:
  if letter in proibido:
    blabla.s

def LongestWord(sen):
  bigger = 0
  
  sen = sen.split()

  for words in sen:
    if len(words) >= bigger:
      bigger = words

  return sen

# keep this function call here 
print(LongestWord(input()))