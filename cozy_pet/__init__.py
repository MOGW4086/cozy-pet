"""cozy_pet: Flask app factory."""

import os
from datetime import timedelta
from flask import Flask


def create_app(test_config=None):
    """Flask アプリケーションファクトリ。

    Args:
        test_config: テスト用の設定辞書。None の場合は通常の設定を使用。

    Returns:
        設定済みの Flask アプリケーションインスタンス。
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production"),
        DATABASE=os.path.join(app.instance_path, "cozy_pet.db"),
        PERMANENT_SESSION_LIFETIME=timedelta(days=365),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # instance フォルダを作成
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ルーティング登録
    from cozy_pet.routes import main as main_bp
    app.register_blueprint(main_bp.bp)

    return app
