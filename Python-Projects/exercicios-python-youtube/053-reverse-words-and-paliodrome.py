try:
    phrase = str(input("Type a phrase to check it reverse: "))
    print(f"\nThe phrase [{phrase}] reversed is {phrase[::-1]}")

    if phrase.replace(" ",'')[::] == phrase.replace(" ","")[::-1]:
        print("The phrase that you typed is a paliodrome...\n")
    else:
        print("The phrase that you typed isn't a paliodrome...\n")


except ValueError:
    print("\nPlease, insert a valid value...\n")