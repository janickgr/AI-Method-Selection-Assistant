import os

class Utils:

    @staticmethod
    def make_absolute_path(relative_path):
        # Normiere die Pfade, um sicherzustellen, dass sie die richtige Syntax haben
        relative_path = os.path.normpath(relative_path)
        base_path = os.path.abspath(os.getcwd())

        # Verbinde den relativen Pfad mit dem Basispfad
        absolute_path = os.path.join(base_path, relative_path)

        return absolute_path
    
    @staticmethod
    def add_elements_to_dict(dictionary, new_elements):
        dictionary.update(new_elements)

        return dictionary