"""メインページのルーティング。"""

import uuid
from flask import Blueprint, render_template, session

bp = Blueprint("main", __name__)


def get_or_create_viewer_id():
    """session から viewer_id を取得し、なければ新規生成する。"""
    if "viewer_id" not in session:
        session["viewer_id"] = str(uuid.uuid4())
    return session["viewer_id"]


@bp.route("/")
def index():
    # _viewer_id は後続 Issue（#3）で DB からペット情報を取得する際に viewer_id として使用する
    _viewer_id = get_or_create_viewer_id()

    # 仮のペット情報（後の Issue で DB から取得する）
    pet = {
        "name": "ペット",
        "stage": "egg",
        "hunger": 80,
        "happiness": 80,
        "sleepiness": 20,
    }

    return render_template("index.html", pet=pet)
