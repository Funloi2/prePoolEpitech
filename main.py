import day4Task


taskList = [task for task in dir(day4Task) if callable(getattr(day4Task, task)) and not task.startswith("__") if task.startswith("task") ]
print(taskList)
for taskName in sorted(taskList):
    task = (getattr(day4Task, taskName))
    task()
    print("\n")
