import websocket

SOCKET = "wss://stream.binance.com:9443 or wss://stream.binance.com:443/ws\
    /ethusdt@kline_1m"


def on_open():
    print("open connection")
    
def on_close():
    print("closed connection")
    
def on_message():
    print("message received")   

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)

