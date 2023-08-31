import asyncio 

import websockets

async def send_msg():
    url = "ws://localhost:8765"
    # try:
    #     async with websockets.connect(uri) as websocket:
    #         print("Server is running!")
    # except ConnectionRefusedError:
    #     print("Server is not running.")
    try:
        async with websockets.connect(url) as websocket:
            name = input("What is your name: ")
            
            await websocket.send(name)  #sending to client
            
            print(f'Client sent: {name}')
            
            greeting = await websocket.recv() #waiting for response from server
            
            print(f'Client received: {greeting}')
    except ConnectionRefusedError:
        print("Server is not running")
        
        
if __name__ == "__main__":
    asyncio.run(send_msg())