import socket
HOST = '127.0.0.1'
PORT = 9997
# 소캣 객체 생성

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 임의 데이터 통신
client.sendto(b'AABBCC', (HOST, PORT))  # 응답 데이터 수신

data, address = client.recvfrom(4096)
print(data.decode('utf-8'))
print(address.decode('utf-8'))
client.close()
