def get_pascals_triangle_row(row_number: int) -> list:
    global array
    array = [1, 1]
    def get_pascals_triangle_row_1(row_number_1):
        global array
        if row_number_1 > 2:
            get_pascals_triangle_row_1(row_number_1 - 1)
        elif row_number_1 == 0:
            return [1]
        elif row_number_1 == 1:
            return [1, 1]
        tmp = [1]
        for i in range(len(array)-1):
            tmp.append(array[i] + array[i+1])
        tmp.append(1)
        array = tmp
        return array

    return get_pascals_triangle_row_1(row_number)