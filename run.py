"""cozy-pet 起動スクリプト。ポート 5002 で起動する。"""

from dotenv import load_dotenv

load_dotenv()

from cozy_pet import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=False)
