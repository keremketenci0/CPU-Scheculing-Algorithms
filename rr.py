class RoundRobinProcess:
    processes = [
        (1, 0, 5),
        (2, 1, 3),
        (3, 2, 1),
        (4, 3, 2),
        (5, 4, 3)
    ]

    def __init__(self, process_id, arrival_time, burst_time, quantum = 2):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.quantum = quantum

def rr_scheduling(processes):
    current_time = 0
    result_list = []

    while any(process.remaining_time > 0 for process in processes):
        for process in processes:
            if process.remaining_time > 0:
                if process.arrival_time > current_time:
                    current_time = process.arrival_time

                execution_time = min(process.quantum, process.remaining_time)
                process.remaining_time -= execution_time
                process.waiting_time = max(0, (current_time - process.arrival_time))
                current_time += execution_time
                
                process.completion_time = current_time
                
                result = {
                    "Process": process.process_id,
                    "Arrival Time": process.arrival_time,
                    "Burst Time": process.burst_time,
                    "Completion Time": process.completion_time,
                    "Waiting Time": process.waiting_time if process.remaining_time == 0 else "-",
                }
                result_list.append(result)
                print(result)

    total_waiting_time = sum(process.waiting_time for process in processes)
    avg_waiting_time = total_waiting_time / len(processes)

    result_list.append(avg_waiting_time)

    return result_list

if __name__ == "__main__":
    processes = [RoundRobinProcess(*process) for process in RoundRobinProcess.processes]
    results = rr_scheduling(processes)
