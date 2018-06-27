import pickle

from checklist.task import Task

PICKLE_VERS = 4


class Checklist:

    def __init__(self, pickle_path=None):
        if pickle_path:
            self.idmap = {}
            self.load(pickle_path)
        else:
            self.tasks = []
            self.idmap = {}

    def load(self, pickle_path):
        with open(pickle_path, 'rb') as pkl:
            self.tasks = pickle.load(pkl)
        for task in self.tasks:
            self.idmap[task.name] = task

    def save(self, pickle_path):
        with open(pickle_path, 'wb') as pkl:
            pickle.dump(self.tasks, pkl, protocol=PICKLE_VERS)

    def newTask(self, name, description=None, parent=None):
        new_task = Task(name, description, parent)
        self.tasks.append(new_task)
        self.idmap[new_task.name] = new_task
