def get_product_of_all_ints_except_at_index(ints_list):
    products_list = [None] * len(ints_list)
    product_so_far = 1
    for i in range(len(ints_list)):
        products_list[i] = product_so_far
        product_so_far = product_so_far * ints_list[i]

    product_so_far = 1
    for i in range(len(ints_list) - 1, -1, -1):
        products_list[i] *= product_so_far
        product_so_far = product_so_far * ints_list[i]

    return products_list


def get_product_of_all_ints_except_at_index_using_division(ints_list):
    products_of_all = 1
    products_list = [None] * len(ints_list)
    for i in range(len(ints_list)):
        if ints_list[i] == 0:
            products_list[i] = products_of_all
        else:
            products_of_all *= ints_list[i]

    for i in range(len(products_list)):
        if ints_list[i] == 0:
            products_list[i] = products_of_all
        else:
            products_list[i] = products_of_all / ints_list[i]

    return products_list


ints = [0, 7, 3, 4]
print(get_product_of_all_ints_except_at_index(ints))
print(get_product_of_all_ints_except_at_index_using_division(ints))
