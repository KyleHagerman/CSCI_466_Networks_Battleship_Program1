import socket, requests, re

def fire(hit_miss,x,y):
    board=open(your_board,"r")
    s=board.readlines()
    board.close()
    if hit_miss=="hit":
        s[y]=s[y][0:x]+"X"+s[y][x+1:]
    elif hit_miss=="miss":
        s[y]=s[y][0:x]+"O"+s[y][x+1:]
    else:
        print("Hit or miss unknown")
    board=open(your_board,"w")
    for i in s:
        board.write(i)
    board.close()

your_board= r"C:\Users\Justin\Documents\MSU_Classes\Networks\opponent_board.txt"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#s.connect(('127.0.0.1',8080))
'''
s.send('Are you there?'.encode('utf-8'))

data = s.recv(64)
print("Received response: "+data.decode('utf-*'+"'"))
'''

r = requests.post('http://127.0.0.1:8080?x=5&y=7')


print(r)
print(r.content)
print(r.status_code)
hit = r.content
fire_result = re.findall(r'\d', str(hit))
did_sink = re.findall(r'=\w', str(hit))
ship_sunk = re.findall(r'\w', did_sink[1])
print(fire_result)
print(did_sink)
print(ship_sunk)

s.close()
'''

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto('hello'.encode('utf-8'),('127.0.0.1',8080))
'''

#Game Flow
#----------------------
'''request at x,y
    s.close
    fire(result)
'''
