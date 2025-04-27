from colorama import init, Fore
init(autoreset=True)

tasks = []

def show_tasks(): 
    if len(tasks) > 0:  
        print("Список задач:")
        for i in range(len(tasks)):  
            print(f"{i + 1}. {tasks[i]}")

def add_task(): 
    task = input("Введіть вашу задачу: ")
    tasks.append(task)
    print(Fore.GREEN + f"Задача {task} додана.")

def remove_task():
    show_tasks()
    if len(tasks) > 0:
        show_tasks()
        try:
            task_number = int(input("Введіть номер задачі для видалення:"))
            if task_number < 1 or task_number > len(tasks):
                print(Fore.RED + "Невірний номер задачі. Спробуйте ще раз.")
            else:
                removed_task = tasks.pop(task_number - 1)
                print(Fore.BLUE + f"Задача '{removed_task}' видалена.")
        except ValueError:
                print(Fore.RED + "Ви повинні ввести правильний номер задачі.")
    else:
        print(Fore.RED + ">>> Ваш список задач порожній")
            
def main():
  print(Fore.GREEN + "\n" + "*" * 10, "Ваш помічник на кожен день",Fore.GREEN + "*" * 10 + "\n")
  while True:
        print("1) Продивитись мої задачі")   
        print("2) Додати нову задачу")
        print("3) Видалити задачу")
        print("4) Вийти ")
        try:
            choice = int(input(Fore.GREEN + "Введіть значення:"))
            if choice == 4:
                print(Fore.GREEN + "\n" + "*" * 10, "Програма завершена",Fore.GREEN + "*" * 10 + "\n")
                break
            elif choice == 1:
               show_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                remove_task()
            else:
                print(Fore.RED + "[!] Невірний ввід, спробуйте ввести число від 1 до 3")
        except (TypeError, ValueError):
            print(Fore.RED + "[!] Ви повинні вести ціле число")
        
main()