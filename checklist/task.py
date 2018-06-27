import uuid


class Task:

    def __init__(self, name, description=None, parent=None):
        self.name = name
        self.description = description
        if parent:
            parent.addChild(self)
            self.parent = parent.name
        self.children = []
        self.completed = False

    def addChild(self, child):
        self.children.append(child.name)
