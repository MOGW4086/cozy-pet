"""cozy-pet 起動スクリプト。ポート 5002 で起動する。"""

import os
from dotenv import load_dotenv

load_dotenv()

from cozy_pet import create_app

app = create_app()

if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host=host, port=5002, debug=debug)
