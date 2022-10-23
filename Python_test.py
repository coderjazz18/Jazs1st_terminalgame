"""Write a for loop that iterates from 0 through 9, inclusive, and 
prints each digit followed by whether the digit is even or odd. The expected output looks like this:

0 is even.

1 is odd.

2 is even.

3 is odd.

4 is even.

5 is odd.

6 is even.

7 is odd.

8 is even.

9 is odd."""

for num in range(10):
    if num % 2 == 0:
        print(str(num) + " is even.")
    else:
        print(str(num) + " is odd")