import websocket

SOCKET = "wss://stream.binance.com:9443 or wss://stream.binance.com:443/ws\
    /ethusdt@kline_1m"

ws = websocket.WebSocketApp(SOCKET)