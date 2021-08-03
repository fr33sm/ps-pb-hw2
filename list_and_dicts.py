import os

# Чистим экран перед стартом программы
def clear_screen():
    os.system('clear' if os.name =='posix' else 'cls')
clear_screen()



# Подготовка, п.1. Создать 4 переменные account1, account2, account3, account4 типа словарь со структурой “account”. Значения ключей для переменных:
# account1: login - ivan, password - q1;
account1 = {'login': 'ivan', 'password': 'q1'}
# account2: login - petr, password - q2;
account2 = {'login': 'petr', 'password': 'q2'}
# account3: login - olga, password - q3;
account3 = {'login': 'olga', 'password': 'q3'}
# account4: login - anna, password - q4.
account4 = {'login': 'anna', 'password': 'q4'}



# Подготовка, п.2. Создать 4 переменные user1...user4 типа словарь со структурой “user”. Значения ключей для переменных:
# user1: name - Иван, age - 20, account - account1;
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
# user2: name - Петр, age - 25, account - account2;
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
# user3: name - Ольга, age - 18, account - account3;
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
# user4: name - Анна, age - 27, account - account4.
user4 = {'name': 'Анна', 'age': 27, 'account': account4}



# Подготовка, п.3. Создать список user_list, состоящий из 4 элементов - user1...user4
user_list = [user1, user2, user3, user4]



# Программа, п.1. Программа должна запрашивать у пользователя ключ
# и выдавать информацию обо всех пользователях по введенному ключу, независимо от того в каком регистре введено значение маленькими или большими буквами.
# Если такого ключа нет, программа должна выдавать сообщение: “Введенный ключ не найден”. 
# Сообщение для ввода ключа (input): “Введите ключ (name или account): ”
show_key = input('Введите ключ (name или account): ').lower()

try:
    for i in range(0, len(user_list)):
        print(f'Значение ключа "{show_key}" для пользователя user{i+1}: {user_list[i][show_key]}')

except: # KeyError
  print('Введенный ключ не найден')



# Программа, п.2. После этого программа должна запрашивать порядковый номер
# и выводить всю информацию для юзера из списка user_list по введенному порядковому номеру.
# Если введен не корректный номер, то выдавать сообщение: “Пользователь с указанным номером не найден”.
# Сообщение для ввода порядкового номера: “Введите порядковый номер: ”

while True:
    try:
        chosen_user = int(input('\n---\nВведите порядковый номер пользователя: '))
        break
    except:
        print('Введите число!')

chosen_user -= 1 # приводим номер пользователя в соответствие с его индексом
print(f'Имя: {user_list[chosen_user]["name"]}')
print(f'Возраст: {user_list[chosen_user]["age"]}')
print(f'Логин: {user_list[chosen_user]["account"]["login"]}')
print(f'Пароль: {user_list[chosen_user]["account"]["password"]}')



# Программа, п.3. После чего программа должна спросить - какого пользователя переместить в конец
# и перенести его в конец списка user_list,
# затем вывести:
#   того кого переместили
#   список до изменения
#   список после изменения
# Сообщение для ввода: “Введите номер пользователя, которого нужно переместить в конец: ”
while True:
    try:
        chosen_user = int(input('\n---\nВведите номер пользователя, которого нужно переместить в конец: '))
        break
    except:
        print('Введите число!')

chosen_user -= 1 # приводим номер пользователя в соответствие с его индексом
print(f'Мы перемещаем: \n{user_list[chosen_user]}\nв конец\n')

print(f'Список ДО изменения:')
for i in range(0, len(user_list)):
    print(f'user{i+1}: {user_list[i]}')

pop_user = user_list.pop(chosen_user)
user_list.append(pop_user)

print(f'\nСписок ПОСЛЕ изменения:')
for i in range(0, len(user_list)):
    print(f'user{i+1}: {user_list[i]}')



# Программа, п.4. В конце должно выводиться сообщение со средним возрастом всех юзеров.
sum_age = 0
for i in range(0, len(user_list)):
    sum_age = sum_age + int(user_list[i]['age'])

average_age = sum_age / len(user_list)

print(f'\n---\nСредний возраст пользователей составляет: {average_age}')