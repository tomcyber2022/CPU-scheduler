# CPU-scheduler
Implementing various CPU scheduling algorithms in C++ is a great way to grasp the impact of different scheduling methods on system performance and efficiency. Below is a C++ program with frontend for inputs and outputs in python that illustrates the implementation of each specified CPU scheduling algorithm: First Come First Serve (FCFS), Round Robin (RR), Shortest Process Next (SPN), Shortest Remaining Time (SRT), Highest Response Ratio Next (HRRN), Feedback (FB), and Aging. 

# Algorithms

### **First Come First Serve (FCFS)**
- Processes are executed in the order they arrive in the ready queue. The CPU picks the first process in the queue and executes it until completion. Once a process starts, it runs to completion without interruption.

### **Round Robin (RR)**
- Each process is given a fixed time slice (quantum). Processes are placed in a circular queue. The CPU executes the first process for one quantum and then moves it to the back of the queue if it’s not finished. This cycle continues until all processes are completed.

### **Shortest Process Next (SPN)**
- At each scheduling decision point, the process with the shortest burst time is selected from the queue. The selected process is then executed to completion. This algorithm is non-preemptive, meaning a running process isn’t interrupted until it finishes.

### **Shortest Remaining Time (SRT)**
- A preemptive version of SPN, where the process with the shortest remaining execution time is selected. If a new process arrives with a shorter remaining time than the current process, the CPU switches to the new process. The CPU continuously checks for the shortest remaining time and switches accordingly.

### **Highest Response Ratio Next (HRRN)**
- Each process’s response ratio is calculated using the formula: \(\text{Response Ratio} = \frac{(Waiting Time + Burst Time)}{Burst Time}\). At each scheduling decision, the process with the highest response ratio is selected. This balances waiting time and burst time to decide the next process. It is non-preemptive, so once a process starts, it runs to completion.

### **Feedback (FB)**
- Processes are placed into multiple queues with different priority levels. New processes start in the highest priority queue. Processes in higher priority queues are given CPU time before those in lower-priority ones. If a process uses its allocated time slice without completing, it is moved to a lower-priority queue. Higher priority processes can interrupt lower priority ones.

### **Aging**
- Processes have a priority that increases as they wait in the queue. This increased priority can be a function of waiting time or other criteria. Over time, even low-priority processes become high-priority, ensuring they eventually get CPU time. The scheduler uses the updated priorities to decide which process to run next.


### Input Format Instructions

- **field 1:** Indicates whether to produce a "trace" (step-by-step execution details) or "stats" (summary statistics) for the simulation.

- **field 2:** Lists the CPU scheduling policies to be analyzed, separated by commas. Each policy may have parameters:
   - Each algorithm is represented by a number, as listed in the introduction.
   - For Round Robin and Aging, specify the quantum \( q \) as part of the policy, e.g., `2-4` for Round Robin with \( q=4 \) and `8-1` for Aging with \( q=1 \).

   **Algorithms:**
   - FCFS (First Come First Serve)
   - RR (Round Robin)
   3 SPN (Shortest Process Next)
   4 SRT (Shortest Remaining Time)
   5 HRRN (Highest Response Ratio Next)
   6 FB-1 (Feedback where all queues have \( q=1 \))
   7 FB-2i (Feedback where \( q=2^i \))
   8 Aging

- **field 3:** An integer representing the last instant for the simulation, shown on the timeline.

- **field 4:** An integer indicating the number of processes to be simulated.

- **Starting from field 5:** Each process is described on a separate line with comma-separated values:
   - For algorithms 1 to 7, include:
     1. Process name (string)
     2. Arrival time
     3. Service time

   - For the Aging algorithm (algorithm 8), include:
     1. Process name (string)
     2. Arrival time
     3. Priority

**Note:**:
-Processes are listed by arrival time. If arrival times are the same, processes with lower priority come first.
-last instant should be greater or equal to sum of execution times of all process.
-Inputs should strictly be given according to the format.


# Execution:
1. Clone the repo
2. Compile the code using `make` command
3. Run `Python3 frontend.py` in terminal


