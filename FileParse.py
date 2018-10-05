from pymongo import MongoClient
classdeptshort = []
classnum = []
classdeptshortandnum = []
classtitle = []
classcredits = []
classdesc = []
classcore = []
classprereq = []
classdeptlong = []
classobject = []
classid = []

def main():
    getclassdeptandnum()
    getclasstitleandcredits()
    getclassdescandcoreandprereq()
    getclassdeptlong()
    getclassprereq()
    print(classprereq)

def getcourseobject():
    uri = 'mongodb://bran:bran123@ds159772.mlab.com:59772/course-organizer-augsburg'
    client = MongoClient(uri)
    db = client.get_database("course-organizer-augsburg")

    for i, v in enumerate(classdeptshort):
        db.courses.insert_one(
        {
            'CourseDepartmentLong': classdeptlong[i],
            'CourseDepartmentShort': classdeptshort[i],
            'CourseNumber': classnum[i],
            'CourseTitle': classtitle[i],
            'CourseCredit': classcredits[i],
            'CourseDescription': classdesc[i],
            'CourseCore': classcore[i],
            'CoursePrerequisite': classprereq[i],
            'CourseID': classid[i],
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


def getclasstitleandcredits():
        for x, dept in enumerate(classdeptshort):
            classdeptnum = classdeptshort[x] + classnum[x]
            with open("Document.txt") as file:
                for num, line in enumerate(file):
                    if classdeptnum in line:
                        lines = open("Document.txt").readlines()
                        classtitle.append(lines[num+1])
                        classcredits.append(lines[num+2])


def getclassdescandcoreandprereq():
    for z, dept3 in enumerate(classdeptshort):
        classid.append(z)
    for x, dept in enumerate(classdeptshort):
        classdeptnum = classdeptshort[x] + classnum[x]
        with open("Document.txt") as file:
            for num, line in enumerate(file):
                if classdeptnum in line:
                    lines = open("Document.txt").readlines()
                    i = num + 3
                    desc = ""
                    while "Core Curriculum Component:" not in lines[i]:
                        if len(lines[i]) == 2:
                            desc += ""
                            i += 1
                        else:
                            desc += lines[i]
                            i += 1
                    classdesc.append(desc)
                    classcore.append(lines[i])
                    classprereq.append(lines[i+1])


def getclassdeptlong():
    for x, dept in enumerate(classdeptshort):
        key = classdeptshort[x] + " "
        with open("Document.txt") as file:
            for num, line in enumerate(file):
                if key in line and " " in line[5:6] and " " in line[3:4]:
                    classdeptlong.append(line)


def getclassprereq():
    for x, dept in enumerate(classprereq):
        classid.append(x)
    for x, dept in enumerate(classprereq):
        temp = []
        string = str(classprereq[x])
        if string.find("None") == -1 and len(string) > 4:
            array = string.replace("Prerequisite", "").replace("(", " ").split()
            for tempstring in array:
                if any(str.isdigit(c) for c in (tempstring[-4:])) and any(str.isalpha(l) for l in (tempstring[:3])) and len(tempstring) >= 6:
                    temp.append(tempstring)
                    for course in temp:
                        try:
                            id = classdeptshortandnum.index(course)
                            temp.remove(course)
                            temp.append(id)
                        except ValueError:
                            print("Could Not Determine Course")
                print(temp)


main()
