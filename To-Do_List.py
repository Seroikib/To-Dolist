import json
import random
quotes=[
  "Code is like humor. When you have to explain it, it’s bad.",
    "Programming isn't about what you know; it’s about what you can figure out.",
    "The only way to learn a new programming language is by writing programs in it.",
    "Simplicity is the soul of efficiency."
]
try:
  with open("tasks.json","r") as file:
    tasks=json.load(file)
except FileNotFoundError:
  tasks=[]
def addSkill():
  skill=input("Enter The Skill You Want To Learn: ")
  priority=input("Priority(High/Medium/Low): ")
  deadline=input("Set A Deadline In Days: ")
  tasks.append({"skill":skill,"status":"pending","priority":priority,"deadline":deadline})
  save_tasks()
  print(f"Task'{skill}'Added Successfully!!")
def completeSkill():
  show_tasks()
  skill_name=input("Enter the skill you want to complete:")
  for task in tasks:
    if task["skill"].lower()==skill_name.lower():
      task["status"]="completed"
      save_tasks()
      print(f"Congrats! You Have completed '{task['skill']}'")
      return
  print("Skill Not Found!")

def deleteSkill():
    show_tasks()
    skill_name=input("Enter the skill you want to delete")
    global tasks
    tasks=[task for task in tasks if task["skill"].lower() !=skill_name.lower()]
    save_tasks()
    print(f"'{skill_name}' has been deleted.")
    
def show_tasks():
    if not tasks:
      print("No Skills Added Yet.")
      return
    #print("Debugging tasks:", tasks)
    print("Your Tech Learning Tasks:")
    for task in tasks:
      print(f"{task['skill']} | Status:{task['status']} | Priority:{task['priority']} | Deadline:{task['deadline']}")
def save_tasks():
    with open("tasks.json","w" )as file:
      json.dump(tasks,file,indent=4)
def showMotivation():
    print(f"Today's Motivation:{random.choice(quotes)}")
def main():
    while True:
      showMotivation()
      print("Tech Skill Tracker")
      print("1 Add Skill")
      print("2 Mark as Completed")
      print("3 Remove Skill")
      print("4 Show Tasks")
      print("5 Exit")
      choice=input("Select an option: ")
      if choice=="1":
        addSkill()
      elif choice=="2":
        completeSkill()
      elif choice=="3":
        deleteSkill()
      elif choice=="4":
        show_tasks()
      elif choice=="5":
        print("Keep Learning  & Coding,, Goodbye!!")
        break
      else:
        print("Invalid Choice. Try Again.")

if __name__=="__main__":
    main()
      
