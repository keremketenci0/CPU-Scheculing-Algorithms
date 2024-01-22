class sjf_non_preemptive_Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turn_around_time = 0


def sjf_non_preemptive_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x.arrival_time)

    completion_time = 0
    result_list = []

    while processes:
        ready_processes = [p for p in processes if p.arrival_time <= completion_time]
        if not ready_processes:
            completion_time += 1
            continue

        shortest_process = min(ready_processes, key=lambda x: x.burst_time)

        processes.remove(shortest_process)

        shortest_process.completion_time = completion_time + shortest_process.burst_time
        shortest_process.turn_around_time = shortest_process.completion_time - shortest_process.arrival_time
        shortest_process.waiting_time = shortest_process.turn_around_time - shortest_process.burst_time

        completion_time = shortest_process.completion_time

        result = (
            {"Process": shortest_process.process_id, "Arrival Time": shortest_process.arrival_time, "Burst Time": shortest_process.burst_time, "Completion Time": shortest_process.completion_time, "Turn Around Time": shortest_process.turn_around_time, "Waiting Time": shortest_process.waiting_time}
        )
        result_list.append(result)
        print("\n", result)

    avg_turn_around_time = sum(p['Turn Around Time'] for p in result_list) / n
    avg_waiting_time = sum(p['Waiting Time'] for p in result_list) / n

    result_list.append(avg_turn_around_time)
    result_list.append(avg_waiting_time)
    
    return result_list

if __name__ == "__main__":
    processes = [sjf_non_preemptive_Process(*process) for process in [
        (1, 0, 8),
        (2, 1, 1),
        (3, 2, 3),
        (4, 3, 2),
        (5, 4, 6)
    ]]

    sjf_non_preemptive_scheduling(processes)
