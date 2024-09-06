# Docker-PythonCalc-project


Steps
----------
1. Install git in the VM
$ sudo apt install git -y

$ git --version

2. Clone the code to VM
$ git clone 

3. Change the directory
$ cd <DirectoryName>

4. Verify the contents
$ ls

5. To see the content available inside the dockerfile
$ cat <DockerfileName>

6. To build the docker image
$ docker build -t <ImageName> .

7. Verify the docker image creation
$ docker images

Now the image is available. Now, we have to run the docker image. Whenever we are running the docker image, we need to specify the port mapping.
Port Mapping?
In my VM, i have created the docker image, when i run this image, container will get created. Container is the run time environment of our app.

8. To run the docker image and to do the port mapping
$ docker run -d -p <HostPortNumber>:<ContainerPortNumber> <ImageName>

 -d represents the detached mode
 -p represents port mapping

$ docker run -d -p 5001:5000 python-app

# Access the application
<PublicIPofVM>:5001/

Before accessing the application, enable port number 5001 for the instance
Type: CustomTCP, Source: AnywhereIPv4, Port: 5001
