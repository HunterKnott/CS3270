'''Hunter Knott, Utah Valley University, CS 2420'''
from course import Course
from courselist import CourseList

def main():
    '''Reads text data to a doubly linked list'''
    courses = CourseList()
    with open("data.txt") as file:
        while True:
            line = file.readline()
            line_entries = line.split(",")
            if not line:
                break
            new_course = Course(int(line_entries[0]), line_entries[1], float(line_entries[2]), float(line_entries[3]))
            courses.insert(new_course)
        print(courses)

if __name__ == '__main__':
    main()
