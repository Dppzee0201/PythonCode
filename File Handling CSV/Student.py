class student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no= roll_no

    def add_marks(self,marks,subject):
        self.marks= marks
        self.subject= subject

    # def get_average(self,marks):
    #     average= (marks/100)*100
    #     print(average)

Std1=student('Deep',120014)
Std1.add_marks(85,'Python')
Std1.add_marks(80,'Data Science')
Std1.add_marks(90,'Ml')



