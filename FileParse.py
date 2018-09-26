from pymongo import MongoClient
classdeptshort = []
classnum = []
classtitle = []
classcredits = []
classdesc = []
classcore = []
classprereq = []
classdeptlong = []
classobject = []

def main():
    getcourseobject()



def getcourseobject():
    uri = 'mongodb://bran:bran123@ds159772.mlab.com:59772/course-organizer-augsburg'
    client = MongoClient(uri)
    db = client['course-organizer-augsburg']
    collection = db.courses

    for i in enumerate(classdeptshort):
        try:
            db.courses.insert_one(
            {
                'CourseDepartmentLong': classdeptlong[i],
                'CourseDepartmentShort': classdeptshort[i],
                'CourseNumber': classnum[i],
                'CourseTitle': classtitle[i],
                'CourseCredit': classcore[i],
                'CourseDescription': classdesc[i],
                'CourseCore': classcore[i],
                'CoursePrerequisite': classprereq[i],
            }
            )
        except Exception, e:
            print str(e)


def getclassdeptandnum():
        file = open("Document.txt")
        while True:
            line1 = file.readline()
            if any(str.isdigit(c) for c in (line1[-4:])) and any(str.isalpha(l) for l in (line1[:3])) and len(line1) == 7:
                classdeptshort.append(line1[:3])
                classnum.append(line1[-4:])
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

def connectToMongo():
    uri = 'mongodb://bran:bran123@ds159772.mlab.com:59772/course-organizer-augsburg'
    client = MongoClient(uri)
    db = client['course-organizer-augsburg']
    collection = db.courses


main()
