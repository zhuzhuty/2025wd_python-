"""
Created on 2025-01-08
"""

# Your code starts here
num_set = {1, 2, 3, 4, 5}
fruits = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

if __name__ == '__main__':
    print(type(num_set))
    print(fruits.difference(y))
    fruits.difference_update(y)
    # print(fruits)
    print(fruits.union(y))