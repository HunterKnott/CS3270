'''Hunter Knott, Utah Valley University, CS 2420'''

class CourseList:
    '''A doubly-linked list that stores Course objects'''
    def __init__(self):
        '''Initializes the list head and tail pointers'''
        self.head = None
        self.tail = None

    def append(self, new_course):
        '''Inserts a new course at the end of the list'''
        if self.head is None:
            self.head = new_course
            self.tail = new_course
        else:
            self.tail.next = new_course
            new_course.prev = self.tail
            self.tail = new_course

    def insert(self, new_course):
        '''Inserts a new course of a given number in ascending order'''
        if self.head is None:
            #New course is the first in the list
            self.head = new_course
            self.tail = new_course
            self.head.prev = None

        elif new_course.course_number < self.head.course_number:
            #New course is lowest in the list
            new_course.prev = None
            self.head.prev = new_course
            new_course.next = self.head
            self.head = new_course

        elif new_course.course_number > self.tail.course_number:
            #New course is highest in the list
            new_course.prev = self.tail
            self.tail.next = new_course
            self.tail = new_course

        else:
            #New course is between list elements
            cur_course = self.head
            while cur_course.course_number < new_course.course_number:
                cur_course = cur_course.next
            cur_course.prev.next = new_course
            new_course.prev = cur_course.prev
            cur_course.prev = new_course
            new_course.next = cur_course

    def remove(self, number):
        '''Removes the first occurance of a given course number'''
        prev_course = self.find(number).prev
        next_course = self.find(number).next

        if next_course is not None:
            next_course.prev = prev_course

        if prev_course is not None:
            prev_course.next = next_course

        if number is self.head:
            self.head = next_course

        if number is self.tail:
            self.tail = prev_course

    def remove_all(self, number):
        '''Removes all courses of a given course number'''
        cur_course = self.head
        while cur_course:
            if number == cur_course.number():
                self.remove(number)
            cur_course = cur_course.next

    def find(self, number):
        '''Returns the first course with the given course number,and -1 if it doesn't exist'''
        cur_course = self.head
        while cur_course:
            if number == cur_course.number():
                return cur_course
            cur_course = cur_course.next
        return -1

    def size(self):
        '''Returns the number of courses in the list'''
        course_count = 0
        cur_course = self.head
        while cur_course:
            course_count += 1
            cur_course = cur_course.next
        return course_count

    def calculate_gpa(self):
        '''Returns the average of the course grades'''
        average_gpa = 0
        if self.size() == 0:
            return average_gpa
        cur_course = self.head
        while cur_course:
            average_gpa += cur_course.grade()
            cur_course = cur_course.next
        average_gpa = average_gpa / float(self.size())
        return average_gpa

    def is_sorted(self):
        '''Returns True if the list is sorted by course number, and False if it isn't'''
        if self.head is None:
            return True
        cur_course = self.head
        while cur_course.next:
            if cur_course.number() > cur_course.next.number():
                return False
            cur_course = cur_course.next
        return True

    def __str__(self):
        '''Returns a string of all courses in course list'''
        list_string = ""
        cur_course = self.head
        while cur_course:
            list_string += cur_course.__str__() + "\n"
            cur_course = cur_course.next
        return list_string

    def __iter__(self):
        '''Makes the course list iterable'''
        self.current_node = self.head
        return self

    def __next__(self):
        '''Returns next course in the course list'''
        if self.current_node is None:
            raise StopIteration
        course = self.current_node
        self.current_node = self.current_node.next
        return course
