# gunicorn_config.py
bind = "0.0.0.0:8000"
workers = 3  # ワーカー数を指定（CPUのコア数 * 2 + 1 くらいが目安だよ）
module = "myproject.wsgi:application" # ここをあなたのプロジェクト名に合わせてね

# その他、ロギングの設定などもここに書けるよ
errorlog = "/var/log/gunicorn_error.log"
accesslog = "/var/log/gunicorn_access.log"
loglevel = "info"