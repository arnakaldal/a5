# Design an algorithm that generates the first n numbers in the following sequence:
# 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# Make sure that you write up the algorithm before starting to code.

# Liðir rununnar byggja á því að leggja saman síðustu 3 liði rununnar
n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 1
n2 = 2
n3 = 3
teljari = 1

while teljari <= n:
    print(n1)
    new_num = n1 + n2 + n3
    n1 = n2
    n2 = n3
    n3 = new_num
    teljari += 1


