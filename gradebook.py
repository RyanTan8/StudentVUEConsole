from collections import OrderedDict
from studentvue import StudentVue
#sv = StudentVue("1222188", "clonetrooper123", 'studentvue.cobbk12.org') 
def login():
    print("Enter Credentials: ")
    username = "1222188"# Your StudentVUE username
    password = "clonetrooper123" # Your StudentVUE password
    domain = "studentvue.cobbk12.org" # Your StudentVUE district's domain
    return StudentVue(username, password, domain)
sv = login()


print(sv.get_student_info())
print(sv.get_gradebook())

