import functools


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks)/len(self.marks)
    #this won't work for WorkingStudent object as WorkingStudent class
    # does not have any friend method
    '''
    def friend(self,friend_name):
        return Student(friend_name,self.school)
    '''
    @classmethod
    def friend(cls,origin,friend_name,salary):
        return cls(friend_name,origin.school,salary)


class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary



anna = WorkingStudent("anna", "oxford", 20)
print(anna.salary)
#works before when only student class exists
#friend = anna.friend('greg')
friend = WorkingStudent.friend(anna,'greg',16)
print (friend.name)
print (friend.school)
print(friend.salary)

#--------------------------------------------------------------------
#initializing variable while passing
def meth(name,location):
    print(name)
    print(location)
a = 'UK'
b = 'Jose'
#meth(a,b)
meth(location='UK', name='Jose')

#----------------------------------------------------------------
# *args will be a tuple and can take any number of arguments
# **kwargs(key word arguments) is a set or a dict and can take any number of key/value pairs

def what_is_args_kwards(*args,**kwargs):
    print (args)
    print(kwargs)
what_is_args_kwards(4,5,6,7,name='Vivek',Location='Somewhere')
what_is_args_kwards(6,3,6,7,'yello','yello','hello')
#----------------------------------------------------------------------
#passing functions as parameters
def method_passing(another):
    return another()
def some_method():
    return 3+5
print(method_passing(some_method))
print(method_passing(lambda: 3+5))
#filters and lambda and filter and function and list comprehension
my_list = [13,5,6,964]
def not_thirteen(x):
    return x!=13
print(list(filter(not_thirteen,my_list)))
print(list(filter(lambda x: x!=13,my_list)))
print([x for x in my_list if x!=13])
#----------------------------------------------------------------------
#decorators in python
#import functools
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("i'm the decorator")
        func()
        print('after the decorator')
    return function_that_runs_func
@my_decorator
def my_func():
    print("i'm the function")
my_func()

# Advanced decorators
def decorator_with_arguments(number):
    def other_decorator(func):
        @functools.wraps(func)
        def func_that_runs_func(*args,**kwargs):
            print("in the decorator")
            if(number==1):
                print("not running func")
            else:
                func(*args,**kwargs)
            print("after the decorator")
        return func_that_runs_func
    return other_decorator

@decorator_with_arguments(40)
def my_function_2(x,y):
    print(x+y)
my_function_2(5,5)
