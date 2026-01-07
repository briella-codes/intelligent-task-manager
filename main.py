from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.tasks import router as task_router
from pathlib import Path
from services.task_service import TaskLinkedList
from models.task import TaskStatus, ALLOWED_ACTIONS
from datetime import date

BASE_DIR = Path(__file__).resolve().parent
print("BASE_DIR =", BASE_DIR)

app = FastAPI()
app.include_router(task_router)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)

#from services import task_service
task_service = TaskLinkedList()

@app.get("/")
def home(request: Request, filter: str | None = None):
    task_service.load_from_file()

    if filter == "overdue":
        tasks = task_service.get_overdue_tasks()
    elif filter == "pending":
        tasks = task_service.get_pending_tasks()
    elif filter == "byPriority":
        tasks = task_service.get_tasks_by_priority()
    elif filter == "done":
        tasks = task_service.get_done_tasks()
    else:
        tasks = task_service.get_all_tasks()
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request,
         "tasks" : tasks,
         "TaskStatus" : TaskStatus,
         "allowed_actions" : ALLOWED_ACTIONS,
         "today": date.today().isoformat()
         }
    )