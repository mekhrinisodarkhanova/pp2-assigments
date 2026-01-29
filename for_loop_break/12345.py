#1
for i in range(1, 10):
    if i == 5:
        break
    print(i)
#2
numbers = [3, 7, 2, -4, 8]
for n in numbers:
    if n < 0:
        break
    print(n)
#3
words = ["go", "run", "stop", "jump"]
for word in words:
    if word == "stop":
        break
    print(word)
#4
nums = [5, 3, 7, 0, 9]
for n in nums:
    if n == 0:
        break
    print(n)
#5
numbers = [1, 3, 5, 6, 7]
for n in numbers:
    if n % 2 == 0:
        print(n)
        break