#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:

        def __init__(self, name, gpa, student_id):
            self.name = name
            self.gpa = gpa
            self.student_id = student_id

    def is_eligible_for_honors(student):
        if student.gpa > 3.5:
            return True
        else:
            return False

    def check_free_lunch_winner(student, generated_id):
        if student.student_id == generated_id:
            print(f"Winner! {student.name} gets free lunch!")
        else:
            print("Loser!")


    student1 = Student(name="tobi akinde", gpa=3.8, student_id="123456")


    honors_eligibility = is_eligible_for_honors(student1)
    print(f"{student1.name}is eligible for honors:{honors_eligibility}")


    generated_id = str(random.randint(100000, 999999))

    # Checking for free lunch winner
    check_free_lunch_winner(student1, generated_id)
    
    
    
    
def main():
    #create three students and check if they get free lunch and if they qualify for honors
    
    
main()
