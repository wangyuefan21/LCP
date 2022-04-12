# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and
# it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
# You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost,
# return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique

# Greedy Approach
# calculate total gas available and cost, if gas is sufficient for the whole trip
# calculate diff = gas - cost, and prefix sum diff array, find the minimal sum
# which represent the gas deficit travel so far
def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    cons = [x - y for (x, y) in zip(gas, cost)]
    if sum(cons) < 0:
        return -1
    ans = -1
    min = 0
    cur = 0
    for i, con in enumerate(cons):
        cur += con
        if cur < min:
            min = cur
            ans = i
    return ans + 1

# Simulation Approach
# traverse the arrays
# accumulate total_surplus as gas - cost
# simulate the surplus of tank accumulate the gas - cost travelled to ith station
# if surplus reaches to negative, reset the surplus to 0 and set start as i + 1
# traverse to the end, see if total_surplus is greater or equal than 0
def canCompleteCircuit_sim(gas, cost):
    surplus = 0
    total_surplus = 0
    ans = 0
    for i in range(len(gas)):
        total_surplus += gas[i] - cost[i]
        surplus += gas[i] - cost[i]
        if surplus < 0:
            surplus = 0
            ans = i+1
    return -1 if total_surplus < 0 else ans


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert canCompleteCircuit(gas, cost) == 3
    assert canCompleteCircuit_sim(gas, cost) == 3

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert canCompleteCircuit(gas, cost) == -1
    assert canCompleteCircuit_sim(gas, cost) == -1

