#Count the Number of Vowels in a String:*
#python
text = "Hello, World"
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
print(f"Number of vowels: {count}")

N = 10
sum = 0
for i in range(2, N + 1, 2):
    sum += i
print(f"Sum of even numbers from 1 to {N}: {sum}")

