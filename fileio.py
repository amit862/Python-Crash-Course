s = "Amit is a good boy"
# Writing to a file
# with open("test.txt", "w") as f:
#     f.write(s)

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()

# Reading to a file

with open("test.txt", "w") as f:
    s=f.read()
    print(s)

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()

