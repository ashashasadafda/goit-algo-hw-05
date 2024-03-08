#завдання 2
def sum_profit(text:str, func:callable):
    return sum(func(text))
    
def generator_numbers(text:str):
    new_text = text.split(" ")
    for word in new_text:
        try:
            number = float(word)
            yield number
        except ValueError:
            pass
   
text = """Загальний дохід працівника складається з декількох 
# частин: 1000.01 як основний дохід, доповнений додатковими 
# надходженнями 27.45 і 324.00 доларів."""         

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")