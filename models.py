# models.py
from django.db import models  # Djangoのモデルを使うためのインポート
from simple_history.models import HistoricalRecords  # 履歴管理を使うためのインポート

from simple_history.models import HistoricalRecords

class MyModel(models.Model):
    # モデルのフィールド
    name = models.CharField(max_length=100)
    history = HistoricalRecords()  # 履歴管理を追加