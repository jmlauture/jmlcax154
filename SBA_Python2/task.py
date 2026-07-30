#!/usr/bin/env python3

""" 
task.py  - Definition of the Personal To-Do List Management system
An implementation of Task class.
Written by: Jean M Lauture
Date: July 23, 2026
"""
# ==========================================
# Task 1: Define the Task Class
# ==========================================
import datetime

class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.title}\nDue Date: {self.due_date}\nStatus: {status}"


