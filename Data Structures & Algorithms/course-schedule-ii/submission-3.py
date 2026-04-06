from typing import List

class Solution:

    def check_prereq(self,course, prereq):
        if course not in self.prereq_dict:
            return False
        
        if prereq in self.prereq_dict[course]:
            return True
        
            # check deeper
        for c in self.prereq_dict[course]:
            if self.check_prereq(c, prereq):
                return True
        return False  


    def orderHelper(self,node):
        # if node in self.roots:
        #     return []
        
        if node in self.prereq_dict:
            depend = self.prereq_dict[node]
            order = []
            for n in depend:
                order += self.orderHelper(n)
                order += [n]
            
            return order
        
        else:
            return [node]



    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        all_courses = [i for i in range(numCourses)]
        self.prereq_dict = dict()
        
        for pr in prerequisites:
            course, prereq = pr
            all_courses[course] = -1

            if course == prereq:
                return []
            
            if self.check_prereq(prereq, course):
                return []
            else:
                self.prereq_dict[course] = self.prereq_dict.get(course, []) + [prereq]
        
        self.roots = [i for i in all_courses if i != -1]
        self.visited = [0]*numCourses
        for i in self.roots:
            self.visited[i] = 1

        res = self.roots if len(self.roots) > 0 else []
        queue = list(self.prereq_dict.keys())

        print(self.prereq_dict)

        while queue:
            node = queue.pop()
            if self.visited[node] != 1:
                order = self.orderHelper(node)
                print('order received: ',order)
                order.append(node)
                for o in order:
                    if self.visited[o] != 1:
                        res.append(o)
                        self.visited[o] = 1

        return res