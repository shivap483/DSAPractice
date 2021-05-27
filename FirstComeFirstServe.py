def is_first_come_first_serve(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    take_out_orders_index_max = len(take_out_orders) - 1
    dine_in_orders_index = 0
    dine_in_orders_index_max = len(dine_in_orders) - 1
    for order in served_orders:
        if take_out_orders_index <= take_out_orders_index_max and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1
        elif dine_in_orders_index <= dine_in_orders_index_max and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1
        else:
            return False

    if take_out_orders_index != len(take_out_orders) or dine_in_orders_index != len(dine_in_orders):
        return False
    return True


to1 = [1, 3, 5]
di1 = [2, 4, 6]
so1 = [1, 2, 4, 6, 5, 3]
print(is_first_come_first_serve(to1, di1, so1))
to2 = [17, 8, 24]
di2 = [12, 19, 2]
so2 = [17, 8, 12, 19, 24, 2]
print(is_first_come_first_serve(to2, di2, so2))


