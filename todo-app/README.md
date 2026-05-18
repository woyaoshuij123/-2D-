# To-Do List Application

A simple yet powerful to-do list application with local storage functionality.

## Features

- ✅ Create, read, update, and delete tasks
- 💾 Persistent local storage using JSON
- 🏷️ Categorize tasks
- ⭐ Mark tasks as complete
- 🔍 Filter and search tasks
- 📊 Task statistics

## Project Structure

```
todo-app/
├── main.py              # Application entry point
├── todo_manager.py      # Core task management logic
├── storage.py           # Local storage handler
├── ui.py                # User interface
├── config.py            # Configuration settings
├── data/
│   └── tasks.json       # Local storage file
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Commands

- `add <task>` - Add a new task
- `list` - Show all tasks
- `complete <id>` - Mark task as complete
- `delete <id>` - Delete a task
- `edit <id> <new_task>` - Edit a task
- `search <keyword>` - Search tasks
- `stats` - Show task statistics
- `exit` - Exit the application

## License

MIT
