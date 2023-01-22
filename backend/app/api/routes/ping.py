import json
import logging

from fastapi import APIRouter, Depends, HTTPException
from app.services.event import send_event

router = APIRouter()

@router.get("")
async def check_ping():
    try:
        res = send_event('ping', {})
        return res.json()

    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Error")
