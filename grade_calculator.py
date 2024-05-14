def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Enter your name")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = int(input("Enter your Math Score: "))
    science_score = int(input("Enter your Science Score: "))
    english_score = int(input("Enter your English Score: "))


    # Calculate the average grade
    # use the PEDMAS order to make sure the grades were added first
    average_grade = (math_score + science_score + english_score) / 3
    

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"Student's name: {student_name}, average grade: {average_grade}")

