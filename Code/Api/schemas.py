from pydantic import BaseModel
from typing import Optional


class CircuitBase(BaseModel):
    circuitRef: str
    name: str
    location: str
    country: str
    lat: float
    lng: float
    alt: int
    url: Optional[str] = None


class CircuitCreate(CircuitBase):
    pass


class Circuit(CircuitBase):
    circuitId: int

    class Config:
        orm_mode = True  # -*- coding: utf-8 -*-
