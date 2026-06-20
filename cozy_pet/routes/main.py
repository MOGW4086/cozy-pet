"""メインページのルーティング。"""

import uuid
from datetime import datetime, timedelta

from flask import Blueprint, make_response, render_template, request

bp = Blueprint("main", __name__)

COOKIE_NAME = "viewer_id"
COOKIE_EXPIRE_DAYS = 365


def get_or_create_viewer_id():
    """Cookie から viewer_id を取得し、なければ新規生成する。

    Returns:
        (viewer_id: str, is_new: bool) のタプル。
        is_new が True の場合、新規生成された ID。
    """
    viewer_id = request.cookies.get(COOKIE_NAME)
    if viewer_id:
        return viewer_id, False
    return str(uuid.uuid4()), True


@bp.route("/")
def index():
    """トップページ。ペットのステータスを表示する。

    Returns:
        レスポンスオブジェクト（Cookie を付与する場合あり）。
    """
    viewer_id, is_new = get_or_create_viewer_id()

    # 仮のペット情報（後の Issue で DB から取得する）
    pet = {
        "name": "ペット",
        "stage": "egg",
        "hunger": 80,
        "happiness": 80,
        "sleepiness": 20,
    }

    resp = make_response(render_template("index.html", pet=pet))

    if is_new:
        expire = datetime.utcnow() + timedelta(days=COOKIE_EXPIRE_DAYS)
        resp.set_cookie(
            COOKIE_NAME,
            viewer_id,
            expires=expire,
            httponly=True,
            samesite="Lax",
        )

    return resp
