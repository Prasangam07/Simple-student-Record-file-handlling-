#Project: Simple student Record (file handlling)

def add_student():
  name = input("Enter student name: ")
  roll = input("Enter student-rollno: ")
  marks = input("Enter marks: ")

  with open("Students.txt","a") as f:
    f.write(roll + ","+name +"," +marks +"\n")

  print("student addes successfulll!!!!\n")  

def View_student():
  try:
    with open("students.txt","r") as f:
      data = f.readlines()
      
      if not data:
        print("No records found.\n")
        return
      print("\n--- student record ---")
      for line in data:
        roll,name,marks = line.strip().split(",")
        print("roll:",roll,"name:",name,"marks:",marks)
      print()
  except FileNotFoundError:      
    print("File not found.\n")
      

while True:
  print("1.Add student")
  print("2.View students")
  print("3.exit")
  choice = input("Enter your choice:")

  if choice =="1":
    add_student()
  elif choice == "2":
    View_student()
  elif choice == "3":
    print("See you later!!")
    break
  else:
    print("Invalied choice")    
  
