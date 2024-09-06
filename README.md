This project demonstrates how to set up and run a Python-based calculator inside a Docker container. Follow the steps below to install the necessary tools, clone the repository, and run the project using Docker.

Prerequisites
A virtual machine (VM) or local environment with Docker installed.
Git installed on the VM.
Steps to Run the Project
1. Install Git in the VM
To install Git, use the following command:

bash
Copy code
$ sudo apt install git -y
Verify the installation:

bash
Copy code
$ git --version
2. Clone the Project Repository
Use Git to clone this repository to your VM:

bash
Copy code
$ git clone <RepositoryURL>
3. Change Directory to the Project Folder
Navigate to the cloned repository's directory:

bash
Copy code
$ cd <DirectoryName>
4. Verify the Project Files
Check the contents of the directory to ensure the files have been copied:

bash
Copy code
$ ls
5. View the Dockerfile Contents
To understand how the Docker image will be built, check the contents of the Dockerfile:

bash
Copy code
$ cat <DockerfileName>
6. Build the Docker Image
Build the Docker image from the Dockerfile by running:

bash
Copy code
$ docker build -t <ImageName> .
Example:

bash
Copy code
$ docker build -t python-app .
7. Verify the Docker Image
After the image is built, verify it was created successfully by listing the Docker images:

bash
Copy code
$ docker images
8. Run the Docker Container with Port Mapping
To run the Docker container from the image and perform port mapping, use:

bash
Copy code
$ docker run -d -p <HostPortNumber>:<ContainerPortNumber> <ImageName>
-d runs the container in detached mode.
-p sets up port forwarding between the host and container.
Example:

bash
Copy code
$ docker run -d -p 5001:5000 python-app
In this example, the application inside the container listens on port 5000, and you access it via port 5001 on the host.

9. Access the Application
After running the container, access the application by opening the following URL in your browser:

arduino
Copy code
http://<PublicIPofVM>:5001/
Note: Before accessing the application, make sure to enable port 5001 in your VM's security group settings:

Type: Custom TCP
Source: Anywhere (0.0.0.0/0)
Port: 5001
Screenshot
![Screenshot 2024-09-06 173302](https://github.com/user-attachments/assets/ec7a40a6-8a51-443b-9034-447e093a5685)


This structure clearly defines each step and includes important explanations for port mapping and security group settings. You can replace placeholders like <DirectoryName>, <DockerfileName>, <ImageName>, and <RepositoryURL> with the actual values from your project.
