from datetime import date
from models.task import Task

#check: it's overdue if task is not done or due date < today
def is_overdue(task: Task) -> bool:
    if task.status == "Done" or task.status =="Canceled" or (not task.due_date):
        return False
    return ( task.due_date < date.today() )

def is_pending(task: Task) -> bool:
    if task.status =="Done" or task.status =="in Progress" or task.status =="Canceled":
        return False
    return task.status =="Pending" or task.status =="Paused"

def is_done(task: Task) -> bool:
    if task.status =="Done":
        return True
    return False

#rush task?
def is_urgent(task: Task) -> bool:
    if task.priority !=1:
        return False
    return is_overdue(task)

#suspicious task... rescheduled many times or blocked/paused
#feature still in progress funcionalidad todavia no disponible
def is_procrastinated(task: Task) -> bool:
    if task.reschedule_count >= 3:
        return True
    if task.status =="Paused":
        return True
        
    return False