import sys

def break_brain():
    string_l = sys.stdin.read().splitlines()
    n, m = map(int, string_l[0].split())
    matrix_1 = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            if string_l[i + 1][j] == '#':
                matrix_1[i][j] = 1
    matrix_2 = [[0 for x in range(m)] for y in range(n)]
    matrix_2[0][0] = matrix_1[0][0]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            left = matrix_2[i - 1][j] if i - 1 >= 0 else 1e10
            top = matrix_2[i][j - 1] if j - 1 >= 0 else 1e10
            l_f = 0
            if i - 1 >= 0 and matrix_1[i - 1][j] == matrix_1[i][j]:
                if matrix_2[i - 1][j] <= left:
                    left = matrix_2[i - 1][j]
                    l_f = 1

            t_f = 0
            if j - 1 >= 0 and matrix_1[i][j - 1] == matrix_1[i][j]:
                if matrix_2[i][j - 1] <= top:
                    top = matrix_2[i][j - 1]
                    t_f =
            complime = 0 if (left <= top and l_f) or (top <= left and t_f) else matrix_1[i][j]

            matrix_2[i][j] = min(left, top) + complime
    return matrix_2[n - 1][m - 1]

if __name__=='__main__':
    string = '''
    2 2
.#
#.'''
    break_brain()
