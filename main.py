#!/usr/bin/env python3

"""  
Python Problem Statement :

Task 1: Ask the user to input 10 ipv4 addresses.
Task 2: Check if the addresses are valid ipv4 addresses.
Task 3: Convert the ipv4 addresses which are in decimal format to Binary, Octal and Hexadecimal format
For conversion use functions (inbuilt or library)
Task 4: Create a list which will hold the addresses. [Decimal, Binary, Octal and Hexadecimal]
Task 5: Transfer the contents of the list to a file named conversion.txt
Task 6: Print the following output on the screen
--------------------------------------------------------------------------------------
<The first IP address in Decimal, Binary, Octal and hexadecimal format is <output from the file conversion. txt>
<The second IP address in Decimal, Binary, Octal and hexadecimal format is <output from the file conversion. txt>
<The tenth IP address in Decimal, Binary, Octal and hexadecimal format is <output from the file conversion. txt> 
"""

val = int(input("How many IPs you want to check : "))

valid_IP = []

for v in range(val):
    IP = input("Enter IP Address : ")

    def valid(IP):
        
        ip = IP.split('.')
        if len(ip) != 4:
            return
            
        for i in ip:
            if not isinstance(int(i), int):
                return
                
            if int(i) < 0 or int(i) > 255:
                return
            
            if len(i) > 1:
                if int(i[0]) == 0:
                    return
                
        if int(ip[0]) == 0:
            return
        
        if int(ip[-1]) == 0 or int(ip[-1]) == 255:
            return
        
        valid_IP.append(IP)
        
    valid(IP)

bi = []
oc = []
he = []
vi = []

for vip in valid_IP:
    
    def convert(valid_ip):
        
        b = '.'.join([bin(int(x)+256)[3:] for x in vip.split('.')])
        o = '.'.join([oct(int(x)+256)[3:] for x in vip.split('.')])
        h = '.'.join([hex(int(x)+256)[3:] for x in vip.split('.')])
        
        bi.append(b)
        oc.append(o)
        he.append(h)
        vi.append(vip)
        
    convert(vip)

with open('IP.txt', 'w') as text:

    for i in range(len(valid_IP)):
        text.write(f"<{vi[i]} | {bi[i]} | {oc[i]} | {he[i]}>\n")
text.close()

fin = open("IP.txt", 'r')
f = fin.read()
print(f)
fin.close()
