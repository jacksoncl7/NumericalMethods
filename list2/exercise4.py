

def sum_function(limit, rng, iterator):
    counter = 0
    for i in range(1, rng+1):
        counter += iterator

    return limit - counter

def topic_a():
    return sum_function(8000, 100000, 0.08)

def topic_b():
    return sum_function(10000, 800000, 0.0125)

print("tipic a result: {}".format(topic_a()))
print("tipic b result: {}".format(topic_b()))

