from pymongo import MongoClient

classdeptlong = []
classdeptshort = []
classnum = []
classdeptshortandnum = []


def main():
    getclassdeptandnum()
    getclassdeptlong()
    getcourseobject()


def getcourseobject():
    uri = 'mongodb://bran:bran123@ds159772.mlab.com:59772/course-organizer-augsburg'
    client = MongoClient(uri)
    db = client.get_database("course-organizer-augsburg")
    apple = list((set(classdeptlong)))
    apple.sort()
    for i, v in enumerate(apple):
        db.departments.insert_one(
        {
            'CourseDepartmentLong': apple[i].replace("\u2013", "-").replace("\n", ""),
            'CourseDepartmentShort': apple[i][:3],
            'CourseNumber': i,
        })

def getclassdeptandnum():
        file = open("Document.txt")
        while True:
            line1 = file.readline()
            if any(str.isdigit(c) for c in (line1[-4:])) and any(str.isalpha(l) for l in (line1[:3])) and len(line1) == 7:
                classdeptshort.append(line1[:3])
                classnum.append(line1[-4:])
                classdeptshortandnum.append(line1.replace("\n", ""))
            if not line1:
                break

def getclassdeptlong():
    for x, dept in enumerate(classdeptshort):
        key = classdeptshort[x] + " "
        with open("Document.txt") as file:
            for num, line in enumerate(file):
                if key in line and " " in line[5:6] and " " in line[3:4]:
                    classdeptlong.append(line)

main()

