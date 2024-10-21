import subprocess
import platform
import time
import sys
import os

backend_dir = os.path.join(os.getcwd(), 'backend')
frontend_dir = os.path.join(os.getcwd(), 'frontend')
app_dir = os.path.join(os.getcwd(), )


def run_in_new_terminal(command, cwd=None):
    """
    Runs a command in a new terminal window based on the OS.
    """
    system = platform.system()
    activate_venv = ['pyenv', 'activate', 'inter_bot']
    if system == "Windows":
        subprocess.Popen(['start', 'cmd', '/k'] + command, cwd=cwd, shell=True)
    elif system == "Darwin":  # macOS
        subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "cd {cwd} && {" ".join(activate_venv)} && {" ".join(command)}"'])
    elif system == "Linux":
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'cd {cwd} && {" ".join(command)}; exec bash'])

def run_fastapi():
    """
    Starts the FastAPI server using Uvicorn in a new terminal.
    """
    run_in_new_terminal(["uvicorn", "main:app", "--reload"], cwd=backend_dir)

def run_streamlit():
    """
    Starts the Streamlit application in a new terminal.
    """
    run_in_new_terminal(["streamlit", "run", "app.py"], cwd=frontend_dir)

def start_ollama():
    """
    Starts Ollama in a new terminal.
    """
    run_in_new_terminal(["ollama", "serve"], cwd=app_dir)

if __name__ == "__main__":
    # Start each process in a separate terminal
    run_fastapi()
    time.sleep(1)  # Optional: add small delay to avoid race conditions
    run_streamlit()
    time.sleep(1)
    start_ollama()

    print("All processes started in separate terminals.")

    try:
        while True:
            time.sleep(1)  # Keep main thread alive
    except KeyboardInterrupt:
        print("Shutting down...")
        sys.exit()
