rows = int(input("enter rows: "))
cols = int(input("enter cols: "))

source = [[0 for i in range(cols)] for j in range(rows)]
chuyenVi = [[0 for i in range(rows)] for j in range(cols)]

for i in range(rows):
    for j in range(cols):
        source[i][j] = int(input(f"a[{i},{j}]: "))
        
for i in range(rows):
    print(source[i])
        
for i in range(cols):
    for j in range(rows):
        chuyenVi[i][j] = source[j][i]
            
for i in range(cols):
    print(chuyenVi[i])