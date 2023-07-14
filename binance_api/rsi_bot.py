import websocket, json, pprint

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"


def on_open(ws):
    print("open connection")
    
def on_close(ws):
    print("closed connection")
    
def on_message(ws, message):  
    json_message = json.loads(message)
    pprint.pprint(f"message received\n{json_message}\n") 

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)

ws.run_forever()