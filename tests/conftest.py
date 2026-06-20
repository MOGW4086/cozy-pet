"""pytest フィクスチャ（後の Issue でテストを追加する）。"""

import pytest

from cozy_pet import create_app


@pytest.fixture
def app():
    """テスト用 Flask アプリを返す。"""
    app = create_app(
        test_config={
            "TESTING": True,
            "DATABASE": ":memory:",
            "SECRET_KEY": "test-secret-key",
        }
    )
    yield app


@pytest.fixture
def client(app):
    """テスト用クライアントを返す。"""
    return app.test_client()
