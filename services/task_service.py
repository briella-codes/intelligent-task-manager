from models.task import Task, TaskStatus
from rules.task_rules import is_overdue, is_procrastinated, is_pending, is_done
from pathlib import Path
import heapq, json
from datetime import date

#save it in app/services/tasks.json
DATA_FILE = Path(__file__).parent / "tasks.json"

class TaskLinkedList:
    def __init__(self):
        #head is the fist task
        self.head = None
        self.load_from_file()

    def __str__(self):
        c= self.head
        while c:
            ret +=(str(c[0])+","+str(c[1]))
            c=c.next
        return ret
    
    def load_from_file(self):
        # reset LinkedList
        self.head = None

        if (not DATA_FILE.exists()) or ( DATA_FILE.stat().st_size==0 ):
            self.last_id = 0
            self.head = None
            return

        with open(DATA_FILE,"r",encoding="utf-8") as f:
            data =json.load(f)

        self.last_id = data.get("last_id", 0)

        for item in data.get("tasks", []):
            due_date_ = date.fromisoformat(item["due_date"]) if item["due_date"] else None
            task = Task(
                id = item["id"],
                title = item["title"],
                description = item["description"],
                priority = item["priority"],
                status = TaskStatus(item["status"]),
                due_date= due_date_ ,
                
                #save = False
            )
            #self.append(task)
            self.add_task_node(task)
        Task.id_counter = self.last_id + 1  


    def save_to_file(self):
        tasks = []
        current = self.head
        while current is not None:
            tasks.append(current.to_dict())
            current = current.next
        
        data = {
            "last_id" : Task.id_counter - 1,
            "tasks" : tasks
        }

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data,f, indent=2)

    def add_task_node(self,task: Task):
        if self.head is None:
            self.head = task
        #    return
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = task


    def add_task(self, title, priority, description =None, due_date = None, save=True):
        new_task= Task(title=title,priority=priority,description=description, due_date=due_date)

        self.add_task_node(new_task)
        
        if save:
            self.save_to_file()

        return new_task


    def get_all_tasks(self):
        heap = []
        current = self.head

        while current is not None:
            due_date_alt = current.due_date or date.max
            heapq.heappush(heap,(due_date_alt, current.priority, current.title, current.id, current))
            current = current.next

        ordered_list = []
        while heap:
            ordered_list.append(heapq.heappop(heap)[4])

        return ordered_list    

    def get_tasks_by_priority(self):
        heap = []
        current = self.head

        while current is not None:
            due_date_alt = current.due_date or date.max
            heapq.heappush(heap,(current.priority, due_date_alt, current.title, current.id, current))
            current = current.next
        """
        print("HEAAPP:")
        
        for h in heap:
            print(h[0],h[1])
        print("--------------------------")
        """
        ordered_list = []
        while heap:
            ordered_list.append(heapq.heappop(heap)[4])

        return ordered_list
    
    def get_overdue_tasks(self):
        list = []
        for t in self.get_all_tasks():
            #print(t.id, t.due_date, type(t.due_date))
            if is_overdue(t):
                list.append(t)
        return list
    
    def get_done_tasks(self):
        list = []
        for t in self.get_all_tasks():
            #print(t.id, t.due_date, type(t.due_date))
            if is_done(t):
                list.append(t)
        return list
    
    def get_pending_tasks(self):
        list = []
        for t in self.get_all_tasks():
            
            if is_pending(t):
                list.append(t)
        return list
        
    #todavia no disponible... funcionalidad en proceso
    def get_procrastinated_tasks(self):
        list=[]
        for t in self.get_all_tasks():
            
            if is_procrastinated(t):
                list.append(t)
        return list
    
    #todavia no disponible... funcionalidad en proceso
    def get_stats(self):
        tasks = self.get_all_tasks()

        stats = {
            "total" : len(tasks),
            "by_status" : {},
            "overdue" : 0
        }

        for t in tasks:
            stats["by_status"][t.status] = stats["by_status"].get(t.status, 0) + 1
            if is_overdue(t):
                stats["overdue"] +=1
        
        return stats
    
    def delete_task(self, task_id:int, save = True) -> bool:
        current = self.head
        prev = None

        while current is not None:
            if current.id == task_id:
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                
                if save:
                    self.save_to_file()
                return True
            
            prev =current
            current =current.next

        return False
    
    def get_by_id(self, task_id: int) -> Task | None:
        current = self.head
        while current is not None:
            if current.id == task_id:
                return current
            current = current.next
        return None
    
    def update_status(self, task_id:int, status: TaskStatus) -> bool:
        current = self.head
        while current is not None:
            if current.id ==task_id:
                current.status= status
                self.save_to_file()
                return True
            current = current.next
        return False