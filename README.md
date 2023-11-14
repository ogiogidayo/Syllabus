# Syllabus_API
ChatGPTで生成
このプロジェクトはPythonで作成されたRESTful APIです。CRUD操作を提供し、データの作成、読み取り、更新、削除を行うことができます。

## プロジェクト構成

- `crud.py`: CRUD操作の関数を含む。
- `database.py`: データベース接続とセッション管理を行う。
- `main.py`: アプリケーションのエントリーポイント、ウェブサーバーの設定。
- `models.py`: データベースモデルを定義。
- `schemas.py`: データのシリアライズとデシリアライズのためのスキーマ定義。

## セットアップ

依存関係のインストールとサーバーの起動方法を以下に示します。

```bash
# 依存関係のインストール
pip install -r requirements.txt

# サーバーの起動
python main.py
