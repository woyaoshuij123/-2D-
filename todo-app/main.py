#!/usr/bin/env python3
"""
To-Do List Application - Main Entry Point
"""

import sys
from todo_manager import TodoManager
from ui import TodoUI

def main():
    """Initialize and run the to-do application."""
    print("\n" + "="*50)
    print("Welcome to the To-Do List Application")
    print("="*50 + "\n")
    
    manager = TodoManager()
    ui = TodoUI(manager)
    
    try:
        ui.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
