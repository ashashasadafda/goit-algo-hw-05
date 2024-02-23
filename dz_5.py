# завдання 1
# def caching_fibonacci():
#     cache = {}

#     def fibonacci(n):
#         if n <= 0:
#             return 0
#         if n == 1: 
#             return 1
#         if n in cache: 
#             return cache[n]

#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return cache[n]

#     return fibonacci



# fib = caching_fibonacci()

# print(fib(5))
# print(fib(25))



# завдання 2
# def sum_profit(text:str, func:callable):
#     return sum(func(text))
    
# def generator_numbers(text:str):
#     new_text = text.split(" ")
#     for word in new_text:
#         try:
#             number = float(word)
#             yield number
#         except ValueError:
#             pass
   
# text = """Загальний дохід працівника складається з декількох 
# # частин: 1000.01 як основний дохід, доповнений додатковими 
# # надходженнями 27.45 і 324.00 доларів."""         

# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")



# завдання 4
def input_error(func):
    def inner(*args, **kwargs):
        # Перевірка чи всі аргументи отримали значення
        if any(arg is None for arg in args[1:]):
            return "введіть аргументи для команди!"
        
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "ви ввели неправильну команду. спробуйте ще разок"
            
            elif isinstance(e, ValueError):
                return "ееправильний формат даних. спробуйте ще разок"
            
            elif isinstance(e, IndexError):
                return "еедостатньо аргументів для виконання команди. спробуйте ще разок"
    return inner

@input_error
def add_contact(phonebook, name, number):
    phonebook[name] = number
    return f"контакт {name} додано до бази бота"

@input_error
def change_contact(phonebook, name, new_number):
    if name in phonebook:
        phonebook[name] = new_number
        return f"контакт {name} оновлено"
    else:
        raise KeyError

@input_error
def show_phone(phonebook, name):
    if name in phonebook:
        return f"номер телефону для контакту {name}: {phonebook[name]}"
    else:
        raise KeyError

@input_error
def show_all(phonebook):
    if phonebook:
        return "\n".join([f"{name}: {number}" for name, number in phonebook.items()])
    else:
        return "база ботіка пуста"

def parse_input(command):
    return command.split()

def main():
    phonebook_bot = {}
    while True:
        command = input("введіть команду або 'close'/'exit' для виходу: ").strip()

        parts = parse_input(command)

        if len(parts) == 1:
            action = parts[0]
            arg1 = arg2 = None
        elif len(parts) == 2:
            action, arg1 = parts
            arg2 = None
        elif len(parts) == 3:
            action, arg1, arg2 = parts
            
        else:
            print("ьакої команди не існує")
            continue

        if action == "close" or action == "exit":
            print("закриваюсь :0")
            break
        
        elif action == "hello":
            print("привіт. як я можу вам допомогти?")
            
        elif action == "add":
            print(add_contact(phonebook_bot, arg1, arg2))
            
        elif action == "change":
            print(change_contact(phonebook_bot, arg1, arg2))
            
        elif action == "phone":
            print(show_phone(phonebook_bot, arg1))
            
        elif action == "all":
            print(f"-------------\n{show_all(phonebook_bot)}\n-------------")
            
        else:
            print("такої команди не існує")


if __name__ == "__main__":
    main()
