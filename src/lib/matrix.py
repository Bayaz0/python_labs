#является ли матрицей
def is_matrix(mat: list[list[float | int]]) -> bool:
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            return False
    return True

#транспонирование
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return list()
    if not is_matrix(mat):
        raise ValueError("ValueError")
    trans_mat = []
    n = len(mat[0])
    for j in range(n):
        new_row = []
        for row in mat:
            new_row.append(row[j])
        trans_mat.append(new_row)
    return trans_mat

#сумма каждой строки 
def row_sums(mat: list[list[float | int]]) -> list[float]:
    res = list()
    if not is_matrix(mat):
            raise ValueError("ValueError")
    for row in mat:
        res.append(sum(row))
    return res  

def col_sums(mat: list[list[float | int]]) -> list[float]:
    res = list()
    if not is_matrix(mat):
        raise ValueError("ValueError")
    n = len(mat[0])
    for j in range(n):
        sum = 0
        for row in mat:
            sum += row[j]
        res.append(sum)
    return res    