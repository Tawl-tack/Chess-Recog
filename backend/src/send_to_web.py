import sys
import struct
import json

def read_message(): # Lê a mensagem da web
    raw_size = sys.stdin.buffer.read(4) # Define o tamanho da mensagem que ele receberá
    if not raw_size:
        return None
    size = struct.unpack('<I', raw_size)[0] 
    message = sys.stdin.buffer.read(size).decode('utf-8') # Decodifica a mensagem da web para o python
    return json.loads(message)

def send_message(answer):
    encoded = json.dumps(answer).encode('utf-8') # Codifica a mensagem para mandar para web
    sys.stdout.buffer.write(struct.pack('<I', len(encoded)))
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush() # Envia para web