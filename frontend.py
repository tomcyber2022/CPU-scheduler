import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import os

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduler Frontend")

        # Input mode
        self.lbl_mode = tk.Label(root, text="Mode ('trace' or 'stats'):")
        self.lbl_mode.grid(row=0, column=0, padx=10, pady=5)
        self.ent_mode = tk.Entry(root)
        self.ent_mode.grid(row=0, column=1, padx=10, pady=5)

        # Scheduling policies
        self.lbl_policies = tk.Label(root, text="Scheduling policies:")
        self.lbl_policies.grid(row=1, column=0, padx=10, pady=5)
        self.ent_policies = tk.Entry(root)
        self.ent_policies.grid(row=1, column=1, padx=10, pady=5)

        # Last instant
        self.lbl_last_instant = tk.Label(root, text="Last instant:")
        self.lbl_last_instant.grid(row=2, column=0, padx=10, pady=5)
        self.ent_last_instant = tk.Entry(root)
        self.ent_last_instant.grid(row=2, column=1, padx=10, pady=5)

        # Number of processes
        self.lbl_num_processes = tk.Label(root, text="Number of processes:")
        self.lbl_num_processes.grid(row=3, column=0, padx=10, pady=5)
        self.ent_num_processes = tk.Entry(root)
        self.ent_num_processes.grid(row=3, column=1, padx=10, pady=5)

        # Processes input
        self.lbl_processes = tk.Label(root, text="Process details (one per line):")
        self.lbl_processes.grid(row=4, column=0, padx=10, pady=5)
        self.txt_processes = scrolledtext.ScrolledText(root, width=40, height=10)
        self.txt_processes.grid(row=4, column=1, padx=10, pady=5)

        # Compile and Run button
        self.btn_compile_run = tk.Button(root, text="Compile & Run Scheduler", command=self.compile_and_run)
        self.btn_compile_run.grid(row=5, column=1, padx=10, pady=5, sticky=tk.E)

        # Output display
        self.lbl_output = tk.Label(root, text="Scheduler Output:")
        self.lbl_output.grid(row=6, column=0, padx=10, pady=5)
        self.txt_output = scrolledtext.ScrolledText(root, width=40, height=10)
        self.txt_output.grid(row=6, column=1, padx=10, pady=5)

    def compile_scheduler(self):
        # Compile the C++ scheduler using g++
        try:
            process = subprocess.Popen(
                ['g++', '-std=c++20', '-Wall', '-o', 'scheduler', 'scheduler.cpp'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                return False, stderr.strip()
            return True, stdout.strip()
        except Exception as e:
            return False, str(e)

    def run_scheduler(self, input_data):
        # Run the compiled C++ scheduler
        try:
            process = subprocess.Popen(
                ['./scheduler'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input_data)

            if process.returncode != 0:
                return False, stderr.strip()
            return True, stdout.strip()
        except Exception as e:
            return False, str(e)

    def compile_and_run(self):
        # Step 1: Compile the scheduler
        compiled, message = self.compile_scheduler()
        if not compiled:
            messagebox.showerror("Compilation Error", f"Failed to compile scheduler:\n{message}")
            return

        # Step 2: Get input data from the GUI
        mode = self.ent_mode.get().strip()
        policies = self.ent_policies.get().strip()
        last_instant = self.ent_last_instant.get().strip()
        num_processes = self.ent_num_processes.get().strip()
        processes = self.txt_processes.get("1.0", tk.END).strip()

        if not all([mode, policies, last_instant, num_processes, processes]):
            messagebox.showwarning("Input Error", "All fields must be filled.")
            return

        input_data = f"{mode}\n{policies}\n{last_instant}\n{num_processes}\n{processes}"

        # Step 3: Run the scheduler
        executed, output = self.run_scheduler(input_data)
        if not executed:
            messagebox.showerror("Execution Error", f"Failed to run scheduler:\n{output}")
            return

        # Step 4: Display the output
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, output)

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()
