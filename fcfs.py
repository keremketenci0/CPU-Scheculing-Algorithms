class FcfsProcess:
    processes = [
        (1, 2, 10),
        (2, 4, 5),
        (3, 6, 35),
        (4, 8, 2)
    ]

    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.turn_around_time = 0
        self.completion_time = 0
        self.waiting_time = 0

def fcfs_scheduling(process_objects):
    process_objects.sort(key=lambda x: x.arrival_time)  # Arrival time'a göre sırala
    total_waiting_time = 0
    total_turn_around_time = 0
    completion_time = 0
    result_list = []

    for process in process_objects:
        if process.arrival_time > completion_time:
            completion_time = process.arrival_time

        process.completion_time = completion_time + process.burst_time
        process.turn_around_time = process.completion_time - process.arrival_time
        process.waiting_time = max(0, process.turn_around_time - process.burst_time)

        total_waiting_time += process.waiting_time
        total_turn_around_time += process.turn_around_time
        completion_time = process.completion_time

        result = (
        {"Process": process.process_id,
        "Arrival Time": process.arrival_time,
        "Burst Time": process.burst_time,
        "Completion Time": process.completion_time,
        "Turn Around Time": process.turn_around_time,
        "Waiting Time": process.waiting_time}
        )
        result_list.append(result)
        print("\n")
        print(result)

    average_waiting_time = total_waiting_time / len(process_objects)
    average_turn_around_time = total_turn_around_time / len(process_objects)

    result_list.append(average_turn_around_time)
    result_list.append(average_waiting_time)
    return result_list

if __name__ == "__main__":
    process_objects = [FcfsProcess(*process) for process in FcfsProcess.processes]
    results = fcfs_scheduling(process_objects)

    print("\nAverage Turn Around Time:", results[-2])
    print("Average Waiting Time:", results[-1])
