from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # given arr prerequisites where prerequisities[i] = [a,b] means that you must take course b before a. b is a pre-req of a. 
        # return true if it is possible to finish all courses, otherwise return false. 
        # it is impossible to finish all courses if there is a cycle where for ex: b must be done before a and a must be done before b. 
        # we can detect cycles by checking if len(topo_order) < n nodes or we can keep a path set that records the path were currently on and if we reach a node thats already been visited, then we have a cycle. so return False. otherwise true. 

        # build an adj list where each node/course maps to a list of the courses that need it. 
        # initialize our seen set, path set.
        # run dfs on node. once dfs finishes all its neighbors should be recorded. 
            # if node in path, return false. if node in seen, continue. 
            # run dfs on its nei. 
        # return True

        adj = defaultdict(list) 
        for src, dst in prerequisites:
            adj[dst].append(src)
        
        path = set()
        seen = set()
        def dfs(dst):
            if dst in path:
                return False
            if dst in seen:
                return True
            path.add(dst)
            seen.add(dst)
            
            for nei in adj[dst]:
                if not dfs(nei):
                    return False
            path.remove(dst)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




