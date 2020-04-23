from sharpy.managers import *

class ManagerHolder:
    """
    """
    def __init__(self, knowledge=None,str_manager_dict=None,type_manager_dict=None):
        self.is_loaded = False
        self.knowledge = None
        self.type_manager_dict = type_manager_dict or dict()

    def load_managers(self, knowledge=None):
        if knowledge:
            self.knowledge = knowledge
        if not self.is_loaded:
            if self.knowledge:
                for manager in self.knowledge.managers:
                    self.add(key_string=None, manager=manager)
                self.is_loaded = True

    def add(self, manager: ManagerBase = None) -> None:
        """

        """
        if not self.knowledge:
            return
        if manager is not None and self.type_manager_dict.get(type(manager), None) is None:
            self.type_manager_dict[type(manager)] = manager
        if manager not in self.knowledge.managers:
            self.knowledge.managers.append(manager)

    def remove(self):
        pass

    def __getitem__(self, key):
        return self.type_manager_dict.get(type(key), None)
