# Part A – Basic Number Patterns

# ===================================================

# 1.

# 1
# 22
# 333
# 4444
# 55555

# n=int(input("enter your num of row you want :- "))

# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(i,end="")
#     print()

# =====================================================

# 2.

# 5
# 44
# 333
# 2222
# 11111

# n = int(input("Enter your number of rows: "))
# for i in range (n,0,-1):
#     for j in range(n,i-1,-1):
#         print(i, end="")
#     print()

# ==============================================================================

# 3.
#     1
#    22
#   333
#  4444
# 55555


# for i in range(1,6,1):
#     for j in range(1,6-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(i,end="")
#     print()

# ======================================================================================


# 4.

# 55555
#  4444
#   333
#    22
#     1

# for i in range(5,0,-1):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(i,0,-1):
#         print(i,end="")
#     print()


# =============================================================================

# Part B – Pyramid Patterns

# 5.
#     1
#    222
#   33333
#  4444444
# 555555555

# for i in range (1,6):
#     for j in range(6-i):
#         print(" ", end="")
#     for k in range(i*2-1):
#         print(i,end="")
#     print()

# =============================================================================


# 6.
# 555555555
#  4444444
#   33333
#    222
#     1

# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i*2-1):
#         print(i,end="")
#     print()

# =============================================================================


# 7.

#     5
#    444
#   33333
#  2222222
# 111111111


# for i in range(5, 0, -1):    
#     for j in range(i - 1):
#         print(" ", end="")
#     for k in range(2 * (6 - i) - 1):
#         print(i, end="")
    
#     print()

# ==============================================================

# 8.
# 111111111
#  2222222
#   33333
#    444
#     5

for i in range(1,6,1):
    for j in range(i-1):
        print(" ", end="")
    for k in range(2*(7-i)-1):
        print(i, end="")
    print()
