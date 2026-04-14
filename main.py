#Write a program to display 1 to 10 numbers in reverse order and skip the number 5.

for i in reversed(range(1,11)):
    if i==5:
        continue
    print(i)

