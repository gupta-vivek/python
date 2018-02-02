import pickle


def mul(x, y):
    return x * y

a = pickle.dumps(mul)

b = pickle.loads(a)

print(b(2, 3))

# import dill as pickle
#
#
# def mul(x):
#     return x + 1
#
# g = pickle.dumps(mul)
# mul(1)
# print(pickle.loads(g)(1))