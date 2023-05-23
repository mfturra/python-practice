# Version 1: Print first few lines of children's song with specific format
'''print("Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are.\n")'''

# Version 2: Break up phrase into segments
a = "Twinkle, twinkle, little star,"
b = "\tHow I wonder what you are!"
c = "\t\tUp above the world so high,"
d = "\t\tLike a diamond in the sky."
e = "Twinkle, twinkle, little star,"
f = "\tHow I wonder what you are!"

# Output string together using formatted string literals
# formatted string variables or f-strings facilitate inclusion of values into string statement
# Done by adding f or F prefix at start of string and {Python_expressions}
print(f'{a} \n {b} \n {c} \n {d} \n {e} \n {f}')

# Additional script playground
'''yes_votes = 42_572_654
no_votes = 43_132_492
percent = yes_votes / (yes_votes + no_votes)
print('\n\n{:-1} YES votes equaling {:1.1%}'.format(yes_votes, percent))'''
