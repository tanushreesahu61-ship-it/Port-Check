import socket
# Converting Domain name into IP Address
domain = input("Enter the Domain name -> ")
try:
    ip = socket.gethostbyname(domain)
    print("IP Adress -> ",ip)
except socket.gaierror:
    print("Could not find the IP Address...")

# Choose Ports
def check_port(ip):
    print("Enter the Service name\nFor Example: HTTP, HTTPS, SSH, FTP, domain, SMTP, IMAP, POP3, Telnet, ms-wbt-server")
    service = input("Service -> ")
    try:
        port = socket.getservbyname(service,"tcp")
        print("Port Number -> ",port)
    except OSError:
        print("Invalid Service")
        return

    # For Connection
    socket.setdefaulttimeout(3)
    s = socket.socket()
    try:
        connect = s.connect((ip,port))
        print("Port is Open")
    except ConnectionRefusedError:
        print("Port is Closed")
    except socket.timeout:
        print("Connection Time out")
    except socket.error as e:
        print("Connection Failed",e)
    finally:
        s.close()
while True:
    check_port(ip)
while True:
    choise = input("Do you want to Scan another Domain? (yes or no) -> ")
    if choise.lower() == "yes":
        domain = input("Enter the Domain name -> ")
        try:
            ip = socket.gethostbyname(domain)
            print("IP Adress -> ",ip)
            check_port(ip)
        except socket.gaierror:
            print("Could not find the IP Address...")
    else:
        break
    choise = input("Do you want to Scan another Port? (yes or no) -> ")
    if choise.lower() == "yes":
        continue
    else:
        break
