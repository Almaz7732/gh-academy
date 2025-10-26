class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_number = 1

    def add_task(self, task_name):
        if not task_name or not task_name.strip():
            return False, "Please enter a valid task name"

        task = {'name': task_name.strip(), 'number': str(self.next_number)}
        self.tasks.append(task)
        self.next_number += 1
        return True, f"The task was added under number {task['number']}"

    def view_tasks(self):
        if not self.tasks:
            return "There are no tasks"

        result = []
        for task in self.tasks:
            result.append(f"Name: {task['name']} | Number: {task['number']}")
        return "\n".join(result)

    def delete_task(self, identifier):
        if not identifier:
            return False, "Please enter a task name or number"

        for task in self.tasks:
            if task['name'] == identifier or task['number'] == identifier:
                self.tasks.remove(task)
                return True, f"The task was deleted under number {task['number']}"

        return False, "No such task"

    def get_tasks_count(self):
        return len(self.tasks)

    def get_task_by_number(self, number):
        for task in self.tasks:
            if task['number'] == str(number):
                return task
        return None


def main():
    print('To-Do List')
    print('If you want Add a new task, please enter "add"')
    print('If you want View all tasks, please enter "view"')
    print('If you want Delete a task, please enter "delete"')
    print('If you want exit, please enter "exit"')

    todo = TodoList()

    while True:
        user_input = input('Enter a command: ').strip().lower()

        if user_input == 'add':
            task_name = input('Enter a task name: ')
            success, message = todo.add_task(task_name)
            print(message)

        elif user_input == 'view':
            result = todo.view_tasks()
            print(result)

        elif user_input == 'delete':
            task_identifier = input('Enter a task name or number for delete: ')
            success, message = todo.delete_task(task_identifier)
            print(message)

        elif user_input == 'exit':
            print('Goodbye!')
            break

        else:
            print('Unknown command. Please enter "add", "view", "delete", or "exit"')


if __name__ == "__main__":
    main()