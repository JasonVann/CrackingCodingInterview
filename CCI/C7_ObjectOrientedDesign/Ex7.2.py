class Employee():
    def __init__(self, id, level):
        self.id = id
        self.level = level
        self.is_available = True
        self.can_handle = True

    def handle_call(self, a_call):
        pass

class Call():
    def __init__(self, level_required):
        self.level_required = level_required

class CallCenter():
    def __init__(self, res_count, manager_count, director_count):
        self.res = []
        self.manager = []
        self.director = []
        for i in range(res_count):
            self.res.append(Employee(i, 1))
        for i in range(manager_count):
            self.manager.append(Employee(i, 2))
        for i in range(director_count):
            self.director.append(Employee(i, 3))

    def dispatch_call(self, a_call):
        no_free = False
        if a_call.level_required == 1:
            for i, res in enumerate(self.res):
                if res.is_available:
                    res.handle_call(a_call)
                    return
            no_free = True
        elif no_free or a_call.level_required == 2:
            for i, res in enumerate(self.manager):
                if res.is_available:
                    res.handle_call(a_call)
                    return
            no_free = True
        else:
            for i, res in enumerate(self.director):
                if res.is_available:
                    res.handle_call(a_call)
                    return
            no_free = True
        if no_free:
            self.busy_tone()

    def busy_tone(self):
        return 'Please wait patiently'
