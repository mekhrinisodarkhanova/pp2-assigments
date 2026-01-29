#1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
#2
numbers = [3, -1, 5, -7, 8]
for n in numbers:
    if n < 0:
        continue
    print(n)
#3
words = ["hello", "skip", "world", "skip", "python"]
for word in words:
    if word == "skip":
        continue
    print(word)
#4
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
#5
texts = ["Hi", "", "Python", "", "Code"]
for t in texts:
    if t == "":
        continue
    print(t)