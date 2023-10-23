'''Hunter Knott, Utah Valley University, CS 2420'''

class Course:
    '''Stores information for a CS course'''
    def __init__(self, number=0, name="", credits=0.0, grade=0.0):
        '''Validates course object parameters and initializes course attributes'''
        if not isinstance(number, int):
            raise ValueError("Course Number should be an integer value")
        if not isinstance(name, str):
            raise ValueError("Course name should be a string value")
        if not isinstance(credits, float):
            raise ValueError("Course credit hours should be a decimal value")
        if not isinstance(grade, float):
            raise ValueError("Course grade should be a decimal value")
        if number < 0:
            raise ValueError("Course number should be a positive")
        if credits < 0:
            raise ValueError("Course credit hours should be a positive number")
        if grade < 0 or grade > 4:
            raise ValueError("Course grade should be a number between 0 and 4")

        self.course_number = number
        self.course_name = name
        self.credit_hrs = credits
        self.course_grade = grade
        self.next = None
        self.prev = None

    def __str__(self):
        '''Returns a string representation of the course object'''
        return f'cs{self.course_number} {self.course_name} Grade:{self.course_grade} Credit Hours:{self.credit_hrs}'

    def number(self):
        '''Getter method for course number'''
        return self.course_number

    def name(self):
        '''Getter method for course name'''
        return self.course_name

    def credit_hr(self):
        '''Getter method for credit hours'''
        return self.credit_hrs

    def grade(self):
        '''Getter method for course grade'''
        return self.course_grade
