class Process:
    def __init__(self):
        pass


class Resource:
    def __init__(self, max_r):
        self.max = max_r
        self.current = max_r


resources = []
processes = []


def add_resource(max_r):
    res = Resource(max_r)
    resources.append(res)


def add_process(num):
    for x in range(0, num):
        processes.append(Process())


def get_processes():
    return processes


def get_resources():
    return resources
