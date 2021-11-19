class Process:
    def __init__(self):
        self.holding_res = []
        self.waiting_res = []
        self.finish = False


class Resource:
    def __init__(self, max_r):
        self.max_r = int(max_r)
        self.cur_r = int(max_r)


resources = []
processes = []
wait_queue = []


def add_resource(commands):
    for x in range(1, int(commands[0]) + 1):
        new_resource = Resource(commands[x])
        resources.append(new_resource)
        for p in processes:
            p.holding_res.append(0)
            p.waiting_res.append(0)


def add_process(num):
    for x in range(0, num):
        processes.append(Process())


def request_resource(p_index, r_index, amt):
    process = processes[p_index]
    resource = resources[r_index]
    for x in range(0, amt):
        if resource.cur_r > 0:
            resource.cur_r -= 1
            process.holding_res[r_index] += 1
        else:
            process.waiting_res[r_index] += 1
            wait_queue.append((p_index, r_index))
            print("Process {0} blocked, waiting on resource {1}".format(p_index, r_index))


def release_resource(p_index, r_index, amt):
    process = processes[p_index]
    resource = resources[r_index]
    for x in range(0, amt):
        if resource.cur_r < resource.max_r:
            resource.cur_r += 1
            process.holding_res[r_index] -= 1
            y = 0
            for wait in wait_queue:
                res_index = wait[1]
                pro_index = wait[0]
                if resources[res_index].cur_r > 0:
                    processes[pro_index].waiting_res[res_index] -= 1
                    processes[pro_index].holding_res[res_index] += 1
                    resources[res_index].cur_r -= 1
                    wait_queue.pop(y)
                    print("Process {0} receives resource {1}".format(pro_index, res_index))
                    y -= 1
                y += 1


def check_deadlock():
    open_r = []
    run_sequence = ""
    for r in resources:
        open_r.append(r.cur_r)
    for p in processes:
        p.finish = False
    all_finished = False
    change_occurred = True
    while not all_finished and change_occurred:
        change_occurred = False
        all_finished = True
        p_index = 0
        for p in processes:
            if not p.finish:
                all_finished = False
            if len(p.waiting_res) == 0 and not p.finish:
                change_occurred = True
                p.finish = True
                run_sequence += "P" + str(p_index) + ","
                for x in range(0, len(p.holding_res)):
                    open_r[x] += p.holding_res[x]
            elif not p.finish:
                can_finish = True
                for x in range(0, len(p.holding_res)):
                    if p.waiting_res[x] > open_r[x]:
                        can_finish = False
                if can_finish:
                    change_occurred = True
                    p.finish = True
                    run_sequence += "P" + str(p_index) + ","
                    for x in range(0, len(p.holding_res)):
                        open_r[x] += p.holding_res[x]
            p_index += 1
    if all_finished:
        res = "No deadlock. Possible run sequence "
        print(res + run_sequence)
    else:
        print("Deadlocked")


def get_processes():
    return processes


def get_resources():
    return resources
