class Make_change():
    def __init__(self):
        self.memo = {}

    def change_possibilities_top_down(self, amount_left, denominations, current_index=0):

        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            print("grabbing memo[%s]" % memo_key)
            return self.memo[memo_key]

        if amount_left == 0:
            return 1
        if amount_left < 0:
            return 0

        if current_index == len(denominations):
            return 0
        print("checking ways to make %i with %s" % (amount_left, denominations[current_index:],))

        current_coin = denominations[current_index]
        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += self.change_possibilities_top_down(amount_left, denominations, current_index + 1)
            amount_left -= current_coin
        self.memo[memo_key] = num_possibilities
        return num_possibilities


def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
    return ways_of_doing_n_cents[amount]


a = Make_change()
print(change_possibilities_bottom_up(10, [1, 2, 3]))
