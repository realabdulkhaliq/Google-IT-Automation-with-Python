# Pointers for Getting Your Environment Setup

### Learning more about operating systems

We’ve talked briefly about what an operating system is and what we'll need to know about operating systems for this course. If you want to learn some additional operating system concepts, check out the videos on this subject in the [Technical Support Fundamentals](https://www.coursera.org/learn/technical-support-fundamentals) course. If you want to explore how to manage Windows and Linux, check out the [Operating Systems and You: Becoming a Power User](https://www.coursera.org/learn/os-power-user) course.

### Installing Python and additional modules

If you don't have Python installed yet, we recommend that you visit the
official [Python website](http://www.python.org/) and download the installer that corresponds to your operating system.

There’s a bunch of guides out there for installing Python and they all follow a similar process to the one we described in the videos. This [guide from Real Python](https://realpython.com/installing-python/) includes instructions on how to install python on a range of different operating systems and distributions.

Once you have Python installed on your operating system, it's a good idea to familiarize yourself with pip and the associated tools. You can find more info about these [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Using package management systems

Package management systems help you better manage the software installed on your machine. These management systems vary a lot from operating system to operating system. So, you need to pick the one that works for the OS you’re using. Check out these guides for help with this:

- [Installing Python 3 on Windows 10 with Chocolatey](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

- [Installing Python 3 on MacOS with Homebrew](https://programwithus.com/learn/python/install-python3-mac)

- [Package management basics on Linux](https://www.digitalocean.com/community/tutorials/package-management-basics-apt-yum-dnf-pkg)

### Other information

- [Python in the Microsoft Store for Windows 10](https://devblogs.microsoft.com/python/python-in-the-windows-10-may-2019-update/)

# Setting up Your Environment

After you’ve installed Python and checked that it works, the next step to set up your developer environment is to choose your main code editor. You’ve explored some code editors in Course 1.

Here are some additional common editors for Python, available for all platforms:

- [Eclipse](http://www.eclipse.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Sublime Text](http://www.sublimetext.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

You can read more about these editors, and others, in these overview comparatives:

## [Python IDEs and Code Editors (Guide)](https://realpython.com/python-ides-code-editors-guide/#pycharm)

This site compares tools that are built exclusively for Python code development and tools built for general development that you can use for Python and explains the pros and cons of each tool.

## [Best Python IDEs and Code Editors](https://www.softwaretestinghelp.com/python-ide-code-editors/)

This site explains the importance of an integrated development environment (IDE) and compares a number of Python IDEs and code editors that can be used on platforms such as Windows, Mac, or Linux.

## [Top 6 Python IDEs for Data Science](https://www.datacamp.com/community/tutorials/data-science-python-ide)

This site reviews common IDEs in terms of functionality to benefit projects for data scientists.

We encourage you to try out these editors and pick your favorite. Then, install it on your computer and experiment with writing and executing Python scripts locally. To review best practices for using and saving Python files, check out the following:

- [Review: Use the command-line](https://www.coursera.org/learn/python-crash-course/supplement/vBqPl/review-use-the-command-line)
- [Use the command-line](https://www.coursera.org/learn/python-crash-course/lecture/Kz1Qr/use-the-command-line)
- [Review: Use JupyterLab and Jupyter Notebooks](https://www.coursera.org/learn/python-crash-course/supplement/C2ll0/review-use-jupyterlab-and-jupyter-notebooks)
- [Use JupyterLab and Jupyter Notebooks](https://www.coursera.org/learn/python-crash-course/lecture/e9iE9/use-jupyterlab-and-jupyter-notebooks)
- [Review: Use Colab](https://www.coursera.org/learn/python-crash-course/supplement/xgTqT/review-use-colab)
- [Use Colab](https://www.coursera.org/learn/python-crash-course/lecture/563SQ/use-colab)
- [Review: Use VS Code](https://www.coursera.org/learn/python-crash-course/supplement/gcQVZ/review-use-vs-code)
- [Use VS Code](https://www.coursera.org/learn/python-crash-course/lecture/DQhOO/use-vs-code)
- [More on IDEs and code editors](https://www.coursera.org/learn/python-crash-course/supplement/5KUxr/more-on-ides-and-code-editors)

# Virtual environments

A virtual environment in Python is a powerful tool that allows you to create isolated environments for your Python projects. Each environment acts as a sandbox, containing its own Python interpreter and library installations. This means you can have multiple projects with different dependencies, ensuring that they do not interfere with each other. In essence, virtual environments provide a clean slate where you can work on your projects without worrying about conflicting libraries or versions.

Why use a virtual environment in Python?
Imagine you're working on two separate Python projects—one requires a specific version of a library, while the other relies on a newer version. Without virtual environments, managing these dependencies could become a nightmare. Here's where virtual environments shine: they allow you to keep your projects isolated, ensuring that changes in one environment do not impact another.

By using virtual environments, you can:

Avoid conflicts between libraries and dependencies.

Test different versions of libraries without affecting your system-wide Python installation.

Maintain a clean and organized development environment.

Collaborate with others while ensuring consistent library versions.

Using a Python virtual environment
Creating and using a virtual environment is a straightforward process. To create a virtual environment, open your terminal and navigate to your project's directory. Then, run the following command:

`python -m venv myenv`

This command creates a virtual environment named "myenv" in your project directory. To activate the virtual environment, use the appropriate command for your operating system:

On Windows:

`myenv\Scripts\activate`

On macOS and Linux:

`myenv/bin/activate`

Once activated, your terminal prompt will change, indicating that you are now working within the virtual environment. You can now install packages using pip just like you normally would.

### Best practices and recommendations

As you dive into the world of virtual environments, keep these best practices in mind:

**Create a virtual environment for each project:** Whenever you start a new project, create a new virtual environment. This ensures a clean and isolated workspace.

**Use requirements files:** To document and manage your project's dependencies, create a requirements.txt file. This file lists all the libraries and their versions. You can generate it using `pip freeze > requirements.txt` and later install them in a new environment using `pip install -r requirements.txt`.

**Activate and deactivate:** Always activate the appropriate virtual environment before working on a project and deactivate it when you're done. This prevents confusion and potential conflicts.

**Version control:** If you're collaborating with others, include the virtual environment setup instructions in your version control system. This ensures everyone is using the same environment.

**Upgrade pip and setuptools:** When you create a new virtual environment, it's a good practice to upgrade pip and setuptools to the latest version. This ensures you're using the most up-to-date tools.

### Key takeaways

Virtual environments are your key to maintaining a clean and efficient Python development workflow. By isolating your projects, you can work confidently, test various libraries, and ensure consistency across your codebase. With this newfound knowledge, you're well on your way to mastering the art of running Python locally and building robust applications.

https://docs.python.org/3/library/venv.html
