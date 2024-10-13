from fastapi import APIRouter
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from models import Task
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from schemas import CreateTask
from schemas import UpdateTask
from backend.db_depends import get_db
router =APIRouter(prefix="/task", tags=["task"])

@router.get('/')
async def all_tasks(db:Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task != None)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(db:Annotated[Session, Depends(get_db)], task_id: int):
    tasks = db.scalars(select(Task).where(Task.id == task_id)).all()
    return tasks

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task : CreateTask):
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   completed=create_task.completed,
                                   user_id=create_task.user_id,
                                   slug=slugify(create_task.title
                                  )))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put('/update')
async def update_tasks(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: CreateTask):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no task found'
            )
    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority,
        completed=update_task.completed
        ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful'
        }


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: CreateTask):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no task found'
            )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task delete is successful'
        }
