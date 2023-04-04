# Acquire display date with a prompt
# Acquired variables
exam_st_date = (11, 12, 2014)

# Reformat tuples to string to concatenate output
month = str(exam_st_date[0])
day = str(exam_st_date[1])
year = str(exam_st_date[2])

# Output start date based on reformated values
print("\nThe examination will start at: " +
      month + " / " + day + " / " + year + "\n")

# Clear solution from example
print("\nThe examination will start at: %i / %i / %i\n" % exam_st_date)
