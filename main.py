import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "websockets==12.0", "-q"])

import asyncio
import websockets
import json

async def handler(websocket):
    print(f"✅ Cliente conectado: {websocket.remote_address}")
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"📩 Recebido: {data}")
            await websocket.send(json.dumps({"status": "ok", "received": data}))
    except websockets.exceptions.ConnectionClosed:
        print("❌ Cliente desconectado")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8080):
        print("🚀 WebSocket Server rodando na porta 8080")
        await asyncio.Future()

asyncio.run(main())
