@echo off
echo ==========================================
echo MF GURU — Local Dev (Python 3.11 recommended)
echo ==========================================
rmdir /s /q venv
IF NOT EXIST venv (
  python -m venv venv
)
call venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
echo Starting uvicorn...
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
set /p =Press Enter to exit...
