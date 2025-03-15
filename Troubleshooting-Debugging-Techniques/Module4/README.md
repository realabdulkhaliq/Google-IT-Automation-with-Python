## When to use (or not use) Docker

Docker is a containerization platform that bundles applications and their dependencies into portable containers, which simplifies deployment and ensures consistent performance across environments.

You should use Docker when:

The application you want to run has already been packaged as containers, or

You are developing a complex application across multiple teams, such as a microservice-based app, or

You're running an application at internet scale across hundreds or thousands of servers.

You may not want to use Docker when:

You’re planning to use Kubernetes, which now prefers new container engines like containerd, or

You are running a huge, monolithic legacy application written in something like Java.

## Terms and definitions

Bandwidth: How much data can be sent or received in a second

Centralized logs collection: This means there's a special server that gathers all the logs from all the servers, or even all computers in the network

Decorator: Used in Python to add extra behavior to functions without having to modify the code

Exhausted: When resources are used completely and programs are getting blocked by not having more access to those resources

Garbage collector: A tool in charge of freeing the memory that's no longer in use

Latency: The delay between sending a byte of data from one point and receiving it on the other

Memory profiler: A tool used to figure out how the memory is being used

Reproduction case: A clear description of how and when the problem appears, a way to verify if the problem is present or not
