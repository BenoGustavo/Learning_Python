from time import sleep

pair = 0 ; odd = 0 

for i in range(51):
    sleep(0.5)
    if i % 2 == 0:
        pair += 1
        print(f"\nPair number {i}")
    else:
        odd += 1
        print(f"\nOdd number {i}")

print(f"\nThere is {odd} odd numbers and {pair} pair numbers...")