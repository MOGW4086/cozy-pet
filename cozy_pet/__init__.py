"""cozy_pet: Flask app factory."""

import logging
import os
from datetime import timedelta

from flask import Flask

logger = logging.getLogger(__name__)


def create_app(test_config=None):
    """Flask アプリケーションファクトリ。

    Args:
        test_config: テスト用の設定辞書。None の場合は通常の設定を使用。

    Returns:
        設定済みの Flask アプリケーションインスタンス。
    """
    app = Flask(__name__, instance_relative_config=True)

    secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    if secret_key == "dev-secret-key-change-in-production":
        logger.warning("SECRET_KEY is not set. Using insecure default. Set SECRET_KEY in production.")

    app.config.from_mapping(
        SECRET_KEY=secret_key,
        DATABASE=os.path.join(app.instance_path, "cozy_pet.db"),
        PERMANENT_SESSION_LIFETIME=timedelta(days=365),
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.environ.get("SESSION_COOKIE_SECURE", "false").lower() == "true",
        SESSION_COOKIE_HTTPONLY=True,
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # instance フォルダを作成
    os.makedirs(app.instance_path, exist_ok=True)

    @app.after_request
    def set_security_headers(response):
        """セキュリティヘッダーをレスポンスに付与する。"""
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        return response

    # ルーティング登録
    from cozy_pet.routes import main as main_bp
    app.register_blueprint(main_bp.bp)

    return app
