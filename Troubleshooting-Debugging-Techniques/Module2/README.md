# Monitoring tools

## Windows processes

Windows Process Monitor, also known as Sysinternals, is a powerful monitoring tool that serves as an advanced task manager. It provides real-time insight into various aspects of the system, including file system operations, registry changes, processes, and threads. The tool excels at diagnosing file access issues, analyzing system configurations, and understanding processes.

## Linux performance

To enhance your Linux system's performance, you can use specialized tools that offer real-time insights into CPU, memory, disk I/O, and network activity for quick performance bottleneck detection. Some of these tools include Perf-tools, bcc/BPF, and bpftrace.

### The USE method

The USE Method is essential for optimizing system performance and troubleshooting servers. It helps identify resource bottlenecks and performance issues by analyzing Utilization, Saturation, and Errors. Resources like CPUs, memory, storage, and network interfaces can be measured for busy time, additional workload capacity, and errors.

## macOS Activity Monitor

Activity Monitor in macOS allows you to monitor and manage system performance easily. You can optimize Mac performance with Activity Monitor's insights into process activity, resource usage, and energy consumption. Activity Monitor identifies unresponsive apps or processes, monitors energy usage, tracks overall energy impact, and displays real-time system status. It enables you to troubleshoot issues and optimize battery life, ensuring smooth and responsive operation.

## Windows Performance Monitor

Performance Monitor is a versatile and customizable tool that analyzes your system's performance. By identifying and resolving hardware problems, poorly designed apps, excessive resource usage, or malware, it ensures smooth and efficient operation. Having real-time data on memory, network, disks, and processors lets you monitor key components and quickly resolve problems. You can configure counters, set data collectors, and analyze reports to optimize your system.

## Windows Resource Monitor

To get real-time insights into your computer's resource usage in Windows, use the Resource Monitor (resmon.exe) tool. It helps identify causes of slowdowns like hardware issues, poorly designed apps, and malware. Access it by searching for "resmon" or "Resource Monitor." Navigate between Memory, Disk, and Network sections for deeper analysis. Be cautious with CPU processes to avoid system instability.

## Windows Process Explorer

The Process Explorer v17.05 software is primarily used for file monitoring and analyzing processes on Windows computers. It provides detailed information about active processes, handles, and DLLs. Processes and their accounts are displayed in the top window, while handles and DLLs are displayed in the bottom window. In addition to troubleshooting DLLs, it also helps detect leaks and issues, providing valuable insights into how the system works.

## Caching

Although a cache is not a monitoring tool, it's important not to overlook them as computing relies heavily on caches, which enhance data access speed and overall system performance. They store frequently accessed data for quick retrieval, making them essential for CPUs, SSDs, HDDs, web browsers, and web servers. Caches are smaller and faster than memory, acting as intermediate storage to optimize efficiency.

## Linux autogrouping

In Linux, autogrouping optimizes desktop performance during CPU-intensive workloads by grouping processes and ensuring fair CPU cycle distribution. Autogrouping tells the process scheduler component in Linux to act based on a group’s configured “nice level” instead of individual processes. However, autogrouping can interfere with traditional processes. When enabled, the ”nice” value primarily affects priority within the group, reducing the effectiveness of “nice” and ”renice” commands. Even programs setting their own nice levels may still receive a "fair" share of CPU time.

### Terms and definitions

Activity Monitor: Mac OS tool that shows what's using the most CPU, memory, energy, disk, or network

Cache: This stores data in a form that's faster to access than its original form

Executor: This is the process that's in charge of distributing the work among the different workers

Expensive actions: Actions that can take a long time to complete

Futures: A module provides a couple of different executors, one for using threads and the other one for using processes

Lists: Sequences of elements

Memory leak: This happens when a chunk of memory that's no longer needed is not released

Profiler: A tool that measures the resources the code is using to see how the memory is allocated and how the time is spent

Real time: The amount of actual time that it took to execute the command

Resource Monitor (or Performance Monitor): Windows OS tool that shows what's using the most CPU, memory, energy, disk, or network
