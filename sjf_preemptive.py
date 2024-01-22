class sjf_preemptive_Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_burst_time = burst_time
        self.completion_time = None
        self.waiting_time = None
        self.turn_around_time = None


def sjf_preemptive_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x.arrival_time)
    completion_time = 0
    result_list = []
    last_processed_id = 1

    while processes:
        ready_processes = [p for p in processes if p.arrival_time <= completion_time and p.remaining_burst_time > 0]
        if not ready_processes:
            completion_time += 1
            continue

        shortest_process = min(ready_processes, key=lambda x: x.remaining_burst_time)

        shortest_process.remaining_burst_time -= 1


        result = {
            "Process": shortest_process.process_id,
            "Arrival Time": shortest_process.arrival_time,
            "Burst Time": shortest_process.burst_time,
            "Completion Time": completion_time + 1,
            "Turn Around Time": "" if shortest_process.remaining_burst_time > 0 else completion_time + 1 - shortest_process.arrival_time,
            "Waiting Time": "" if shortest_process.remaining_burst_time > 0 else completion_time + 1 - shortest_process.arrival_time - shortest_process.burst_time
        }

        if shortest_process.remaining_burst_time == 0:
            processes.remove(shortest_process)

        result_list.append(result)
        print("\n", result)

        completion_time += 1

    avg_turn_around_time = sum(0 if p['Turn Around Time'] == "" else p['Turn Around Time'] for p in result_list) / n
    avg_waiting_time = sum(0 if p['Waiting Time'] == "" else p['Waiting Time'] for p in result_list) / n

    result_list.append(avg_turn_around_time)
    result_list.append(avg_waiting_time)

    return result_list


if __name__ == "__main__":
    processes = [sjf_preemptive_Process(*process) for process in [
        (1, 0, 7),
        (2, 1, 5),
        (3, 2, 3),
        (4, 3, 1),
        (5, 4, 2),
        (6, 5, 1)
    ]]

    sjf_preemptive_scheduling(processes)
