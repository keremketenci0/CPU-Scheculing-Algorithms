class HrrnProcess:
    processes = [
        (1, 1, 3),
        (2, 3, 6),
        (3, 5, 8),
        (4, 7, 4),
        (5, 8, 5)
    ]
    
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turn_around_time = 0
        self.response_ratio = 0

def hrrn_scheduling(processes):
    total_waiting_time = 0
    total_turn_around_time = 0
    total_response_ratio = 0
    current_time = 0
    total_processes = len(processes)
    result_list = []

    while processes:
        ready_processes = [p for p in processes if p.arrival_time <= current_time]

        if not ready_processes:
            current_time += 1
            continue

        for process in ready_processes:
            process.response_ratio = (current_time - process.arrival_time + process.burst_time) / process.burst_time

        ready_processes.sort(key=lambda x: x.response_ratio, reverse=True)
        selected_process = ready_processes[0]

        selected_process.completion_time = current_time + selected_process.burst_time
        selected_process.turn_around_time = selected_process.completion_time - selected_process.arrival_time
        selected_process.waiting_time = selected_process.turn_around_time - selected_process.burst_time

        total_waiting_time += selected_process.waiting_time
        total_turn_around_time += selected_process.turn_around_time
        total_response_ratio += selected_process.response_ratio
        current_time = selected_process.completion_time

        processes.remove(selected_process)

        for process in processes:
            process.response_ratio = (current_time - process.arrival_time + process.burst_time) / process.burst_time

        result = {
            "Process": selected_process.process_id,
            "Arrival Time": selected_process.arrival_time,
            "Burst Time": selected_process.burst_time,
            "Completion Time": selected_process.completion_time,
            "Turn Around Time": selected_process.turn_around_time,
            "Waiting Time": selected_process.waiting_time,
            "Response Ratio": selected_process.response_ratio
        }
        result_list.append(result)
        print("\n\n")
        print(result)

    average_waiting_time = total_waiting_time / total_processes
    average_turn_around_time = total_turn_around_time / total_processes
    average_response_ratio = total_response_ratio / total_processes

    result_list.append(average_response_ratio)
    result_list.append(average_turn_around_time)
    result_list.append(average_waiting_time)
    return result_list


if __name__ == "__main__":
    processes = [HrrnProcess(*process) for process in HrrnProcess.processes]
    results = hrrn_scheduling(processes)

    print("\nAverage Response Ratio:", results[-3])
    print("Average Turn Around Time:", results[-2])
    print("Average Waiting Time:", results[-1])