from collections import  deque
def bfs(start,goal,graph,visited=None):
    visited=set()
    queue=deque([[start]])
    while queue:
        print("queue",queue)
        print("visited",visited)
        path=queue.popleft()
        print("path",path)
        node=path[-1]
        print("node",node)
        if node==goal:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path=path+[neighbor]
                print(new_path)
                queue.append(new_path)


graph={'A':['B','D','E'],'B':['A','C','D','F'],'C':['B','E','F'],'D':['A','B','E'],'E':['A','C','D','F'],'F':['B','C','E']}
bfs('A','F',graph)
