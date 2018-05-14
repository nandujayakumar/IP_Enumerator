from netaddr import IPNetwork
import subprocess


def ping_request():
	with open('Block.txt','r') as obj:
		for line in obj:
			pro = subprocess.Popen(['ping','-n','1',line] , stdout=subprocess.PIPE).communicate([0])
			print (pro)
			

def host_finder(block):
    for ip in IPNetwork(block).iter_hosts():
        with open('Block.txt', 'a') as File_obj:
            File_obj.write(str(ip) + "\n")


def main():
    File_path = input("Enter the path to the Network block list\n")
    try:
        with open(File_path, 'r') as file_object:
            for line in file_object:
                host_finder(line)
    except FileNotFoundError:
        print("Invalid Path !\tPlease enter a valid path")

main()
ping_request()
