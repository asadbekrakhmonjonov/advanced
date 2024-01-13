def row_sums(my_matrix: list):
    sum1 = sum(my_matrix[0])
    sum2 = sum(my_matrix[1])
    my_matrix[0].append(sum1)
    my_matrix[1].append(sum2)
if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
