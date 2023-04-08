from sys import maxsize


class Project:
    def __init__(self, id=None, name=None, status=None, is_inherit=None, view_status=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.is_inherit = is_inherit
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return f"{self.id}: {self.name} {self.status} {self.view_status} {self.description}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name \
            and self.status == other.status and self.view_status == other.view_status \
            and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize