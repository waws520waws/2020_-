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


"""
在这个版本中我们忽略了一个问题：就是我们的朋友中也可能有我们自己的存在，只是上面的图中并没有展示而已
这样假设我们在我的朋友中还会再次将我添加到搜索的队列中，这样将会形成死循环，所以改进的建议就是
增加一个列表，将搜索过的元素加入到这个列表中，以免再次对其进行搜索
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
"""


def find_mango_seller(name):
    search_queue = deque()
    search_queue += graph[name]
    search_list = []
    while search_queue:
        person = search_queue.popleft()
        if not person in search_list:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                search_list.append(person)
    return False


if __name__ == '__main__':
    find_mango_seller("you")
