from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date
import uuid
from sqlalchemy import Column, String, Float, Date, Text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from config import engine, Base, get_db

# Modelo de pydantic
# Proyecto

class ProyectoBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100, examples="Sistema de Gestión de proyectos web")
    descripcion: str = Field(..., min_length=10, max_length=500, examples="Desarrollo de una app para gestion de proyectos web")
    presupuesto: float = Field(..., gt=0, le=10000000, examples=2500.33)
    fecha_inicio: str = Field(..., description="YYYY-MM-DD", examples="2025-09-25")
    estado: str = Field(..., pattern=r"^(planificacion|en_progreso|completado|cancelado)$", example="planificación")

class ProyectoCreate(ProyectoBase):
    pass

class ProyectoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100, examples="Actualización del nombre")
    descripcion: Optional[str] = Field(None, min_length=10, max_length=500, examples="Actualización de la descripción")
    presupuesto: Optional[float] = Field(None, gt=0, le=10000000, examples=123456.45)
    fecha_inicio: Optional[str] = Field(None, description="YYYY-MM-DD", examples="2020-10-10")
    estado: Optional[str] = Field(None, pattern=r"^(planificacion|en_progreso|completado|cancelado)$", example="en_progreso")

class ProyectoResponse(ProyectoBase):
    proyecto_id: str = Field(..., description="ID único generado por uuid", examples="550e8400-e29b-41d4-a716-446655440000")

# Cliente

class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50, examples="Luis Guillermo Molero Suárez")
    email: EmailStr = Field(..., examples="luisguillermomolero.suarez@gmail.com")
    telefono: str = Field(..., min_length=7, max_length=20, examples="+573254568920")
    empresa: str =  Field(..., min_length=2, max_length=100, examples="Soluciones Tecnológicas S.A.S")
    direccion: str = Field(..., min_length=10, max_length=200, examples="Calle 55 #45-67 Manizales, Colombia")

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=50, examples="Actualización del nombre")
    email: Optional[EmailStr] = Field(None, examples="Actualización del correo")
    telefono: Optional[str] = Field(None, min_length=7, max_length=20, examples="+571231231212")
    empresa: Optional[str] =  Field(None, min_length=2, max_length=100, examples="Actualización de la empresa")
    direccion: Optional[str] = Field(None, min_length=10, max_length=200, examples="Actualización de la direccion")

class ClienteResponse(ClienteBase):
    cliente_id: str = Field(..., description="ID único generado por uuid", examples="550e8400-e29b-41d4-a716-446655440000")
    

# Modelos ORM

# Proyectos

class Proyecto(Base):
    __tablename__ = "proyectos"
    __table_args__ = {'extend_existing': True}
    
    proyecto_id = Column(String(36), primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    presupuesto = Column(Float, nullable=False)
    fecha_inicio = Column(Date, nullable=False)

# Clientes

class Cliente(Base):
    __tablename__ = "clientes"
    __table_args__ = {'extend_existing': True}
    
    cliente_id = Column(String(36), primary_key=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=False)
    empresa = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    
# Routers personalizados

