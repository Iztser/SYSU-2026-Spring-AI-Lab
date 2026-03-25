def MatrixAdd(A,B):
    if(len(A) != len(B) or len(A[0]) != len(B[0])):
        return None
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        res.append(row)
    return res
    
def MatrixMul(A,B):
    if(len(A) != len(B) or len(A[0]) != len(B[0])):
        return None
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] * B[i][j])
        res.append(row)
    return res

n = int(input("请输入矩阵的规模："))
print(f"请输入矩阵A：")
A = [list(map(int,input().split())) for _ in range(n)]
print(f"请输入矩阵B:")
B = [list(map(int,input().split())) for _ in range(n)]
print(MatrixAdd(A,B))
print(MatrixMul(A,B))