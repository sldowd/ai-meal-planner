from cli.interface import app
from db.core import init_db

if __name__ == "__main__":
    app()
    init_db()
