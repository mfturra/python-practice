# Prompt: Add up the sum of even number across the range
# Establish an empty iterable variable
even_total = 0

for i in range(1, 101, 1):
    if i % 2 == 0:
        even_total += i
        # print(f'Unskipped number is {i}')
    else:
        pass  # print(f'Skipped number is {i}')

# Output even_total value
print(f'Total even numbers is {even_total}')
