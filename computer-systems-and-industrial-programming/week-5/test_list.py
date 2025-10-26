import unittest
import sys

sys.path.insert(1, '../../python/week-5')
from todo_list import TodoList


class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo = TodoList()

    def test_initial_state(self):
        self.assertEqual(self.todo.get_tasks_count(), 0)
        self.assertEqual(self.todo.tasks, [])

    def test_add_valid_task(self):
        success, message = self.todo.add_task("Learn Python")
        self.assertTrue(success)
        self.assertIn("was added under number 1", message)
        self.assertEqual(self.todo.get_tasks_count(), 1)

        # Проверяем, что задача действительно добавлена
        task = self.todo.get_task_by_number(1)
        self.assertIsNotNone(task)
        self.assertEqual(task['name'], "Learn Python")
        self.assertEqual(task['number'], "1")

    def test_add_empty_task(self):
        success, message = self.todo.add_task("")
        self.assertFalse(success)
        self.assertEqual(message, "Please enter a valid task name")
        self.assertEqual(self.todo.get_tasks_count(), 0)

        success, message = self.todo.add_task("   ")
        self.assertFalse(success)
        self.assertEqual(self.todo.get_tasks_count(), 0)

    def test_view_empty_tasks(self):
        result = self.todo.view_tasks()
        self.assertEqual(result, "There are no tasks")

    def test_view_tasks_with_content(self):
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")

        result = self.todo.view_tasks()
        self.assertIn("Task 1", result)
        self.assertIn("Task 2", result)
        self.assertIn("Number: 1", result)
        self.assertIn("Number: 2", result)

    def test_delete_task_by_number(self):
        self.todo.add_task("Task to delete")
        self.assertEqual(self.todo.get_tasks_count(), 1)

        success, message = self.todo.delete_task("1")
        self.assertTrue(success)
        self.assertIn("was deleted under number 1", message)
        self.assertEqual(self.todo.get_tasks_count(), 0)

    def test_delete_task_by_name(self):
        self.todo.add_task("Task to delete")
        self.assertEqual(self.todo.get_tasks_count(), 1)

        success, message = self.todo.delete_task("Task to delete")
        self.assertTrue(success)
        self.assertIn("was deleted under number 1", message)
        self.assertEqual(self.todo.get_tasks_count(), 0)

    def test_delete_nonexistent_task(self):
        success, message = self.todo.delete_task("999")
        self.assertFalse(success)
        self.assertEqual(message, "No such task")

        success, message = self.todo.delete_task("Nonexistent Task")
        self.assertFalse(success)
        self.assertEqual(message, "No such task")

    def test_delete_empty_identifier(self):
        success, message = self.todo.delete_task("")
        self.assertFalse(success)
        self.assertEqual(message, "Please enter a task name or number")

    def test_auto_increment_numbers(self):
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        self.todo.add_task("Task 3")

        self.assertEqual(self.todo.get_task_by_number(1)['name'], "Task 1")
        self.assertEqual(self.todo.get_task_by_number(2)['name'], "Task 2")
        self.assertEqual(self.todo.get_task_by_number(3)['name'], "Task 3")

        self.todo.delete_task("2")
        self.todo.add_task("Task 4")

        self.assertEqual(self.todo.get_task_by_number(4)['name'], "Task 4")


if __name__ == '__main__':
    unittest.main()