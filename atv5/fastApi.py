
from fastapi import FastAPI, HTTPException
import datetime
import math

app = FastAPI()

# Obter a data e hora atual
@app.get("/data_hora")
def get_data_hora():
    data_hora_atual = datetime.datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    return {"data_hora": data_hora_formatada}

# Calcular o fatorial de um número
@app.get("/fatorial/{numero}")
def calcular_fatorial(numero: int):
    if numero < 0:
        raise HTTPException(status_code=400, detail="Número deve ser não negativo")
    return {"fatorial": math.factorial(numero)}

# Obter as casas do pi
@app.get("/pi/{casas}")
def obter_pi(casas: int):
    if casas <= 0:
        raise HTTPException(status_code=400, detail="Número de casas deve ser positivo")
    return {"pi": f"{math.pi:.{casas}f}"}

# Obter o n-ésimo número da sequência de Fibonacci
@app.get("/fibonacci/{n}")
def fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="Número deve ser não negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return {"fibonacci": a}

@app.get("/")
def read_root():
    return {"message": "API em funcionamento"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
