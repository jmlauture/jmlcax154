#!/usr/bin/env python3

""" 
main.py  - The User Interface for the Personal To-Do List Management system
Written by: Jean M Lauture
Date: July 23, 2026
"""
# ==========================================
# Task 3: Create the Main User Interface
# ==========================================
from pathlib import Path

from todolist import add_task, complete_task, delete_task, list_tasks, mark_task_completed

file_path = Path("C:/Users/pasto/my_github/jmlcax154/SBA_Python2")
taskfile = file_path / "tasks.txt"


if __name__ == "__main__":

    task_list = []

    while True:
        print("\nPersonal To-Do List Management System")
        print("A. Add Task")
        print("B. Complete Task")
        print("C. Delete Task")
        print("D. List Tasks")
        print("E. Mark Task as Completed")
        print("F. Quit")

        choice = input("Enter your choice: ")

        if choice == "A":
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            add_task(task_list, title, due_date)
        elif choice == "B":
            index = int(input("Enter task index to complete: "))
            complete_task(task_list, index)
        elif choice == "C":
            index = int(input("Enter task index to delete: "))
            delete_task(task_list, index)
        elif choice == "D":
            list_tasks(task_list)
        elif choice == "E":
            index = int(input("Enter task index to mark as completed: "))
            mark_task_completed(task_list, index)
        elif choice == "F":
            print("\nThank you for using the Personal To-Do List Management System.")
            print("\n" + "-"*50 + "\n")
            print("\nDo you want to save your tasks before exiting? (Y/N)")
            save_choice = input().strip().upper()
            if save_choice == "Y":
                # Implement saving functionality here (e.g., save to a file)
                # Check if the file tasks.txt exist  
                #if taskfile.is_file():
                #  open("tasks.txt", "w").write("\n".join(str(task) for task in task_list)) 
                #  print("Tasks saved successfully.")

                try:
                    # The a will create if it does not exist
                    with open(taskfile, "a") as file:
                       file.write("\n".join(str(task) for task in task_list))
                       print("\nTasks saved successfully.")   
                       break                 
                except FileNotFoundError:
                    # Code will actually only trigger here if the parent directory folder doesn't exist.
                    print(f"The requested file {taskfile} could not be found.")
                    print("\nCreate the file and try again.")
                    break
            else:
                break
        else:
            print("\nInvalid choice. Please try again.")
