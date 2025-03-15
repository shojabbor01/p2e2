# # OOP EXAM

# ## KEEP IN MIND: YOU ARE DOING THIS FOR YOUR BRIGHT FUTURE, SO GIVE YOUR 120%!
# ## ПОМНИТЕ: ВЫ ДЕЛАЕТЕ ЭТО ДЛЯ СВОЕГО СВЕТЛОГО БУДУЩЕГО, ПОЭТОМУ ВЫКЛАДЫВАЙТЕСЬ НА ВСЕ СВОИ 120%!

# ## RULES:
# > No interner, no help to each other!

# > Make one file and place all your work there (e.g. ubaydov_ahmad.py)

# > Send the file in github

# > You have 2 hours only


# # Task 1
# Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.
# Создайте функцию, которая возвращает «верхнюю», если все буквы в слове прописные, «нижнюю», если строчные, и «смешанную» для любого сочетания   этих двух букв.

# getCase("whisper...") ➞ "lower"

# getCase("SHOUT!") ➞ "upper"

# def lower_or_upper(string):
#     if string.isupper():
#         return "upper"
#     elif string.islower():
#         return "lower"
#     else:
#         return "mixed"
# res = lower_or_upper(input())
# print(res)




# # Task 2
# The Fibonacci sequence is defined as follows: φ0=1, φ1=1, φn=φn-1+φn-2 for n>1. The beginning of the Fibonacci series looks like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Write a function int phi(int n) (C/C++), function phi (n:integer ): integer, (Pascal), which, given a natural number n, returns φn.
# Последовательность Фибоначчи определена следующим образом: φ0=1, φ1=1, φn=φn-1+φn-2 при n>1. Начало ряда Фибоначчи выглядит следующим образом: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Напишите функцию int phi(int n) (C/C++), function phi (n:integer): integer, (Pascal), которая по данному натуральному n возвращает φn.
# # input 
# 3
# # output
# 3

# def Fibonacci(num):
#     if num <= 1:
#         return 1
#     else:
#         return Fibonacci(num-1) + Fibonacci(num-2)
# number = int(input())
# res = Fibonacci(number)
# print(res)
    



# # Task 3
# Print the following pattern.(Распечатайте следующий шаблон.)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6
# 7 7 7
# 8 8
# 9

# n = int(input())
# for i in range(1, n//2):
#     for j in range(i):
#         print(i, end=" ")
#     print()
# for i in range(n//2, n+1):
#     for j in range(n-i):
#         print(i, end=" ")
#     print()




# # # Task 4
# # Create a class Employee with a public attribute name, a protected attribute _salary, and a private attribute __id. Demonstrate how these are accessed and restricted.
# # Создайте класс Employee с публичным атрибутом name, защищенным атрибутом _salary и закрытым атрибутом __id. Покажите, как они доступны и ограничены.
# class Employee:
#     def __init__(self, name, salary, id):
#         self.name = name
#         self._salary = salary
#         self.__id = id
#     def my_id(self):
#         return self.__id
#     def my_salary(self):
#         return self._salary
#     def my_name(self):
#         return self.name
# res = Employee("Khayriddin", 10000, 1234)
# print(res.my_id())
# print(res.my_salary())
# print(res.my_name())


        


# # Task 5
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. Use incapsulation methods as well. 
# Напишите программу на Python для создания класса человека. Включите такие атрибуты, как имя, страна и дата рождения. Реализуйте метод определения возраста человека. Также используйте методы инкапсуляции.

# from datetime import date
# class Person:
#     def __init__(self):
#         self.name = "Khayriddin"
#         self._country = "Tajikistan"
#         self.__birthday = 1999
#     def my_name(self):
#         return self.name
#     def my_coumtry(self):
#         return self._country
#     def my_birthday(self):
#         return self.__birthday
#     def my_age(self):
#         today = date.today()
#         return today.year - self.__birthday
# res = Person()
# print(res.my_name())
# print(res.my_coumtry())
# print(res.my_birthday())
# print(res.my_age())
    
    



