# # names =["sam", "john", "james"]
# # map_of_names = map(len,names)
# # print(list(map_of_names))

# # len_of_names=[]
# # for name in names:
# #     len_of_names.append(str.upper(name))
    
# # print(len_of_names)

# ages=[15,29,30,45]
# age_Checker = list(map((lambda age:age >=18),ages))
# print(age_Checker)



# # age_Check =[]
# # for age in ages:
# #     check = Voting_Age(age)
# #     age_Check.append(check)
# # print(age_Check)

# # map_of_ages= filter(Voting_Age,ages)
# # print(list(map_of_ages))

# items=[3,2]
# square = map((lambda x: x**2),items)
# print(list(square))
# ##A FUNCTION FROM LABS
# number = int(input("Please enter number and lets check if it is even :")) 
# even_Numbers=[1,56,234,87,4,76,24,69,90,135]
# def is_even(num):
#     return num % 2 != 0

# print(is_even(number))

# squares= list(map((lambda num :num % 2),even_Numbers))
# print(squares)
##oop
class person:
    def __init__(self,name:str,DoB:str):
        self.name = name
        self.Dob = DoB
    def speak(self):
        print("Hello")

    def walk(self):
        print('Walking away')

person1 = person("Angela","Acquah")
person1.speak()
person1.walk()

class Age:
    def __init__(self,value):
        self._value = value
    @property
    def value(self):
        return self._value
Age2 = Age(20)
print(Age2.value)