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
