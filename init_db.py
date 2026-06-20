"""SQLite DB 初期化スクリプト。

使い方:
    python init_db.py

instance/cozy_pet.db を作成し、pets テーブルを初期化する。
"""

import os
import sqlite3


DB_DIR = os.path.join(os.path.dirname(__file__), "instance")
DB_PATH = os.path.join(DB_DIR, "cozy_pet.db")

CREATE_PETS_TABLE = """
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    viewer_id TEXT NOT NULL,
    name TEXT NOT NULL DEFAULT 'ペット',
    stage TEXT NOT NULL DEFAULT 'egg',
    hunger INTEGER NOT NULL DEFAULT 80,
    happiness INTEGER NOT NULL DEFAULT 80,
    sleepiness INTEGER NOT NULL DEFAULT 20,
    total_happiness INTEGER NOT NULL DEFAULT 0,
    last_updated TEXT NOT NULL DEFAULT (datetime('now')),
    born_at TEXT NOT NULL DEFAULT (datetime('now')),
    last_fed TEXT,
    last_played TEXT,
    last_slept TEXT,
    color_r INTEGER NOT NULL DEFAULT 100,
    color_g INTEGER NOT NULL DEFAULT 150,
    color_b INTEGER NOT NULL DEFAULT 200,
    personality TEXT NOT NULL DEFAULT 'normal',
    special_skill TEXT,
    generation INTEGER NOT NULL DEFAULT 1,
    parent_id INTEGER REFERENCES pets(id),
    is_active INTEGER NOT NULL DEFAULT 1,
    married_at TEXT,
    visitor_info TEXT,
    retired_at TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


def init_db():
    """DB ファイルを作成し、テーブルを初期化する。"""
    os.makedirs(DB_DIR, exist_ok=True)
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(CREATE_PETS_TABLE)
            conn.commit()
        print(f"DB を初期化しました: {DB_PATH}")
    except sqlite3.Error as e:
        print(f"DB 初期化エラー: {e}")
        raise


if __name__ == "__main__":
    init_db()
