def max_duffel_bag_value(capacity, caketuples):
    max_value_at_capacity_n = [0] * (capacity + 1)
    for current_capacity in range(capacity + 1):
        current_max_value = 0
        for cake_weight, cake_value in caketuples:
            if cake_weight == 0 and cake_value != 0:
                return float('inf')
            if cake_weight <= current_capacity:
                max_value_using_cake = max_value_at_capacity_n[current_capacity - cake_weight] + cake_value
                current_max_value = max(max_value_using_cake, current_max_value)
                max_value_at_capacity_n[current_capacity] = current_max_value
    return max_value_at_capacity_n[capacity]


print(max_duffel_bag_value(20, [(7, 160), (3, 90), (2, 15)]))
