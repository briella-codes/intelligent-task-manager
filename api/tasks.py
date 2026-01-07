from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from models.task import Task, TaskStatus
from schemas.task import TaskResponse
from services.task_service import TaskLinkedList
from datetime import date

router = APIRouter(prefix="/tasks")

templates = Jinja2Templates(directory="templates")


task_service = TaskLinkedList()

def task_to_response(task: Task) -> TaskResponse:
    return TaskResponse(id =task.id,
                        title=task.title,
                        description=task.description,
                        priority=task.priority,
                        status=task.status,
                        due_date=task.due_date)


@router.post("/")
def create_task_form(request: Request, title:str =Form(...),priority:int=Form(1), description:str | None=Form(None),due_date:date | None = Form(None)):
    if due_date and due_date < date.today():
        raise HTTPException(status_code=400,detail="Due date cannot be a past date")
    task_service.add_task(
        title = title,
        description= description,
        priority=priority,
        due_date=due_date
    )
    return RedirectResponse(url=request.headers.get("referer","/"), status_code=303)

@router.get("/{task_id}/edit")
def edit_task_form(request: Request, task_id:int):
    task = task_service.get_by_id(task_id)
    if not task:
        raise HTTPException(404)
    
    previous_url = request.headers.get("referer","/")

    return templates.TemplateResponse(
        "edit_task.html",
        {"request" : request,
         "task" :task,
         "TaskStatus" : TaskStatus,
         "previous_url" : previous_url }
    )

@router.post("/{task_id}/edit")
def update_task(request: Request,
                task_id:int,
                title:str=Form(...),
                priority:int=Form(...),
                status:TaskStatus=Form(...),
                description:str|None=Form(None),
                due_date: date | None = Form(None),
                return_to: str = Form("/")):
    task = task_service.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404)
    task.title = title
    task.priority = priority
    task_service.update_status(task_id,status)

    task.description = description
    #if due_date is not None:
    task.due_date = due_date

    #aca podria poner una validacion
    task_service.save_to_file()
    return RedirectResponse(url=return_to, status_code=303)

@router.post("/api", response_model=TaskResponse)
def create_task_api(title:str,priority:int, description:str | None,due_date:date, id:int|None):
    new_task = task_service.add_task(
        title = title,
        description= description,
        priority=priority,
        due_date=due_date,
        id = id
    )
    return task_to_response(new_task)
    
"""
@router.post("/",response_model=TaskResponse)
def create_task(task: TaskCreate):
    new_task = task_service.add_task(
        title = task.title,
        description= task.description,
        priority=task.priority,
        due_date=task.due_date
    )
    return task_to_response(new_task)
"""

@router.get("/", response_model=list[TaskResponse])
def list_tasks(order: str ="priority"):
    if order == "priority":
        tasks = task_service.get_tasks_by_priority()
    else:
        tasks = task_service.get_all_tasks()
    return [task_to_response(t) for t in tasks]


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"mesage" : "Task deleted!"}
"""
@router.post("/{task_id}/delete")
def delete_task_html(task_id: int):
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404)
    return RedirectResponse("/tasks/", status_code=303)
"""
@router.post("/{task_id}/delete")
def delete_task_form(task_id: int):
    ok = task_service.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404,detail="Task not found")
    return RedirectResponse(url="/", status_code=303)

@router.post("/delete-selected")
def delete_selected(request: Request, task_ids: list[int] | None = Form(None)):
    #print(task_ids)
    if not task_ids:
        return RedirectResponse(url=request.headers.get("referer","/"), status_code=303)
    for task_id in task_ids:
        task_service.delete_task(task_id, save=False)
    task_service.save_to_file()
    return RedirectResponse(url=request.headers.get("referer","/"), status_code=303)

@router.post("/{task_id}/status")
def change_status(request: Request, task_id:int, status:TaskStatus=Form(...)):
    ok = task_service.update_status(task_id,status)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found!")
    return RedirectResponse(url=request.headers.get("referer","/"), status_code=303)


@router.get("/flags")
def get_flags():
    overdue_tasks = task_service.get_overdue_tasks()
    procrastinated_tasks = task_service.get_procrastinated_tasks()

    return{
        "overdue" : [task_to_response(t) for t in overdue_tasks],
        "procrastinated" : [task_to_response(t) for t in procrastinated_tasks]
    }

@router.get("/stats")
def get_stats():
    return task_service.get_stats()

