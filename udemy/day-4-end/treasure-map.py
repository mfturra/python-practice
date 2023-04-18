# Prompt
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Adjust inputs to accurate num
col = int(position[0])-1
row = int(position[1])-1

# Create new reference list for modifying map values
location = [row, col]

# Modify map list based on user input
map[location[0]][location[1]] = 'X'

# Print updated map
print(f"{row1}\n{row2}\n{row3}")
