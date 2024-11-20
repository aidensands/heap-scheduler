from task import Task
from datetime import datetime
class Scheduler:

    def __init__(self):
        self._heap = []
        self._idx = {}

    def __len__(self):
        return len(self._heap)

    def get_parent_index(self, i):
        return (i - 1) // 2 if i else None

    def get_left_child_index(self, i):
        index = 2 * i + 1
        return index if index < len(self) else None

    def get_right_child_index(self, i):
        index = 2 * i + 1
        return index if index < len(self) else None

    def get_min_child_index(self, i):
        right_child_i = self.get_right_child_index(i)
        left_child_i = self.get_left_child_index(i)

        if left_child_i is None:
            return None
        elif right_child_i is None:
            return left_child_i
        else:
            return left_child_i if self._heap[left_child_i] < self._heap[right_child_i] else right_child_i

    def add_task(self, item, priority, desc):
        self._heap.append(Task(priority, item, desc, datetime.now()))
        self._idx[item] = len(self) - 1
        self.up_heap(len(self) - 1)
        return f'Added Task With Priority {priority}'

    def down_heap(self, i):
        min_child = self.get_min_child_index(i)

        while min_child is not None and self._heap[i] > self._heap[min_child]:
            self._swap(i, min_child)
            i = min_child
            min_child = self.get_min_child_index(i)

    def up_heap(self, i):
        parent_index = self.get_parent_index(i)

        while parent_index is not None and self._heap[i] < self._heap[parent_index]:
            self._swap(i, parent_index)
            i = parent_index
            parent_index = self.get_parent_index(i)

    def _swap(self, i , j):
        item_i = self._heap[i].name
        item_j = self._heap[j].name
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        self._idx[item_i] = j
        self._idx[item_j] = i

    def do_task(self):
        task = self._heap[0]
        self._swap(0, len(self) - 1)
        self._heap.pop()
        self._idx.pop(task.name)
        self.down_heap(0)
        return f'Task Complete: {task.name} at {datetime.now()}'
