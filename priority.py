class PriorityProcess:
    processes = [
        (1, 1, 3, 2),
        (2, 3, 6, 1),
        (3, 5, 8, 3),
        (4, 7, 4, 2),
        (5, 8, 5, 1)
    ]

    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turn_around_time = 0


def priority_scheduling(processes):
    total_waiting_time = 0
    total_turn_around_time = 0
    current_time = 0
    total_processes = len(processes)
    result_list = []

    while processes:
        ready_processes = [p for p in processes if p.arrival_time <= current_time]

        if not ready_processes:
            current_time += 1
            continue

        ready_processes.sort(key=lambda x: (x.priority, x.arrival_time))
        selected_process = ready_processes[0]

        selected_process.completion_time = current_time + selected_process.burst_time
        selected_process.turn_around_time = selected_process.completion_time - selected_process.arrival_time
        selected_process.waiting_time = selected_process.turn_around_time - selected_process.burst_time

        total_waiting_time += selected_process.waiting_time
        total_turn_around_time += selected_process.turn_around_time
        current_time = selected_process.completion_time

        processes.remove(selected_process)

        result = {
            "Process": selected_process.process_id,
            "Arrival Time": selected_process.arrival_time,
            "Burst Time": selected_process.burst_time,
            "Completion Time": selected_process.completion_time,
            "Turn Around Time": selected_process.turn_around_time,
            "Waiting Time": selected_process.waiting_time,
            "Priority": selected_process.priority
        }
        result_list.append(result)
        print("\n", result, "\n")

    average_waiting_time = total_waiting_time / total_processes
    average_turn_around_time = total_turn_around_time / total_processes

    result_list.append(average_turn_around_time)
    result_list.append(average_waiting_time)
    return result_list


if __name__ == "__main__":
    processes = [PriorityProcess(*process) for process in PriorityProcess.processes]
    results = priority_scheduling(processes)

    print("Average Turn Around Time:", results[-2])
    print("Average Waiting Time:", results[-1])