from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class ClienteSchema(BaseModel):
    nome: str
    cpf: str
    data_nasc: date
    email: EmailStr


class ClientePublic(BaseModel):
    id: int
    nome: str
    cpf: str
    data_nasc: date
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class ClienteDB(ClienteSchema):
    id: int


class ClienteList(BaseModel):
    clientes: list[ClientePublic]
