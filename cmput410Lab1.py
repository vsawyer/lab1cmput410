class Student:
    courseMarks = {}
    name = ""
    family = ""
    def __init__(self,name,family):
        self.name = name
        self.family = family
        self.courseMarks[] = courseMarks

    def addCourseMark(self,course,mark):
        self.courseMarks[course] = mark
        
    def average(self):
        avg = sum(self.courseMarks.values())/len(self.courseMarks)
        print(avg)
        
Val = Student('Valerie', 'Sawyer')
Val.addCourseMark('math',80.0)
Val.addCourseMark('science',70.0)
Val.average()
