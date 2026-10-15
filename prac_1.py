# A PROGRAM THA CONTINUOSLY ACCEPTS STUDENT NAMES UNTIL THE LIBRARIAN  CLOSES THE SYSTEM, PRINTS A FINAL COUNT 
# UCU Library Attendance Tracker
# sequence: setting up an initial state before the main logic begins
attendance = []
system_running = True
print ("welcome to the Hamu Mukasa library Attendance system")
print("Type quit to exit and generate the final report.\n")

# ITERATION: A while loop keeps the program running until a condition changes
while system_running:

    # capturing user input
    student_name = input("Enter student name or ID(or type 'quit'):").strip()

# Selection: Decisions pathway based on the input provide
    if student_name.lower() == 'quit':
        # changes the state to end the loop
        system_running = False

    elif student_name == "":
        # edge case hanling: user just pressed enter

        print("Error: Name cannot be blank. Please enter name")
    elif student_name in attendance:
        print(f"Notice: {student_name} is already signed in!.\n")

    else:
        attendance.append(student_name)
        print(f"Success: {student_name} has already been signed in")
print("\n" + "="*30)   
print("FINAL ATTENDANCE REPORT")
print("="*30) 
print(f"Total students in the library: {len(attendance)}")
for index, student in enumerate(attendance,start=1):
    print(f" {index}. {student}")