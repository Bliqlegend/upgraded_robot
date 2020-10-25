import os
import re

import docker


def options():

    print("Options Menu  : \n")
    l = [
        "Deploy an Instance",
        "Copy Code files to Backupdir",
        "Exec into terminal",
        "Run a certain Command",
        "Delete any instance",
        "Get container IP",
        "SSH into the container",
        "Commit to DockerHub",
        "Check How many instances are running",
        "Deploy a temporary instance",
    ]
    n = 1
    for i in l:
        print(f"{n}. {i}")
        n += 1
    num = int(input("\nEnter Your Choice : "))
    name = input("Enter the Default container Name : ")
    return num, name


def deploy_an_instance(name):
    os.system("clear")
    print("Deploying an instance with Arbitraty name and 8080,2222")
    os.system("docker pull cultholmes/progressive_minds")
    os.system(
        "docker run -dit --privileged --security-opt seccomp=unconfined -h {'$USER'} -p 8080:80 -p 2222:22 -e ALLOWED_NETWORKS=0.0.0.0/0 cultholmes/progressive_minds"
    )
    print("Done")
    num = options()
    return num


def copy_code_backup(name):
    os.system("clear")
    print("Copying all the files to home Directory")
    l = os.popen("docker inspect --format='{{.Id}}' " + name)
    brr = l.read()
    os.system(f"docker cp {brr}:/root/code ~/")
    print("Done")
    num = options()
    return num


def exec_into_terminal(name):
    os.system("clear")
    print("Execing into terminal")
    os.system(f"docker exec -it {name} bash")


def run_a_certain_command(name):
    os.system("clear")
    print("Execing into terminal")
    command = input("Enter the command : ")
    os.system(f"docker exec -it {name} ")


def delete_an_instance(name):
    os.system("clear")
    print("Deleting an instance")
    l = os.popen("docker inspect --format='{{.Id}}' " + name)
    brr = l.read()
    os.system(f"docker rm -f {brr}")
    print("Done")
    num = options()
    return num


def get_continer_ip(name):
    os.system("clear")
    print("Getting the IP of default container")
    l = os.popen("docker inspect --format='{{.Id}}' " + name)
    brr = l.read()
    os.system(
        "docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "
        + name
    )
    num = options()
    return num


def ssh_into_the_container(name):
    os.system("clear")
    print("Interactive shell will be started , Password: toor")
    os.system("ssh root@localhost -p 2222")


def commmit_to_docker_hub(name):
    os.system("clear")
    id = input("Enter your Docker ID/Username: ")
    os.system(f"docker tag {name} {id}/progressive_minds ")
    os.system(f"docker push {id}/progressive_minds ")


def deploy_a_temp_instance(name):
    os.system("clear")
    print("Deploying an instance with Arbitraty name and 8080,2222")
    os.system(" docker pull cultholmes/progressive_minds")
    os.system(
        "docker run -it --rm --privileged --security-opt seccomp=unconfined -h {'$USER'} -p 8080:80 -p 2222:22 -e ALLOWED_NETWORKS=0.0.0.0/0 cultholmes/progressive_minds"
    )
    print("Done")
    num = options()
    return num


def check_num_intances():
    os.system("clear")
    print("Deleting an instance")
    l = os.popen("docker ps")
    num = options()
    return num


if __name__ == "__main__":
    num, name = options()
    # num = copy_code_backup()
    if num == 1:
        num = deploy_an_instance(name)
    elif num == 2:
        num = copy_code_backup(name)
    elif num == 3:
        num = exec_into_terminal(name)
    elif num == 4:
        num = run_a_certain_command(name)
    elif num == 5:
        num = delete_an_instance(name)
    elif num == 6:
        num = get_continer_ip(name)
    elif num == 7:
        num = ssh_into_the_container(name)
    elif num == 8:
        num = commmit_to_docker_hub(name)
    elif num == 9:
        num = check_num_intances(name)
    elif num == 10:
        num = deploy_a_temp_instance(name)
    else:
        print("You really gonna play bitc?")
