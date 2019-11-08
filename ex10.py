from collections import OrderedDict

graph: OrderedDict = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['G'],
         'E': ['F'],
         'F': ['C'],
         'G': []
         }

graph: OrderedDict = {'A': ['B', 'C', 'D'],
         'H': [],
         'B': [],
         'C': ['E', 'D'],
         'D': ['B'],
         'E': [],
         'F': [],
         'G': ['A']
         }

graph: OrderedDict = {'5': ['0', '2'],
         '4': ['0', '1'],
         '2': ['3'],
         '3': ['1'],
         '1': [],
         '0': []
         }


#print(len(graph))

def topologicalSort(graph: OrderedDict):
    keys = list(graph)
    #print(keys)

    visited = [False] * len(graph)

    ans: list = []

    def dfs(u):

        visited[keys.index(u)] = True

        for e in graph[u]:
            if not visited[keys.index(u)]:
                dfs(e)

        ans.insert(0, u)
        #print(visited)


    for v in graph:
        #print(visited)
        if not visited[keys.index(v)]:
             dfs(v)


    ans.reverse()
    return ans


print(topologicalSort(graph))



