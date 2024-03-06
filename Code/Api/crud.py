from sqlalchemy.orm import Session
from models import Circuit as CircuitModel
from schemas import CircuitCreate, Circuit


def get_circuit(db: Session, circuit_id: int):
    return db.query(CircuitModel).filter(CircuitModel.circuitId == circuit_id).first()


def get_circuits(db: Session, skip: int = 0, limit: int = 10):
    return db.query(CircuitModel).offset(skip).limit(limit).all()


def create_circuit(db: Session, circuit: CircuitCreate):
    db_circuit = CircuitModel(**circuit.dict())
    db.add(db_circuit)
    db.commit()
    db.refresh(db_circuit)
    return db_circuit


def update_circuit(db: Session, circuit_id: int, circuit: CircuitCreate):
    db_circuit = db.query(CircuitModel).filter(CircuitModel.circuitId == circuit_id).first()
    if db_circuit:
        for key, value in circuit.dict().items():
            setattr(db_circuit, key, value)
        db.commit()
        db.refresh(db_circuit)
    return db_circuit


def delete_circuit(db: Session, circuit_id: int):
    db_circuit = db.query(CircuitModel).filter(CircuitModel.circuitId == circuit_id).first()
    if db_circuit:
        db.delete(db_circuit)
        db.commit()
    return db_circuit
