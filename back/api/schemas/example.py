from typing import Optional
from pydantic import BaseModel, Field


class ExampleBase(BaseModel):
    name: str = Field(..., example="Sample Name")
    description: Optional[str] = Field(None, example="This is a sample description.")


class ExampleRequest(ExampleBase):
    created_at: str = Field(..., example="2024-01-01T00:00:00Z")


class ExampleResponse(ExampleBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True
