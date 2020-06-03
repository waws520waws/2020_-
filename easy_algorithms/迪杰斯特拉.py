"""
迪杰斯特拉算法：
首先需要构建三个字典：
第一个字典是连接图的字典，表明的是各个边之间的关系
第二个字典是需要一个花费表，这个表是不断迭代更新从起始节点到当前节点的最小花费
第三个字典的作用是记录从起始节点到这个节点的路径中，自己的父亲节点是谁 方便最终获得最短的路径

还需要一个列表来记录那些的点被展开过，若再次回到这个点，这个点已经被展开了，那么这个点就会被跳过
"""

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

parent=parents["fin"]
while parent:
    print(parent)
    if parent == "start":
        parent = None
    else:
        parent=parents[parent]
