#!/usr/bin/env python3

""" 
todolist.py  - Functions to manage tasks in a Personal To-Do List
Written by: Jean M Lauture
Date: July 23, 2026
"""
# ==========================================
# Task 2: Implement To-Do Manager Functions
# ==========================================

import datetime

# from SBA_Python2.task import Task
from task import Task

def add_task(task_list, title, due_date=None):
    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
        task = Task(title, due_date)
        #if due_date is not None:
        #    task.due_date = due_date(datetime.date.today("%Y-%m-%d"))
        task_list.append(task)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
def complete_task(task_list, index):
    try:
        if 0 <= index < len(task_list):
            task_list[index].mark_completed()
    except IndexError:
        print("Invalid task index.")

def delete_task(task_list, index):
    try:
        if 0 <= index < len(task_list):
            task_list.pop(index)
    except IndexError:
        print("Invalid task index.")

def list_tasks(task_list):
    for index, task in enumerate(task_list):
        print(f"{index}: {task}")

def mark_task_completed(task_list, index):
    try:
        if 0 <= index < len(task_list):
            task_list[index].mark_completed()
    except IndexError:
        print("Invalid task index.")
