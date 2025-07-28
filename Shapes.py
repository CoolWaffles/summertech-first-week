# for j in range(5):
#     for i in range(5):
#         print("o ", end="")
#     print()

# for i in range(1):
#     print("x ", end="")
# print()
# for i in range(2):
#     print("x ", end="")
# print()
# for i in range(3):
#     print("x ", end="")
# print()
# for i in range(4):
#     print("x ", end="")
# print()

# for j in range(4):
#     for i in range(j+1):
#         print("x ", end="")
#     print()

for j in range(4):
    for i in range(3-j):
        print(" ", end="")
    for i in range(j+1):
        print("x ", end="")
    print()
for j in range(3):
    for i in range(j+1):
        print(" ", end="")
    for i in range(3-j):
        print("x ", end="")
    print()