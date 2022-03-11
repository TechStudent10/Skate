class Function:
    def __init__(self, name, uid, args, lines):
        self.name = name
        self.uid = uid
        self.args = args
        self.lines = lines

    def return_obj(self):
        return self.__dict__