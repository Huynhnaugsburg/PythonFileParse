def main():
    file = open("Document.txt", "r")
    while True:
        line = file.readline()
        if " - " in line:
            departmentname = line
            print(departmentname)
            deptshort = departmentname[:3]
            getcoursenumber(deptshort)
        if not line:
            break
    file.close()


def getcoursenumber(dept):
    file = open("Document.txt")
    while True:
        line2 = file.readline()
        if dept in line2 and " - " not in line2 and len(line2) == 7:
            print(line2)
            CourseName = file.readline()
            print(CourseName)
            description = ""
            check = True
            while check:
                line3 = file.readline()
                if "Core Curriculum Component" in line3:
                    Core = line3
                    check = False
                else:
                    description += line3
            print(description)

            check2 = True
            while check2:
                line4 = file.readline()
                if "Prerequisite(s):" in line4:
                    Prereq = line4
                    check2 = False
            print(Core)
            print(Prereq)
        if not line2:
            break


main()

