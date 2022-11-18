# create a function that returns an array of 2 dimensions:
# each cell value will be the multiplication of its x, y position (indices) in the array, base 1.
# for example: cell value at position 2, 3 will be 2 x 3 = 6
# The function takes 2 parameters: number of rows, number of columns to define the array dimensions

def array_multiplication(nb_row, nb_col):
    res = []
    for i in range(nb_row):
        row_list = []
        for j in range(nb_col):
            row_list.append(i*j)
        res.append(row_list)
    return res


print(array_multiplication(3, 3))
