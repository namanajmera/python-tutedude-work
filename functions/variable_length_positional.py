def student_details(sname, sid, *args):
    if len(args) == 0:
        print(f"Sorry, Student {sid}-{sname} failed...!!!")
    else:
        percent = sum(args) / len(args)
        print(f"Student {sid}-{sname} has {percent:.2f}% of the data")

student_details("Naman", "S01", 89,87,99,100,86)
student_details("Test", "S02")