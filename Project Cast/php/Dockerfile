FROM php:8.2-apache

# 安裝常用擴展
RUN docker-php-ext-install pdo pdo_mysql mysqli

# 啟用 Apache mod_rewrite
RUN a2enmod rewrite

# 設置工作目錄
WORKDIR /var/www/html

# 複製源代碼
COPY . /var/www/html/

EXPOSE 80