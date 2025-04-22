from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.infraestructure.websocket.websocket_manager import manager

router = APIRouter()

@router.websocket("/ws/notifications")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # no usamos nada, pero mantenemos viva la conexión
    except WebSocketDisconnect:
        manager.disconnect(websocket)