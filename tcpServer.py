import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(bind_ip, bind_port))

def get_mail_id():
    with open("id.txt","r") as ids:
        findId = ids.readlines()
        mailid = findId[0]
        return mailid

def update_id():
    old_id = get_mail_id()
    new_id = int(old_id) +1
    with open("id.txt","w") as ids:
        ids.write(str(new_id))

def send_mail(content,client_socket):
    parse = content.split("#!")
    print(parse)
    userMail = parse[1]
    mailTo = parse[2]
    header = parse[3]
    mailContent = parse[4]

    with open("mails.txt","a") as mails:
        mails.write("\n" +get_mail_id()+"\n" + userMail + "\n" + mailTo +"\n"+header+"\n"+mailContent+"\n")

    update_id()
    client_socket.send(bytes('SUCCESS',encoding="utf-8"))

def del_mail(content,client_socket):
    with open("mails.txt", "r") as mails:
        lines = mails.readlines()
        for lineid in range(0, len(lines)):
            if lineid % 6 == 1:
                mail_id = lines[lineid]
                deleting_id = content+"\n"
                print(deleting_id)
                if mail_id == deleting_id:
                    writing = "#"+content+"\n"
                    lines[lineid] = writing
                    with open('mails.txt', 'w') as file:
                        file.writelines(lines)

def get_mails(content,client_socket):
    with open("mails.txt", "r") as mails:
        allMails = mails.read()
        client_socket.send(bytes(allMails, encoding="utf-8"))


def handle_client_connection(client_socket):
    request = client_socket.recv(1024).decode("ASCII")
    print('Received {}'.format(request))
    print(request)
    #client_socket.send(bytes('ACK!',encoding="utf-8"))
    if request[0:3] == "SND":
        send_mail(request[3:],client_socket)
    if request[0:3] == "DEL":
        print("sdasdsadasda" +request[5:])
        del_mail(request[5:],client_socket)
    if request[0:3] == "GET":
        get_mails(request[3:],client_socket)
    client_socket.close()
    print("socket closed")
    server.accept()

while True:
    client_sock, address = server.accept()
    print('Accepted connection from {}:{}'.format(address[0], address[1]))

    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)
    )
    client_handler.start()

