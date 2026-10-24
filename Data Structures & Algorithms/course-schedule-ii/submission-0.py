from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build an adj list (maps course: [courses that need course]) and indegrees (tells us how many prereqs a node has) for each node
        indegrees = [0] * numCourses
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegrees[course] += 1


        # initialize a queue and res arr that will hold our valid order
        q = deque()
        res = []

        # iterate over range of numCourses, and for each course we check to see if indegrees == 0. this means that course is ready to be processed (has no pre-reqs)
        # append it to queue. 
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        # while our queue is non empty, we pop off the leftmost course and add it to res.
        # then we iterate over the nei of that course (via adj list) and decrement the nei indegrees by 1 (since we js popped off 1 of its pre-reqs)
        # check if any of them now == 0. if so add to queue and repeat this process

        while q:
            course = q.popleft()
            res.append(course)
            for nei in adj[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)


        # check if len(res) < numCOurses. this means theres a cycle so return []

        return [] if len(res) < numCourses else res
        # return res otherwise. 