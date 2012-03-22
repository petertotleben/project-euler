#!/usr/bin/python
#
# Project Euler -- Problem 32
#
# How many ways are there to make 2 pounds using any number of english coins

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def find(value, coin_list):
    print "value = {0} coin list = {1}".format(value, coin_list)
    if value == 0:
        print"\tvalue = 0, returning 1"
        return 1
    if coin_list[0] == 1:
        print "\t1 is head, returning 1"
        return 1
    if coin_list[0] == value:
        print "\t coinlist = value, recurse"
        return 1 + find(value, coin_list[1:])

    print "\tmain part"
    max_tries = value / coin_list[0]
    list_to_try = [i * coin_list[0] for i in range(max_tries+1)]
    print "\tneed to try this list {0}".format(list_to_try)
    values = [ find(value - i*coin_list[0], coin_list[1:]) for i in range(max_tries +1) ]
    return reduce( (lambda x, y: x+y), values )
    



if __name__ == "__main__":
    answer = find(200, coins)
    print "The answer is {0}".format(answer+1)

