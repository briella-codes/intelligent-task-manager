# INTELLIGENT TASK MANAGER server-rendered FastAPI app (Work IN PROGRESS: this project is still being developed and improved)
Run the app directly using this [https://intelligent-task-manager-vodt.onrender.com/](https://intelligent-task-manager-7hrh.onrender.com), or clone the repo and follow the installation steps [here](#INSTALLATION-AND-EXECUTION)
<sub> - para Español ir al final del README.md - </sub><br><br>
I chose to develop a task manager because **I enjoy working in an organized, structured, and efficient way**, both in a professional environment and in everyday life.
This project reflects that mindset: **prioritizing tasks, maintaining clarity, and continuously improving processes**.

**Intelligent Task Manager** is a web application developed in **Python** as a personal project, focused on **task management with priorities and due dates**. It was initially conceived as a simple yet well-structured tool to organize tasks in a clear and efficient manner.

## GOAL
To experiment with FastAPI and strengthen my knowledge, combining a **modern backend with server-side rendering (server-rendered web app) using HTML forms**, rather than building a purely public REST API.

## TOOLS AND TECHNOLOGIES USED:
* Python
* FastAPI
* Jinja2 (server-rendered HTML templates)
* Uvicorn
* HTML / CSS

## TECHNICAL APROACH
- Service-based architecture (clear separation between routes, business logic, and templates).
- Server-side rendering, oriented toward a web workflow using HTML forms.
- Use of data structures for task management:
  - heapq implements a priority queue using a binary heap based on a list (#heap #heapq #priorityqueue #lists).
  - Implementation of priority-based sorting algorithms to organize tasks.
- Data validation on both backend and frontend (for example, enforcing future due dates).

## INSTALLATION AND EXECUTION
Clone the repository and, inside the project folder, run:

- Create and activate a virtual environment: <br>
python -m venv venv  
venv\Scripts\activate  (Windows)
source venv/bin/activate  (Linux)
- Install dependencies:<br>
pip install -r requirements.txt
- Run Uvicorn:<br>
uvicorn main:app --reload
- Open in your browser:<br>
[http://localhost:8000/](http://localhost:8000/)

# INTELLIGENT TASK MANAGER -ADMINISTRADOR DE TAREAS INTELIGENTE (Trabajo EN PROCESO: este proyecto todavía está siendo desarrollado y mejorado)
Corre la app directamente usando este [https://intelligent-task-manager-vodt.onrender.com/](https://intelligent-task-manager-7hrh.onrender.com), o clona el repo y sigue los pasos de instalación [aqui](#INSTALACIÓN-Y-EJECUCIÓN)
Elegí desarrollar un task manager porque disfruto **trabajar de forma ordenada, estructurada y eficiente**, tanto en el ámbito profesional como en el día a día.
Este proyecto refleja esa forma de pensar: **priorizar tareas, mantener claridad y mejorar continuamente los procesos**.
**Intelligent Task Manager** es una aplicación web desarrollada en **Python** como proyecto personal, enfocada en la **gestión de tareas con prioridad y fechas límite**. Inicialmente pensada como una herramienta simple pero estructurada para organizar tareas de manera clara y eficiente.

## OBJETIVO:
Experimentar con FastAPI y reafirmar conocimientos, combinando **backend moderno con renderizado del lado del servidor (server-rendered web app) mediante formularios HTML**, en lugar de una API REST puramente pública.

## HERRAMIENTAS Y TECNOLOGÍAS USADAS:
- Python
- FastAPI
- Jinja2 (templates HTML renderizados en el servidor)
- Uvicorn
- HTML / CSS

## ENFOQUE TÉCNICO
- Arquitectura basada en servicios (separación entre rutas, lógica de negocio y templates).
- Renderizado del lado del servidor (server-side rendered), orientado a flujo web mediante formularios HTML.
- Uso de estructuras de datos para la gestión de tareas:
  - heapq implementa una cola de prioridad usando un heap binario basado en una lista (#heap #heapq #coladeprioridad #listas #nodos)
  - Implementación de algoritmos de ordenamiento por prioridad para organizar las tareas.
- Validaciones de datos desde backend y frontend (por ejemplo, fechas futuras)

## INSTALACIÓN Y EJECUCIÓN
Clonar el repositorio y, dentro de la carpeta del proyecto, ejecutar:
- Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate  (Windows)
source venv/bin/activate  (Linux)

- Instalar dependencias:
pip install -r requirements.txt
- Correr Uvicorn:
uvicorn main:app –reload
- Abrir en el navegador:
[http://localhost:8000/](http://localhost:8000/)

