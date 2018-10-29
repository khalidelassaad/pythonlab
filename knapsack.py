# values, weights, capacity, return highest possible value


def knapsack(vals, weights, capacity):
    subresults = dict()
    knapsackhelper(vals,weights,capacity,0, subresults)
    return max(subresults.items(), key=lambda x: x[1])

#what helps solve a problem?
#if we know the capacity limits of all combinations!

def knapsackhelper(vals, weights, capacity, value, subresults): #contents is a set of value, weight tuples
    if not vals:
        return
    if capacity == 0:
        return
    #subresults maps a val weight cap triple to a max value
    if (vals, weights, capacity) in subresults:
        return
    #if can put in first item, create a case for it
    newvals = vals[1:]
    newweights = weights[1:]
    newcapacity_take = -1
    if weights[0] <= capacity:
        newcapacity_take = capacity - weights[0]
        newvalue_take = value + vals[0]
        if (newvals, newweights, newcapacity_take) in subresults:#value already in subresults, do nothing
            pass
        else:#value not in subresults, add it and return it
            subresults[(newvals, newweights, newcapacity_take)] = knapsackhelper(newvals, newweights, newcapacity_take,
                                                                            newvalue_take, subresults)
    #alternatively, choose not to take first item, what is result for remainder?
    newcapacity_dont = capacity
    newvalue_dont = value
    if (newvals, newweights, newcapacity_dont) in subresults:  # value already in subresults, do nothing
        pass
    else:  # value not in subresults, add it and return it
        subresults[(newvals, newweights, newcapacity_dont)] = knapsackhelper(newvals, newweights, newcapacity_dont,
                                                                        newvalue_dont, subresults)
    #set self value for as the max of the two branches
    if newcapacity_take == -1:
        subresults[(vals, weights, capacity)] = subresults[(newvals, newweights, newcapacity_dont)]
    else:
        subresults[(vals, weights, capacity)] = max(subresults[(newvals, newweights, newcapacity_dont)],
                                                subresults[(newvals, newweights, newcapacity_take)])
    return

print("Expected/Result: {}/{}".format(220,knapsack((60,100,120),(10,20,30),50)))
