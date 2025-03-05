# Module 3

## Blue screen of death (BSoD)

A common disruption in computing systems is the kernel panic in Mac OS, also known as the notorious "Blue Screen of Death" (BSoD) in Windows, both of which require restarting the computer. Although rare, analyzing these occurrences is essential for uncovering OS issues. BSoDs are usually caused by hardware glitches, problematic drivers, or abrupt process terminations. These failure screens display error codes, memory locations, and technical insights related to the crash.

## Reading system logs

System logs are crucial for understanding and resolving issues across multiple operating systems. Whether you're using a Mac, Linux, or another system, delving into these logs can yield valuable insights. Analyzing logs is critical for identifying system errors and crashes on Windows computers. The Windows logs such as System and Application carefully record data retrieval events, providing insight into software, hardware, and user interaction.

### Mac System Logs

Mac system logs provide insights into system operations. By using the Console app, you can capture error messages, warnings, and interactions between hardware and software. These logs are especially useful when investigating system behavior.

### Linux System Logs

Linux system logs offer insights into troubleshooting. They give detailed information about the Linux environment, such as errors and hardware-software interactions. Using command-line utilities, you can access these logs to identify unusual behavior patterns. These logs provide a holistic overview of system performance.

## Process Monitor

Monitoring tools like Process Monitor in Windows provide real-time visibility into file system actions, registry changes, and process behavior. With features from legacy tools such as Regmon and Filemon, Process Monitor captures input/output parameters, uses non-destructive filtering, identifies root causes, and compiles comprehensive process data. This includes details such as image paths, commands, user information, and session IDs. The tool offers customizable columns, flexible filters, and scalable logging to enhance event management. Tooltips provide quick access to log files and reveal process relationships. It also records boot-time operations for comprehensive tracking, troubleshooting, malware detection, and system activity analysis.

## Linux strace command

You can use a Linux strace command to trace system calls and signals. It aids in debugging and diagnostics by analyzing application and process behavior. It captures system calls, pinpoints issues, optimizes code, and enhances system performance. You use strace by entering the program's name and any arguments at the command line. This tool logs detailed system call information, enabling you to analyze bottlenecks, unintended behaviors, and misconfigurations. The strace command contributes to a better understanding of OS and application interactions, ultimately leading to efficient software development and effective issue resolution.

## Tracing system calls

Tracing system calls on Linux is useful for identifying security risks and tracing system calls, which reveal the intricate interactions between processes and operating systems. You can trace a Linux system call using the ptrace API and the strace command, and you can trace a Mac OS X system call using the dtrace system. Windows uses the GUI tool Process Monitor, and additional projects enhance system call tracing. Tools like Logger, LogView, and NtTrace leverage Microsoft's Event Tracing for Windows (ETW) capabilities. Across operating systems, tracing system calls remains pivotal for development and monitoring, anchoring system analysis and optimization.
