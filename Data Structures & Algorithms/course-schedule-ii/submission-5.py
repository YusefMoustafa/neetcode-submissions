from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dfs topological sort

        # want the topological order if theres no cycles. 
        # build a graph represented as an adj list (course: [this course's prereqs])
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)
        # initialize a visiting set (courses we visit per node) and a visited set and a order list that holds the final order. 
        visiting = set()
        visited = set()
        order = []
        # define dfs function that takes a course. 
            # if the course is in the visiting set then we return False
            # if the course is in the visited set then we return True
            # if its in neither, then we add it to both sets. 
            # iterate over that courses neighbors (adj[course]) and run dfs on each neighbor. If it doesnt come back true (meaning its in the visited set) we again return False. 
            # we add course to the order list outside the for loop.
            # remove the course from the visiting set since were done with this dfs run. 
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            order.append(course)
            visiting.remove(course)
            return True

        # now we can iterate over the numCourses to account for any unconnected graphs and check if dfs on each index returns true. if not return []. otherwise we just return the order. 
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order







