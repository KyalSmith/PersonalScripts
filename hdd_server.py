import socket
import os
import sys
import threading
import time

messages = ""

def main():

    try:

        interface = sys.argv[1]
        print(interface)



        interface_data = str(os.popen("ifconfig").read())
        interface_data = interface_data.split()


        for count,val in enumerate(interface_data):


            if val == interface:
                interface_data = interface_data[count:]
                break



        ip = interface_data[6][5:]

        server_thread = threading.Thread(target=Connect,args=(ip))
        email_thread = threading.Thread(target=Email)

        server_thread.start()
        email_thread.start()



    except Exception as e:
        print("Exception:\t" + e)






def Connect(ip):

    global messages

    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)

    socket_server.bind((ip,65000))

    socket_server.listen(5)
    conn,addr = socket_server.accept()

    while True:

        hd_status = conn.recv(1024)

        messages +=  hd_status.decode() + "\n\n\n"



def Email():

    global messages

    while True:

        time.sleep(5)

        if messages:

            command = "echo \'" + messages + "\' | mail -s \"Warning Hardrive Space!\" kyal.smith@spree.co.za"

            os.system(command)

            messages = ""




if __name__=="__main__":
    main()