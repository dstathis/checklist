#    Copyright (C) 2018 Dylan Stephano-Shachter
#
#    This file is part of Checklist.
#
#    Checklist is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Checklist is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Checklist.  If not, see <https://www.gnu.org/licenses/>.

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
