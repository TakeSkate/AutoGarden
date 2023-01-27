from pydantic import BaseModel


class RegistryBase(BaseModel):
    id: int
    day: str
    month: str
    year: str
    hour: str
    minute: str
    temperatura_ambiente: int
    humedad_ambiente: int
    humedad_planta: int
    luminosidad: int
    riego: bool


class RegistryCreate(RegistryBase):
    pass


class Registry(RegistryBase):
    id: int

    class Config:
        orm_mode = True

