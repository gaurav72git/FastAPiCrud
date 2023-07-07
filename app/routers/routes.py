from datetime import datetime
import uuid
from app import models, schema
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db

router = APIRouter()


@router.get('/get_data')
def get_data():


@router.get('/get_data_trigger')
def get_data_trigger():


@router.put('/update_data')
def update_data():


@router.post('/add_data')
def add_data():
