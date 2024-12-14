import os
import time
os.system('start cmd /k "python -m http.server 8000"')
time.sleep(3)
os.system('start http://localhost:8000')