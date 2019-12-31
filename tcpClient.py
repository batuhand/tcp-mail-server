import socket

host = '0.0.0.0'
port = 9999


def send_mail(userMail, mailTo, header, content):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sendContent = "SND" + "#!" + userMail + "#!" + mailTo + "#!" + header + "#!" + content
    client.connect((host, port))
    client.send(bytes(sendContent, encoding="utf-8"))
    response = client.recv(4096).decode("ASCII")
    print(response)
    client.close()


def get_mails(userMail):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sendContent = "GET" + "#!" + userMail
    client.connect((host, port))
    client.send(bytes(sendContent, encoding="utf-8"))
    response = client.recv(4096).decode("ASCII")
    print(response)
    client.close()


def delete_mail(mailId):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sendContent = "DEL" + "#!" + mailId
    client.connect((host, port))
    client.send(bytes(sendContent, encoding="utf-8"))
    response = client.recv(4096).decode("ASCII")
    print(response)
    client.close()





while True:
    print("Welcome to Batu Mail Service \n1- Send Mail\n2- Get Mails\n3- Delete Mail")
    choice = input()
    if choice == "1":
        userMail = input("Your mail adress: ")
        mailTo = input("Receivers mail adress: ")
        header = input("Mail header: ")
        content = input("Mail content: ")
        send_mail(userMail,mailTo,header,content)


    elif choice=="2":
        userMail = input("Your mail adress")
        get_mails(userMail)

    elif choice=="3":
        mailId = input("Mail id: ")
        delete_mail(mailId)

