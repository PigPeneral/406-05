# 【Django 專案 Dockerfile】
FROM python:3.11-slim

# 【自訂】設定環境變數
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# 【自訂】設定工作目錄
WORKDIR /app/django

# 【自訂】安裝系統相依套件
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 【自訂】複製 requirements.txt 並安裝套件
COPY requirements.txt /app/django/
RUN pip install --no-cache-dir -r requirements.txt

# 【自訂】複製所有專案檔案
COPY . /app/django/

# 【自訂】建立必要目錄
RUN mkdir -p /app/django/static /app/django/media

# 【自訂】設定檔案權限（如果 manage.py 存在的話）
RUN if [ -f "manage.py" ]; then chmod +x manage.py; fi

# 【自訂】暴露連接埠
EXPOSE 8000

# 【自訂】啟動指令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]# 【Django 專案 Dockerfile】
FROM python:3.11-slim