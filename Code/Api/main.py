## https://fastapi.tiangolo.com/tutorial/sql-databases/
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud
import schemas

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Route to get a circuit by its ID
@app.get("/circuits/{circuit_id}", response_model=schemas.Circuit)
def read_circuit(circuit_id: int, db: Session = Depends(get_db)):
    circuit = crud.get_circuit(db, circuit_id)
    if circuit is None:
        raise HTTPException(status_code=404, detail="Circuit not found")
    return circuit


# Route to get all circuits
@app.get("/circuits/", response_model=list[schemas.Circuit])
def read_circuits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    circuits = crud.get_circuits(db, skip=skip, limit=limit)
    return circuits


# Route to create a new circuit
@app.post("/circuits/", response_model=schemas.Circuit)
def create_circuit(circuit: schemas.CircuitCreate, db: Session = Depends(get_db)):
    return crud.create_circuit(db=db, circuit=circuit)


# Route to update an existing circuit
@app.put("/circuits/{circuit_id}", response_model=schemas.Circuit)
def update_circuit(circuit_id: int, circuit: schemas.CircuitCreate, db: Session = Depends(get_db)):
    updated_circuit = crud.update_circuit(db=db, circuit_id=circuit_id, circuit=circuit)
    if updated_circuit is None:
        raise HTTPException(status_code=404, detail="Circuit not found")
    return updated_circuit


# Route to delete a circuit
@app.delete("/circuits/{circuit_id}", response_model=schemas.Circuit)
def delete_circuit(circuit_id: int, db: Session = Depends(get_db)):
    deleted_circuit = crud.delete_circuit(db=db, circuit_id=circuit_id)
    if deleted_circuit is None:
        raise HTTPException(status_code=404, detail="Circuit not found")
    return deleted_circuit
