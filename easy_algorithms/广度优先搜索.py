"""
广度优先搜索的实现过程：
1.上面的部分是图的构建的过程
2.下面使用队列进行数据元素的存储
3.使用广度优先搜索的方式进行数据的检查
"""

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["anuj", "peggy"]
graph["bob"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque


def person_is_seller(person):
    return person[-1] == "m"


def find_mango_seller():
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
    return False


if __name__ == '__main__':
    find_mango_seller()
