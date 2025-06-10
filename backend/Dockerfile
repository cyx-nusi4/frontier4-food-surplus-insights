# backend/Dockerfile
FROM python:3.9-slim

## 替换 Ubuntu 软件源为阿里云镜像源（基于 Debian 的镜像）
#RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
#    && sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
#
# 安装必要的系统工具
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the backend code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt

# Expose the backend port
EXPOSE 5002

# Run the Flask app
CMD ["python", "run.py"]