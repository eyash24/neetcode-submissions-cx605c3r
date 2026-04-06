class Solution:
    def check_prereq(self, course, prereq):
        if course not in self.prereq_pointer.keys():
            return False

        if prereq in self.prereq_pointer[course]:
            return True
        
        # check deeper
        depends_on = self.prereq_pointer[course]
        for c in depends_on:
            if self.check_prereq(c, prereq):
                return True
        
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.prereq_pointer = dict()

        for pr in prerequisites:
            print(self.prereq_pointer)
            course, prereq = pr
            if course == prereq:
                return False
            print(f'course: {course}, prepreq: {prereq}')
            if self.check_prereq(prereq, course):
                return False
            else:
                self.prereq_pointer[course] = self.prereq_pointer.get(course, []) + [prereq]
        
        return True
