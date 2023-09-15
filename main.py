import day5Task


taskList = [task for task in dir(day5Task) if callable(getattr(day5Task, task)) and not task.startswith("__") if task.startswith("task") ]
print(taskList)
for taskName in sorted(taskList):
    task = (getattr(day5Task, taskName))
    task()
    print("\n")
