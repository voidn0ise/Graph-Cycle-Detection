class Graph(object):
    def __init__(self, data):
        self.data = data
        self.ret = {}

    def list2dict(self):
        for x, y in self.data:
            self.ret.setdefault(x, []).append(y)
        return self.ret

    def is_cyclic(self, ret):
        ret = self.ret
        visited = set()
        path = [object()]
        path_set = set(path)
        stack = [iter(ret)]
        while stack:
            for v in stack[-1]:
                if v in path_set:
                    return True
                elif v not in visited:
                    visited.add(v)
                    path.append(v)
                    path_set.add(v)
                    stack.append(iter(ret.get(v,())))
                    break
            else:
                path_set.remove(path.pop())
                stack.pop()
        return False


graph_array = Graph(list(input("Enter Multidimensional Array: ")))
try:
    arr = graph_array.list2dict()
    print(arr)
except:
    print("Can't convert array to list")
try:
    print(graph_array.is_cyclic(arr))
except:
    print("Incorrect Array formatting")