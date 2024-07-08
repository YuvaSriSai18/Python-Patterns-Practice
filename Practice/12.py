class student():
    def __init__(self,id,Mid_1_Marks,Mid_2_Marks,Quiz_Marks) -> None:
        student.ID = id
        student.M1_marks = Mid_1_Marks
        student.M2_marks = Mid_2_Marks
        student.quiz_marks = Quiz_Marks
    
    def grade(percentage):
        if(percentage >= 90):
            return 'A' 
        elif(percentage >= 80):
            return 'B'
        elif(percentage >= 70):
            return 'C'
        elif(percentage >= 60):
            return 'D'
        elif(percentage >= 40 and percentage < 60):
            return 'E'
        else:
            return 'F'
    
    
    def Mark_list(self,Name,Roll_No):
        print(f'Roll Number : {Roll_No}')
        print(f'Name : {Name}')
        print(f'MID-1 Marks : {student.M1_marks}')
        print(f'MID-2 Marks : {student.M2_marks}')
        print(f'Quiz Marks : {student.quiz_marks}')
        print(f'Total Marks : {student.M1_marks + student.M2_marks + student.quiz_marks}' )
        print(f'Grade : {student.grade(student.M1_marks + student.M2_marks + student.quiz_marks)}')
obj1 = student(750,15,15,5)
print(obj1.Mark_list("Yuva Sri Sai" , 750))