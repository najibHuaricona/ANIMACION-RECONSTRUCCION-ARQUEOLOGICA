from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os, threading, time, webbrowser
os.chdir(Path(__file__).resolve().parent)
PORT=8000
def open_browser():
 time.sleep(1); webbrowser.open(f"http://127.0.0.1:{PORT}")
threading.Thread(target=open_browser,daemon=True).start()
print(f"Proyecto Puerta del Sol: http://127.0.0.1:{PORT}")
print("Cierra esta ventana para detener el servidor.")
ThreadingHTTPServer(("127.0.0.1",PORT),SimpleHTTPRequestHandler).serve_forever()
