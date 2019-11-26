import math

row1 = int(input("Enter row for first matrix : "))
column1 = int(input("Enter column for first matrix 1: "))

firstmatrix = []

for i in range(row1):
    a = []
    for j in range(column1):
        a.append(int(input("{}{} -> ".format(i,j))))
    firstmatrix.append(a)


row2 = int(input("Enter row for second matrix : "))
column2 = int(input("Enter column for second matrix : "))

secondmatrix = []
add_result = []

for i in range(row2):
    a = []
    for j in range(column2):
        a.append(int(input("{}{} -> ".format(i,j))))
    secondmatrix.append(a)

for i in range(row2):
    a = []
    for j in range(column2):
        a.append(0)
    add_result.append(a)

for i in range(row1):
    for j in range(column1):
        add_result[i][j] = firstmatrix[i][j] + secondmatrix[i][j]

print("\nMatrix Addition Result: ")
for i in range(row1):
    print(add_result[i])

mul_result = []
for i in range(row2):
    a = []
    for j in range(column2):
        a.append(0)
    mul_result.append(a)

for i in range(row1):
   for j in range(column2):
      for k in range(row2):
         mul_result[i][j] += firstmatrix[i][k] * secondmatrix[k][j]

print("\nMatrix Multiplication Result: ")
for i in range(row1):
    print(mul_result[i])

trans_firstmatrix = []
for i in range(row2):
    a = []
    for j in range(column2):
        a.append(0)
    trans_firstmatrix.append(a)

trans_secondmatrix = []
for i in range(row2):
    a = []
    for j in range(column2):
        a.append(0)
    trans_secondmatrix.append(a)


for i in range(row1):
   for j in range(column1):
       trans_matrix1[j][i] = matrix1[i][j]

for i in range(row2):
   for j in range(column2):
       trans_matrix2[j][i] = matrix2[i][j]

print("\nTranspose of Matrix1: ")
for i in range(row1):
    print(trans_firstmatrix[i])


print("\nTranspose of Matrix2: ")
for i in range(row2):
    print(trans_secondmatrix[i])
