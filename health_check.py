import os
import sys
import json
import urllib.request
from datetime import datetime

# Lista de servicios o URLs a comprobar
ENDPOINTS = [
    "https://httpbin.org/status/200",
    "https://api.github.com",
    "https://www.google.com"
]

def check_endpoints(urls):
    results = []
    print(f"[{datetime.now()}] Iniciando chequeo de servicios...")
    
    for url in urls:
        status_entry = {"url": url, "timestamp": datetime.now().isoformat(), "status": "DOWN"}
        try:
            response = urllib.request.urlopen(url, timeout=5)
            if response.getcode() == 200:
                status_entry["status"] = "UP"
                print(f" [OK] {url} está operativo.")
            else:
                print(f" [WARN] {url} devolvió código {response.getcode()}")
        except Exception as e:
            print(f" [ERROR] No se pudo conectar a {url}: {e}")
        
        results.append(status_entry)
        
    return results

if __name__ == "__main__":
    report_data = check_endpoints(ENDPOINTS)
    print("Chequeo finalizado con éxito.")
