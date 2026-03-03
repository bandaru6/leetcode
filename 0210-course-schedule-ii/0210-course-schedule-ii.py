class Solution: 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        courses = defaultdict(list) 
        for course, prereq in prerequisites: 
            courses[course].append(prereq) 
        
        order = [] 
        visited, cycle = set(), set() 
            
        def dfs(curr): 
            if curr in cycle: 
                return False 
            if curr in visited: 
                return True 
            cycle.add(curr) 
            for prereq in courses[curr]: 
                if dfs(prereq) == False: 
                    return False 
            cycle.remove(curr) 
            visited.add(curr) 
            order.append(curr) 
        
        for num in range(numCourses): 
            depth = dfs(num) 
            if depth == False: 
                return [] 
        
        return order