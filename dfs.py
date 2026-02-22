def dfs(start,goal,graph,vis=None,path=None):
    if vis is None:
        vis=set()
    if path is None:
        path=[]
    path.append(start)
    vis.add(start)
    print(start)
    if start==goal:
        return path
    #vis.add(start)
    for child in graph[start]:
        if child not in vis:
            if dfs(child,goal,graph,vis):
                return True 
    return False
graph={'A':['B','D','E'],'B':['A','C','D','F'],'C':['B','E','F'],'D':['A','B','E'],'E':['A','C','D','F'],'F':['B','C','E']}
dfs('A','F',graph)