# ### Task 6: Calculator
# Write a program in Python that asks the user for two numbers and one operation (+, -, *, /). It will then calculate the operation and display the result on the screen.
# 1. Create a public class Calculator.
# 2. Create a constructor that initializes the first number and the second number: __init__(num1, num2).
# 3. Create the following methods in the Calculator class:      
#     * Sum()    
#     * Subtract()            
#     * Multiplication()           
#     * Division()           
# 4. Use a switch block  to call the appropriate methods based on the chosen operation.
# ##
# Напишите программу на Python, которая запрашивает у пользователя два числа и одну операцию (+, -, *, /).  
# Затем она выполнит указанную операцию и отобразит результат на экране. 
# ### Инструкции
# 1. Создайте общедоступный класс Calculator.
# 2. Создайте конструктор, который инициализирует первое число и второе число: __init__(num1, num2).
# 3. Создайте следующие методы в классе Calculator:      
#     * Sum() (Сложение)           
#     * Subtract() (Вычитание)            
#     * Multiplication() (Умножение)          
#     * Division() (Деление)     
# 4. Используйте блок switch чтобы вызывать соответствующие методы на основе выбранной операции.

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def Sum(self):
#         return self.num1 + self.num2
#     def Subtract(self):
#         return self.num1 - self.num2
#     def Multiplication(self):
#         return self.num1 * self.num2
#     def Division(self):
#         return self.num1 // self.num2
# num1 = int(input())
# num2 = int(input())
# char = input()
# res1 = Calculator(num1, num2)
# if char == "+":
#     res2 = res1.Sum()
# elif char == "-":
#     res2 = res1.Subtract()
# elif char == "*":
#     res2 = res1.Multiplication()
# elif char == "//":
#     res2 = res1.Division()
# else:
#     print("amali nodurust")
# print(res2)
    



# Task 7
# Create a class BankAccount with private attributes __balance and __pin.
# Initialize the values in the constructor.
# Access the __balance directly and see what happens when you try to access __balance or __pin.

# Создайте класс BankAccount с приватными атрибутами __balance и __pin.
# Инициализируйте значения в конструкторе.
# Получите доступ к __balance напрямую и посмотрите, что произойдет, когда вы попытаетесь получить доступ к __balance или __pin.

# In the same BankAccount class, define a setter method to update the private attribute _balance.
# Ensure that balance can’t be negative by checking in the setter.
# В том же классе BankAccount определите метод-сеттер для обновления частного атрибута _balance.
# Убедитесь, что баланс не может быть отрицательным, проверив в сеттере.

# class BankAccount:
#     def __init__(self, balance, pin):
#         self.__balance = balance
#         self.__pin = pin 
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self, new_balance):
#         if new_balance <= 0:
#             print("u vas ne dostatochno sredstv dlya soversheniya vizova :)")
#         else:
#             self.__balance = new_balance
# res = BankAccount(10000, 1234)
# res.set_balance(3000)
# print(res.get_balance())






# # Task 8
# Create a base class Animal with a method speak().
# Create a derived class Dog that overrides speak().
# Further, derive a class Puppy from Dog and override the speak() method again.
# Call the speak() method from a Puppy object.
# Создайте базовый класс Animal с методом speak().
# Создайте производный класс Dog, который переопределяет speak().
# Далее, выведите класс Puppy из Dog и снова переопределите метод speak().
# Вызовите метод speak() из объекта Puppy.

# class Animal:
#     def __init__(self):
#         pass
#     def speak(self):
#         print("govorit sobaka") 
# class Dog(Animal):
#     def speak(self):
#         print("sobaka perestal govorit")
# class Puppy(Dog):
#     def speak(self):
#         print("sobaka snova nachal govorit")
# res = Puppy()
# print(res.speak())
    
            


# # Task 9
# Build a Nobel class. An instance is already created for you and instance attributes are included inside the print. Take those clues and try to reverse engineer the class.  Implement string representation of a class object using str method inside the class.

# Создайте Nobel класс. Экземпляр уже создан для вас, и атрибуты экземпляра включены в результат print. Воспользуйтесь этими подсказками и попытайтесь спроектировать класс. Реализуйте строковое представление объекта класса, используя метод str внутри класса.
# ```
# class Nobel:
#     pass

# np2005=Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)
# ```

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def __str__(self):
#         return f"{self.year} {self.category} {self.winner}"
# np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005.category, np2005.year, np2005.winner)




# # Task 10
# Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest ice cream. Note that there is a class provided for you in the Tests tab.
# Each sprinkle has a sweetness value of 1
# Check below for the sweetness values of the different flavors.
# Создайте функцию, которая берет список объектов класса IceCream и возвращает значение сладости самого сладкого мороженого. Обратите внимание, что на вкладке «Тесты» вам предоставлен класс.
# Каждая посыпка имеет показатель сладости 1.
# Ниже приведены значения сладости различных вкусов.
 
# class IceCream:
#     def init(self, flavor, num_sprinkles):
#         self.flavor = flavor
#         self.num_sprinkles = num_sprinkles

#  Flavors         |Sweetness Value    |
#  -------------------|-------------------|
#  Plain             |   0               |
#  Vanilla         |   5               |
#  ChocolateChip     |   5               |
#  Strawberry         |   10              |
#  Chocolate         |   10              |   
#  ---------------------------------------|
 
# ice1 = IceCream("Chocolate", 13)         # value of 23
# ice2 = IceCream("Vanilla", 0)           # value of 5

# sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
# sweetest_icecream([ice3, ice1]) ➞ 23