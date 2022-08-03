cpu_workloads = {}

with open("cpu-results.txt") as file:
    for line in file:
       (workloadname, cpuvalue) = line.split()
       cpu_workloads[workloadname] = cpuvalue

print(len(cpu_workloads))