from fastapi import FastAPI

app = FastAPI(title="Zafiyet Tarama ve Yonetim Sistemi")

@app.get("/")
def read_root():
    return {
        "status": "active",
        "message": "Zafiyet Tarama Servisi Calisiyor"
    }

@app.get("/health")
def health_check():
    return {
        "database": "waiting_connection",
        "scanner": "ready"
    }
