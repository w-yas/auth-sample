from fastapi import APIRouter, Depends
from schemas.example import ExampleRequest, ExampleResponse, ExampleBase
from db.db import get_db

router = APIRouter()


@router.get("/")
async def get_root():
    return {"message": "API is running"}


@router.post("/example", response_model=ExampleResponse)
async def create_example(example: ExampleRequest, db=Depends(get_db)):
    db_example = ExampleBase(
        name=example.name, description=example.description, created_at=example.created_at
    )
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example
