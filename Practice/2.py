def calc_Grade(percentage):
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
Student_Percentage = int(input('Enter Student Percentage : '))
Student_Grade = calc_Grade(Student_Percentage)
print(f'Student has {Student_Percentage}% and got grade {Student_Grade}')