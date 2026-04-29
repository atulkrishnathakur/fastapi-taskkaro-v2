from sqlmodel import SQLModel, Field

class TaskBase(SQLModel): # It is not create table in database
    title: str
    content: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass


class TaskPatch(SQLModel):
    title: str | None = None
    content: str | None = None

class TaskOut(TaskBase):
    id: int

class Task(TaskBase, table=True): # use to create table in DB because table=True used
    id: int = Field(primary_key=True)