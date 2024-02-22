print("Hello World")

print("Hello Git")

message = "Hello world!"

name = "Hanna"
hello_string = f"Hello, {name}!"
print(hello_string)

n = 5000

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

a = input("Сьогодні буде гарний день: ")
# На екрані ви побачите: Сьогодні буде гарний день:

a = 6
P = 4 * a
print(f"Периметр квадрата дорівнює {P}")

my_list = list() #списки
empty_list = []
my_list = [1, 2, 3, 4, 5]
my_list.append(4) #додавання
my_list.remove("Hello") #видалення

some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
last_letter = some_iterable[2] #можливість доступу за індексом

chars = ['a', 'b', 'c']
last = chars.pop(1) #видалення за індексом

chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers) #розширити один список іншим

chars = ["a", "c"]
chars.insert(1, "b") #Для вставки елемента x на позицію з індексом i у список

chars = ['a', 'b']
chars.clear() # [] #Для очищення списку від елементів

chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c') #знаходження індексу першого входження заданого елемента у списку

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) #кількість елементів у колекції

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort() #сортування за зростанням
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]
nums.sort(reverse=True) #сортування за спаданням
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]
words = ["banana", "apple", "cherry"]
words.sort(key=len) #сортування за кількістю букв
print(words)  # Виведе ['apple', 'banana', 'cherry']

#теж саме з sorted() сортує не змінюючи список, використовують з будь-якою коллекцією

chars =  ['a', 'b']
chars_copy = chars.copy() #Щоб повернути копію списку

chars = ["banana", "apple", "cherry"]
chars.reverse() #зворотній порядок елементів

my_dict = {"name": "Alice", "age": 25, "city": "New York"} #створення словника

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice' #доступ за ключем
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

del my_dict["age"] #видалення за ключем
print(my_dict)

print("name" in my_dict) #Для перевірки, чи є ключ у словнику
print("age" in my_dict)

my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Поверне 25 #отримання значення за ключем
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику

empty_set = set() #порожня множина
a = set('hello')
b = {1, 2, 3, 4, 5}  #методи створення заповненої множини

lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
d_lst = set(lst) #перетворити список на множину
lst=list(d_lst) #перетворити множину на список

numbers = {1, 2, 3}
numbers.add(4) #додає елемент
print(numbers)  # {1, 2, 3, 4}

numbers = {1, 2, 3}
numbers.remove(3) #видаляє з вийнятком
print(numbers)  # {1, 2}

numbers = {1, 2, 3}
numbers.discard(2) #видаляє без вийнятка
print(numbers)  # {1, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3} #перетини у множинах
print(a & b)  # {3}

print(a.difference(b))  # {1, 2} #різниця між множинами
print(a - b)  # {1, 2}

print(a.symmetric_difference(b))  # {1, 2, 4, 5} #Симетрична різниця між двома множинами включає всі елементи, які містяться в одній множині, але не містяться в іншій, і навпаки
print(a ^ b)  # {1, 2, 4, 5}

print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}  # {1, 2, 4, 5} #Об'єднання двох множин включає всі елементи з обох множин, але без дублікатів

my_frozenset = frozenset([1, 2, 3, 4, 5]) #після створення замороженої множини ви не можете додати або видалити елементи з неї
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})
#результатом кожної операції буде нова заморожена множина

#порожні кортежі
my_tuple = tuple() # або
my_tuple = ()

#заповнені кортежі
my_tuple = (1, 2, 3)
my_tuple = (1, "Hello", 3.14)
my_tuple = 1, "Hello", 3.14 #упакування кортежу

first_item = my_tuple[0]  # Отримати перший елемент

points = {
    (0, 0): "O"
    (1, 1): "A"
    (2, 2): "B"
} #використовувати як ключі у словнику

#методи рядків
game_string = 'My favorite "Game"'
s = "Hello world!"
print(s[0])# H
print(s[-1])# !впорядкована послідовність
s = "Hello world!"
s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError Незмінна послідовність

s = "Hello" 
print(s.upper()) # Виведе 'HELLO' усі літери рядка перевести у верхній регістр

s = "Some Text"
print(s.lower())  # Виведе 'some text' переведення в нижній регістр

s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True перевірити, що рядок починається з підрядка

s = "hello.jpg"
print(s.endswith("jpg"))  # Виведе True перевірити, що рядок закінчується підрядком

s = "hello world".capitalize()  # Результат: "Hello world" перший символ рядка великою літерою, а інші — малими

s = "hello world".title()  # Результат: "Hello World" перетворює перші літери кожного слова в рядку на великі

"123".isdigit()  # True чи складається рядок тільки з цифр
"hello".isalpha()  # True чи складається рядок тільки з літер
" ".isspace()  # True чи складається рядок тільки з пробілів

#Форматування рядків

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))

#Зрізи у Python (Slice) послідовність[початок:кінець:крок]

s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Виведе 'Hello'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2] 
odd_numbers = numbers[::2]  # Виведе [1, 3, 5, 7, 9] #непарні числа списку за допомогою зрізів

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1:10:2]
even_numbers = numbers[1::2] # Виведе [2, 4, 6, 8, 10] #парні числа зі списку за допомогою зрізів

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = numbers[2:10:3]
three_numbers = numbers[2::3] #отримаємо числа списку, кратні трьом

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers) #буде зберігати зворотний список

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print(copy_numbers) #зробити копію списку в Python

































