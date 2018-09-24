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
            if not line2:
                break
main()