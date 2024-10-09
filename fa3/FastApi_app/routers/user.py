from fastapi import APIRouter

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from FastApi_app.backend.db_depends import get_db
from typing import Annotated
from FastApi_app.models import User
from FastApi_app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router =APIRouter(prefix="/user", tags=["user"])

@router.get('/')
async def all_users() :
    pass

@router.get('/user_id')
async def user_by_id() :
    pass

@router.post('/create')
async def create_user() :
    pass

@router.put('/update')
async def update_user() :
    pass

@router.delete('/delete')
async def delete_user() :
    pass
