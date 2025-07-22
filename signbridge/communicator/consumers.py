from channels.generic.websocket import AsyncWebsocketConsumer
import cv2
import asyncio
import json
import base64


class SignBridgeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({
            'status': 'CONNECTED',
            'message': 'Conexión WebSocket establecida'
        }))

        # Prueba simple sin cámara primero
        while True:
            await asyncio.sleep(1)
            await self.send(json.dumps({
                'test': 'Mensaje de prueba cada segundo'
            }))