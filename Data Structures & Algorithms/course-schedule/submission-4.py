class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # given arr prerequisites where prerequisites[i] = [a,b]. this means we must take course b before a. (b -> a). 
        # given numCourses which are the total number of courses needed to be taken. labeled 0 - n-1. 
        # return true if its possible to finish all courses, else false. 

        # we can use dfs to do a topological sort, where we iterate over each course, and perform dfs on that course and have it return true or false

        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visited = set()
        path = set()

        # our dfs function will take the course and do a postorder traversal. so we will check if that node has been visited, if so continue, else add it. 
        # if the node has been in the path already, then we will return False. this means that we visited the same course twice on the same dfs run which means theres a cycle. well never be able to finish all courses. 
        # otherwise check the neighbors of the course. run dfs on them. 
        # return True at the end. 


        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            visited.add(node)
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            path.remove(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
