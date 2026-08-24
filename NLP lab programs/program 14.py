subject = input("Enter subject (He/They): ")
verb = input("Enter verb (runs/run): ")

if (subject == "He" and verb == "runs") or \
   (subject == "They" and verb == "run"):
    print("Sentence is Correct")
else:
    print("Subject-Verb Agreement Error")