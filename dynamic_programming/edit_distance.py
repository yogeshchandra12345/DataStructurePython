def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    temp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for row in range(m+1):
        for col in range(n+1):
            if row == 0:  # insert col elements in str1 to make it equal to str2
                temp[row][col] = col
            elif col == 0:  # delete row elements in str1 to make it equal to str2
                temp[row][col] = row
            elif str1[row - 1] == str2[col - 1]:
                temp[row][col] =  temp[row-1][col-1]
            else:  # minimum of insert, delete, replace operation on  row element in str1 to make it equal to str2
                temp[row][col] = 1 + min(temp[row][col-1], temp[row-1][col], temp[row-1][col-1])
    return temp[m][n]


str1 = "sunday"
str2 = "saturday"
print(edit_distance(str1, str2,))

