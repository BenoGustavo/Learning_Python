sentence = input("Insert a sentence: ").lower()

print(f"How many times the letter 'A' appers?\n {sentence.count('a')}")
print(f"When it first appers? {sentence.replace(' ','').find('a')}")
print(f"When it least appers? {sentence.replace(' ','').rfind('a')}")