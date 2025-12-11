def student_details(sname, sid, *args, **kwargs):
    if len(kwargs) == 0:
        print(f"Sorry, Student {sid}-{sname} failed...!!!")
    else:
        percent = sum(kwargs.values()) / len(kwargs)
        print(f"Student {sid}-{sname} has {percent:.2f}% of the data")

student_details("Naman", "S01", "football", "tennis", sub_1 = 100, sub_2 = 99)
student_details("Test", "S02")