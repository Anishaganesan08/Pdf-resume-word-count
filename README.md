## TERMINAL

docker pull ubuntu:

“docker pull“ is a command to download a docker image.  Here  docker pull ubuntu is a command with default configuration to download a ubuntu image.

docker image ls:

This command lists the images stored in the docker repository.
Here this command is used to check whether the ubuntu image has downloaded.

docker ps :

This command used to list the containers.

docker run -it -p 8888:8888 --name sample ubuntu:

The command docker run is used to start and run the containers.
The command -it is used to type commands on container.


## DOCKER TERMINAL
 
"apt get update" is a command used to update the package.
"apt-get install python3-pip" command used to install pip.
"pip3 install jupyter" command used to install notebook.
"jupyter-notebook --version" command used to see the notebook version.
"jupyter-notebook --allow-root --ip=0.0.0.0" command used to run the notebook via browser.


# Pdf-resume-word-count

"!pip install PyPDF2" the PyPDF2 is a python library for working with PDF documents.

# PYTHON CODE

from PyPDF2 import PdfReader

reader=PdfReader('/media/Anisha resume final1.pdf')

page=reader.pages[0]

text=page.extract_text()

words=text.split()
print(len(words))
