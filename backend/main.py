from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from subprocess import Popen, PIPE, TimeoutExpired
from models import SessionLocal, Code

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",  # Vite default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

def run_code(code: str):
    process = Popen(['python', '-c', code], stdout=PIPE, stderr=PIPE)
    try:
        stdout, stderr = process.communicate(timeout=10)
    except TimeoutExpired:
        process.kill()
        return 'Code execution timed out'

    if process.returncode == 0:
        return stdout.decode('utf-8')
    else:
        return stderr.decode('utf-8')

@app.post("/test")
def test_code(request: CodeRequest):
    result = run_code(request.code)
    return {"result": result}

@app.post("/submit")
def submit_code(request: CodeRequest):
    db: Session = SessionLocal()
    result = run_code(request.code)
    code_entry = Code(code=request.code, result=result)
    db.add(code_entry)
    db.commit()
    db.refresh(code_entry)
    return {"result": result}
