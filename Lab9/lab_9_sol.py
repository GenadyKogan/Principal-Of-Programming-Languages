# ----- Q1 ----- #
def text_preprocessing(text, stopwords):
    bag_words = {}
    filtered = filter(lambda x: x not in stopwords and not x.isnumeric(),map(lambda x: x.lower(), text.split()))
    for word in filtered:
        if word not in bag_words:
            bag_words[word] = 0
        bag_words[word] = bag_words[word]+1
    return bag_words

stop_list = ('is', 'it', 'a', 'the', 'my', 'and')
print(text_preprocessing('My cat is 10 and it is a very fat cat', stop_list))
# -------------- #


# ----- Q2 ----- #
def make_account():
    balance = 0
    def dispatch(x):
        if x == 'get':
            return balance
        elif x == 'change':
            def change(y):
                nonlocal balance
                if  dispatch('get') >= -y:
                    balance += y
                else:
                    return 'Out of funds during change'
                return balance
            return change
        elif x == 'move':
            def move(y,z):
                if z < 0:
                    return 'Negative transaction amount'
                elif dispatch('get') < z:
                    return 'Out of funds during change'
                else:
                    return (dispatch('change')(-z),y('change')(z))
            return move
        return balance
    return dispatch
# ------------------------------------------------
# a1 = make_account()
# a1 # => <function make_account.<locals>.dispatch at 0x0000022ABD3332F0>
# a2=make_account()
# a1('change')(20) # => 20
# a1('get') # => 20
# a1('change')(-25) # => 'Out of funds during change'
# a1('move')(a2, 7) # => (13, 7)
# a2('move')(a1, 2) # => (5, 15)
# a1('move')(a2, 30) # => 'Out of funds during change'
# a1('move')(a2, -30) # => 'Negative transaction amount'
# -------------- #

# ----- Q3 ----- #
from functools import reduce
from operator import add
#a
make_pairs = lambda el, lst: tuple(map(lambda x: (el, x), lst))
#b (two solutions)
c_prod = lambda lst1, lst2: tuple(map(lambda x: make_pairs(x, lst2), lst1))
c_prod = lambda lst1, lst2: tuple(make_pairs(x, lst2)for x in lst1)
#c
flat_c_prod = lambda lst1, lst2: reduce(add, c_prod(lst1, lst2), ())
#d
cond_c_prod = lambda p, lst1, lst2: flat_c_prod(tuple(filter(p, lst1)), tuple(filter(p, lst2)))
# -------------- #

# ----- Q4 ----- #
def easy_park(fee):
    ns = { 'balance' : 0 }
    def charge(amount):
        ns['balance'] += amount
        print(ns['balance'])
    def park(time):
        ns['balance'] -= float(time) * fee
        print('balance left: ' + str(ns['balance']))
    def dispatch(m, *args):
        if m == 'charge':
            return charge(*args)
        elif m == 'park':
            return park(*args)
        else:
            print('unknown message: ' + m)
    return dispatch
# -------------- #
