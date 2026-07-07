import mysql.connector

# ==============================
# DATABASE CONNECTION
# ==============================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kalkimaster3.6.9",
        database="hello2"
    )


# ==============================
# CREATE TASK
# ==============================
def create_task():
    title = input("Enter task title: ")
    description = input("Enter description: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO tasks (title, description) VALUES (%s, %s)"
    cursor.execute(query, (title, description))

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Task created successfully!")


# ==============================
# READ TASKS
# ==============================
def view_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    print("\n📋 TASK LIST\n")

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print("-" * 30)

    cursor.close()
    conn.close()


# ==============================
# UPDATE TASK
# ==============================
def update_task():
    task_id = input("Enter task ID: ")
    new_status = input("Enter new status (pending/completed): ")

    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE tasks SET status=%s WHERE id=%s"
    cursor.execute(query, (new_status, task_id))

    conn.commit()
    cursor.close()
    conn.close()

    print("🔄 Task updated successfully!")


# ==============================
# DELETE TASK
# ==============================
def delete_task():
    task_id = input("Enter task ID to delete: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM tasks WHERE id=%s"
    cursor.execute(query, (task_id,))

    conn.commit()
    cursor.close()
    conn.close()

    print("🗑️ Task deleted successfully!")


# ==============================
# MENU SYSTEM
# ==============================
def menu():
    while True:
        print("\n====== TASK MANAGER ======")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice, try again.")


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    menu()