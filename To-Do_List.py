import random
skills=[]
quotes=[ "'The secret of getting ahead is getting started.' – Mark Twain",
    "'Don't watch the clock; do what it does. Keep going.' – Sam Levenson",
    "'It always seems impossible until it’s done.' – Nelson Mandela",
    "'Small daily improvements are the key to staggering long-term results.' – Unknown",
    "'You don’t have to be great to start, but you have to start to be great.' – Zig Ziglar",
    "'The way to get started is to quit talking and begin doing.' – Walt Disney"]
def motivation():
  return random.choice(quotes)
def addSkill():
  skillName=input("Enter The Skill to learn:")
  priority=input("Enter the priorrity(High/Medium/Low):")
  deadline=input("Enter the deadline in days:")

  skill={"name":skillName, "priority":priority,"deadline":deadline, "status":"Pending"}
  skills.append(skill)

  print(f"Skill'{skillName}' added succesfully!")
  print(motivation())

def showSkill():
  if not skills:
    print("No skill Avalable")
  else:
    print("YOUR SKILLS:")
    for i, skill in enumerate(skills,1):
      print(f"{i}.{skill['name']}| priority:{skill['priority']}| Deadline:{skill["deadline"]}|Status:{skill['status']}")
  print(motivation())

def deleteSkill():
    if not skills:
      print("No skill to delete.")
      return
    showSkill()
    skillName=input("Enter the skill name to delete:")

    for skill in skills:
      if skill["name"].lower()==skillName.lower():
        skills.remove(skill)
        print(f"Skill'{skillName}' deleted succesfully!")
        print(motivation())
        return
      
    print("Task not found!")

def main():
    while True:
        print("\n1. Add Skill\n2. Show Skills\n3. Delete Skill\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            addSkill()
        elif choice == "2":
            showSkill()
        elif choice == "3":
            deleteSkill()
        elif choice == "4":
            print("Exiting Skill Tracker, Goodbye!")
            print("'Believe you can and you’re halfway there.' – Theodore Roosevelt")
            break
        else:
            print("Invalid choice. Please retry.")

if __name__ == "__main__":
    main()
