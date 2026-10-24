from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # solve using kahns algo. 

        # build indegree of each node.
        indegree = [0] * numCourses
        # build adj list. 
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[dst].append(src)
            indegree[src] += 1
        
        # any node with indegree of 0 gets put into the queue. 
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # then we pop from the queue and decrement its nei indegree by 1 and increment finish by 1.
        finish = 0
        while q:
            course = q.popleft()
            finish += 1
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        # then we check this nodes nei to see if their indegrees are ready to be put in queue (indegree of 0). if so add to q.
        return finish == numCourses
        # when queue is empty, check if finish == numCourses. if so return true


