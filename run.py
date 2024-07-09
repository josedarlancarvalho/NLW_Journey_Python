print("Starting the Flask application...")  # Linha de depuração
from src.main.server.server import app

if __name__ == "__main__":
    print("Running the Flask application...")  # Linha de depuração
    app.run(host="0.0.0.0", port=3000, debug=True)
