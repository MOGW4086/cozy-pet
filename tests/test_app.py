"""アプリケーション起動の基本スモークテスト。"""


def test_create_app(app):
    """create_app() が正常にアプリを生成すること。"""
    assert app is not None


def test_index_returns_200(client):
    """トップページが 200 を返すこと。"""
    response = client.get("/")
    assert response.status_code == 200


def test_viewer_id_session_created(client):
    """初回アクセスで viewer_id セッションが生成されること。"""
    with client.session_transaction() as sess:
        sess.clear()

    client.get("/")

    with client.session_transaction() as sess:
        assert "viewer_id" in sess


def test_security_headers(client):
    """セキュリティヘッダーが付与されること。"""
    response = client.get("/")
    assert response.headers.get("X-Content-Type-Options") == "nosniff"
    assert response.headers.get("X-Frame-Options") == "DENY"
    assert "Referrer-Policy" in response.headers


def test_character_svg_rendered(client):
    """SVGキャラクターが index ページに含まれること。"""
    response = client.get("/")
    assert b"<svg" in response.data
