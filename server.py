


import asyncio
import websockets


async def receive_message(websocket):
    
    
    name = await websocket.recv() #waiting for the message
    
    print(f'Server Received: {name}') #Printing the text received by client
    
    greeting = f"Hello {name}"
    
    await websocket.send(greeting) #Sending the server response to client
    
    print(f'Server sent: {greeting}')
    
    
async def run():
    async with websockets.serve(receive_message, "localhost", 8765):
        await asyncio.Future()
        
if __name__ == "__main__":
    print('Server is up and running')
    asyncio.run(run())