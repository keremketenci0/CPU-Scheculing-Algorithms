import tkinter as tk
from tkinter import messagebox
from fcfs import fcfs_scheduling, FcfsProcess
from hrrn import hrrn_scheduling, HrrnProcess
from sjf_non_preemptive import sjf_non_preemptive_scheduling, sjf_non_preemptive_Process
from sjf_preemptive import sjf_preemptive_scheduling, sjf_preemptive_Process
from ltf import ltf_scheduling, LtfProcess
from rr import rr_scheduling, RoundRobinProcess
from priority import priority_scheduling, PriorityProcess
import pandas as pd
import matplotlib.pyplot as plt

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Simulator")
        self.root.geometry("600x500")
        
        self.fcfs_processes = []
        self.hrrn_processes = []
        self.sjf_non_preemptive_processes = []
        self.sjf_preemptive_processes = []
        self.ltf_processes = []
        self.rr_processes = []
        self.priority_processes = []

        self.fcfs_checked = tk.BooleanVar()
        self.hrrn_checked = tk.BooleanVar()
        self.sjf_non_preemptive_checked = tk.BooleanVar()
        self.sjf_preemptive_checked = tk.BooleanVar()
        self.ltf_checked = tk.BooleanVar()
        self.rr_checked = tk.BooleanVar()
        self.priority_checked = tk.BooleanVar()

        self.create_widgets()
    
    def create_widgets(self):
        # inputs_frame
        self.inputs_frame = tk.Frame(self.root)
        self.inputs_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # frame for space
        self.space_frame_left = tk.Frame(self.root, width=20)
        self.space_frame_left.pack(side=tk.LEFT)
        
        # inputs
        self.label_arrival = tk.Label(self.inputs_frame, text="Arrival Time:")
        self.label_arrival.pack()
        self.entry_arrival = tk.Entry(self.inputs_frame)
        self.entry_arrival.pack()
        
        self.label_burst = tk.Label(self.inputs_frame, text="Burst Time:")
        self.label_burst.pack()
        self.entry_burst = tk.Entry(self.inputs_frame)
        self.entry_burst.pack()
        
        self.button_add_process = tk.Button(self.inputs_frame, text="Add Process", command=self.add_process)
        self.button_add_process.pack(pady=10)
        

        # default processes button
        self.button_default_processes = tk.Button(self.inputs_frame, text="Add Default Processes", command=self.add_default_processes)
        self.button_default_processes.pack(pady=10)


        # Checkboxs
        self.fcfs_checkbutton = tk.Checkbutton(self.inputs_frame, text="FCFS", variable=self.fcfs_checked)
        self.fcfs_checkbutton.pack()
        
        self.hrrn_checkbutton = tk.Checkbutton(self.inputs_frame, text="HRRN", variable=self.hrrn_checked)
        self.hrrn_checkbutton.pack()

        self.sjf_non_preemptive_checkbutton = tk.Checkbutton(self.inputs_frame, text="sjf (non preemptive)", variable=self.sjf_non_preemptive_checked)
        self.sjf_non_preemptive_checkbutton.pack()

        self.sjf_preemptive_checkbutton = tk.Checkbutton(self.inputs_frame, text="sjf (preemptive)", variable=self.sjf_preemptive_checked)
        self.sjf_preemptive_checkbutton.pack()

        self.ltf_checkbutton = tk.Checkbutton(self.inputs_frame, text="LTF", variable=self.ltf_checked)
        self.ltf_checkbutton.pack()

        self.rr_checkbutton = tk.Checkbutton(self.inputs_frame, text="RR", variable=self.rr_checked)
        self.rr_checkbutton.pack()

        self.priority_checkbutton = tk.Checkbutton(self.inputs_frame, text="PRIORITY", variable=self.priority_checked)
        self.priority_checkbutton.pack()

        # default processes for priority algo button
        self.button_priority_default_processes = tk.Button(self.inputs_frame, text="Add Default Processes for priority", command=self.add_priority_default_processes)
        self.button_priority_default_processes.pack(pady=10)


        # run algorithm button
        self.button_run_algorithm = tk.Button(self.inputs_frame, text="Run Algorithm", command=self.run_algorithm)
        self.button_run_algorithm.pack(pady=10)
        

        # clear button
        self.button_clear_list = tk.Button(self.inputs_frame, text="Clear List", command=self.clear_list)
        self.button_clear_list.pack(pady=10)
        
        # list frame
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Listbox and scrollbar
        self.process_list = tk.Listbox(self.list_frame)
        self.process_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.process_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.process_list.yview)
    
    def add_process(self):
        try:
            arrival_time = int(self.entry_arrival.get())
            burst_time = int(self.entry_burst.get())
            process_id = len(self.fcfs_processes) + 1
            
            fcfs_process = FcfsProcess(process_id, arrival_time, burst_time)
            hrrn_process = HrrnProcess(process_id, arrival_time, burst_time)
            sjf_non_preemptive_process = sjf_non_preemptive_Process(process_id, arrival_time, burst_time)
            sjf_preemptive_process = sjf_preemptive_Process(process_id, arrival_time, burst_time)
            ltf_process = LtfProcess(process_id, arrival_time, burst_time)
            rr_process = RoundRobinProcess(process_id, arrival_time, burst_time)

            self.fcfs_processes.append(fcfs_process)
            self.hrrn_processes.append(hrrn_process)
            self.sjf_non_preemptive_processes.append(sjf_non_preemptive_process)
            self.sjf_preemptive_processes.append(sjf_preemptive_process)
            self.ltf_processes.append(ltf_process)
            self.rr_processes.append(rr_process)
            
            # show added process on the list
            self.process_list.insert(tk.END, f"Process: {process_id}, Arrival Time: {arrival_time}, Burst Time: {burst_time}")
            
            self.entry_arrival.delete(0, tk.END)
            self.entry_burst.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Arrival Time and Burst Time.")
    
    def run_algorithm(self):
        avg_fcfs = 0
        avg_hrrn = 0
        avg_sjf_np = 0
        avg_sjf_p = 0
        avg_ltf = 0
        avg_rr = 0
        avg_priority = 0

        if (self.fcfs_checked.get() and self.fcfs_processes) or (self.hrrn_checked.get() and self.hrrn_processes) or (self.sjf_non_preemptive_checked.get() and self.sjf_non_preemptive_processes or (self.ltf_checked.get() and self.ltf_processes) or (self.priority_checked.get() and self.priority_processes) or (self.rr_checked.get() and self.rr_processes)) :
            if self.fcfs_checked.get():
                self.fcfs_result_list = fcfs_scheduling(self.fcfs_processes)
                self.average_waiting_time_fcfs = self.fcfs_result_list[-1]
                avg_fcfs = self.average_waiting_time_fcfs
                self.average_turn_around_time_fcfs = self.fcfs_result_list[-2]
                #messagebox.showinfo("FCFS Result", f"Average Waiting Time for FCFS: {self.average_waiting_time_fcfs}\nAverage Turn Around Time for FCFS: {self.average_turn_around_time_fcfs}")
                self.create_gantt_charts("FCFS", self.fcfs_result_list, -2,"Average Waiting Time: " + str(self.average_waiting_time_fcfs) + "\nAverage Turn Around Time: " + str(self.average_turn_around_time_fcfs))

            if self.hrrn_checked.get():
                self.hrrn_result_list = hrrn_scheduling(self.hrrn_processes)
                self.average_waiting_time_hrrn = self.hrrn_result_list[-1]
                avg_hrrn = self.average_waiting_time_hrrn
                self.average_turn_around_time_hrrn = self.hrrn_result_list[-2]
                self.average_response_ratio_hrrn = self.hrrn_result_list[-3]
                #messagebox.showinfo("HRRN Result", f"Average Waiting Time for HRRN: {self.average_waiting_time_hrrn}")
                self.create_gantt_charts("HRRN", self.hrrn_result_list, -3, "Average Waiting Time: " + str(self.average_waiting_time_hrrn) + "\nAverage Turn Around Time: " + str(self.average_turn_around_time_hrrn) + "\nAverage Response Ratio: " + str(self.average_response_ratio_hrrn))

            if self.sjf_non_preemptive_checked.get():
                self.sjf_non_preemptive_result_list = sjf_non_preemptive_scheduling(self.sjf_non_preemptive_processes)
                self.average_waiting_time_sjf_non_preemptive = self.sjf_non_preemptive_result_list[-1]
                avg_sjf_np = self.average_waiting_time_sjf_non_preemptive
                self.average_turn_around_time_sjf_non_preemptive = self.sjf_non_preemptive_result_list[-2]
                #messagebox.showinfo("sjf (non preemptive) Result", f"Average Waiting Time for sjf (non preemptive): {self.average_waiting_time_sjf_non_preemptive}")
                self.create_gantt_charts("sjf (non preemptive)", self.sjf_non_preemptive_result_list, -2, "Average Waiting Time: " + str(self.average_waiting_time_sjf_non_preemptive) + "\nAverage Turn Around Time: " + str(self.average_turn_around_time_sjf_non_preemptive))
            
            if self.sjf_preemptive_checked.get():
                self.sjf_preemptive_result_list = sjf_preemptive_scheduling(self.sjf_preemptive_processes)
                self.average_waiting_time_sjf_preemptive = self.sjf_preemptive_result_list[-1]
                avg_sjf_p = self.average_waiting_time_sjf_preemptive
                self.average_turn_around_time_sjf_preemptive = self.sjf_preemptive_result_list[-2]
                #messagebox.showinfo("sjf (preemptive) Result", f"Average Waiting Time for sjf (preemptive): {self.average_waiting_time_sjf_preemptive}")
                self.create_gantt_charts("sjf (preemptive)", self.sjf_preemptive_result_list, -2, "Average Waiting Time: " + str(self.average_waiting_time_sjf_preemptive) + "\nAverage Turn Around Time: " + str(self.average_turn_around_time_sjf_preemptive))
            
            if self.ltf_checked.get():
                self.ltf_result_list = ltf_scheduling(self.ltf_processes)
                self.average_waiting_time_ltf = self.ltf_result_list[-1]
                avg_ltf = self.average_waiting_time_ltf
                self.average_turn_around_time_ltf = self.ltf_result_list[-2]
                #messagebox.showinfo("LTF Result", f"Average Waiting Time for LTF: {self.average_waiting_time_ltf}")
                self.create_gantt_charts("LTF", self.ltf_result_list, -2, "Average Waiting Time: " + str(self.average_waiting_time_ltf) + "\nAverage Turn Around Time: " + str(self.average_turn_around_time_ltf))
            
            if self.rr_checked.get():
                self.rr_result_list = rr_scheduling(self.rr_processes)
                self.average_waiting_time_rr = self.rr_result_list[-1]
                avg_rr = self.average_waiting_time_rr
                #messagebox.showinfo("RR Result", f"Average Waiting Time for RR: {self.average_waiting_time_rr}")
                self.create_gantt_charts("RR", self.rr_result_list, -1, "Average Waiting Time: " + str(self.average_waiting_time_rr)) # "Average Waiting Time: " + str(self.average_waiting_time_rr)

            if self.priority_checked.get():
                self.priority_result_list = priority_scheduling(self.priority_processes)
                self.average_waiting_time_priority = self.priority_result_list[-1]
                avg_priority = self.average_waiting_time_priority
                self.average_turn_around_time_priority = self.priority_result_list[-2]
                #messagebox.showinfo("PRIORITY Result", f"Average Waiting Time for PRIORITY: {self.average_waiting_time_priority}")
                self.create_gantt_charts("PRIORITY", self.priority_result_list, -2, "Average Waiting Time: " + str(self.average_waiting_time_priority) + "\nAverage Turn Around Time: " + str(self.average_turn_around_time_priority))

            plt.show()

        data = {
            "algorithm": ["FCFS", "HRRN", "SJF(N-P)", "SJF", "LTF","RR", "PRIORITY"],
            "Average Waiting Time": [avg_fcfs, avg_hrrn, avg_sjf_np, avg_sjf_p, avg_ltf,avg_rr, avg_priority]
        }

        avg_wine_df = pd.DataFrame(data)

        plt.figure(figsize=(7, 6))

        plt.bar(x=avg_wine_df["algorithm"], height=avg_wine_df["Average Waiting Time"],
                width=0.85, color="tomato", edgecolor="black", linewidth=1.5
                )

        plt.xlabel("Algorithm")
        plt.ylabel("Average Waiting Times")

        plt.title("Average Waiting Times Per Algorithm", loc="left", fontdict=dict(fontsize=20, fontweight="bold"), pad=10)

        # Set y-axis ticks to display specific values
        plt.yticks([avg_fcfs, avg_hrrn, avg_sjf_np, avg_sjf_p, avg_ltf,avg_rr, avg_priority])

        plt.show()

    def create_gantt_charts(self, algorithm, result_list, x, y):
        # Extracting process data only
        process_data = result_list[:x]

        start_points = [item["Arrival Time"] for item in process_data[:1]] + [item["Completion Time"] for item in process_data[:-1]]

        data = {
            "Process": [item["Process"] for item in process_data],
            "BurstTimes": [item["Burst Time"] for item in process_data]
        }

        avg_wine_df = pd.DataFrame(data)

        start_points = start_points[:len(avg_wine_df)]

        plt.figure(figsize=(7, 7))
        plt.xlim(0, process_data[-1]["Completion Time"])
        plt.yticks([])

        process_colors = {
            1: 'blue',
            2: 'red',
            3: 'green',
            4: 'gray',
            5: 'brown',
            6: 'purple',
            7: 'orange',
            8: 'beige',
            9: 'maroon',
        }

        # Çubuk grafiğini çiz
        bars = plt.barh(y=[0] * len(avg_wine_df), width=avg_wine_df["BurstTimes"],
                        height=0.85, color=[process_colors[process] for process in avg_wine_df["Process"]],
                        edgecolor="black", linewidth=1.5, left=start_points
                        )

        # Eksen etiketlerini ayarla
        plt.xlabel(y)
        plt.ylabel("Processes")

        plt.title(algorithm + "'s Gantt Charts", loc="left", fontdict=dict(fontsize=20, fontweight="bold"), pad=10)

        # x ekseni etiketlerini belirli değerlere ayarla
        plt.xticks([0] + [item["Arrival Time"] for item in process_data[:1]] + [item["Completion Time"] for item in process_data])

        # Her bir sütunun içine hangi işlemin ait olduğunu yaz
        for bar, item, process in zip(bars, process_data, avg_wine_df["Process"]):
            plt.text((bar.get_x() + int(item["Completion Time"])) / 2, bar.get_y() + bar.get_height() / 2, str(process),
                    ha='center', va='center', color='white', fontweight='bold')

        # Show the plot
        #plt.show()

    def add_default_processes(self):
        if not self.process_list.get(0, tk.END):
            default_processes = [
                (1, 0, 6),
                (2, 2, 4),
                (3, 4, 2),
                (4, 6, 8),
                (5, 8, 10),
            ]
            for process_id, arrival_time, burst_time in default_processes:
                fcfs_process = FcfsProcess(process_id, arrival_time, burst_time)
                hrrn_process = HrrnProcess(process_id, arrival_time, burst_time)
                sjf_non_preemptive_process = sjf_non_preemptive_Process(process_id, arrival_time, burst_time)
                sjf_preemptive_process = sjf_preemptive_Process(process_id, arrival_time, burst_time)
                ltf_process = LtfProcess(process_id, arrival_time, burst_time)
                rr_process = RoundRobinProcess(process_id, arrival_time, burst_time)

                self.fcfs_processes.append(fcfs_process)
                self.hrrn_processes.append(hrrn_process)
                self.sjf_non_preemptive_processes.append(sjf_non_preemptive_process)
                self.sjf_preemptive_processes.append(sjf_preemptive_process)
                self.ltf_processes.append(ltf_process)
                self.rr_processes.append(rr_process)
                
                self.process_list.insert(tk.END, f"Process: {process_id}, Arrival Time: {arrival_time}, Burst Time: {burst_time}")
        else:
            messagebox.showinfo("Info", "Process list is not empty. Please clear the list before adding default processes.")

    def add_priority_default_processes(self):
        if not self.process_list.get(0, tk.END):
            default_processes = [
                (1, 0, 6, 3),
                (2, 2, 4, 2),
                (3, 4, 2, 5),
                (4, 6, 8, 1),
                (5, 8, 10, 4),
            ]
            for process_id, arrival_time, burst_time, priority in default_processes:
                priority_process = PriorityProcess(process_id, arrival_time, burst_time, priority)
                self.priority_processes.append(priority_process)
                
                self.process_list.insert(tk.END, f"Process: {process_id}, Arrival Time: {arrival_time}, Burst Time: {burst_time}, Priority: {priority}")
        else:
            messagebox.showinfo("Info", "Process list is not empty. Please clear the list before adding default processes.")

    def clear_list(self):
        self.process_list.delete(0, tk.END)
        self.fcfs_processes = []
        self.hrrn_processes = []
        self.sjf_non_preemptive_processes = []
        self.sjf_preemptive_processes = []
        self.ltf_processes = []
        self.rr_processes = []
        self.priority_processes = []

def main():
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()