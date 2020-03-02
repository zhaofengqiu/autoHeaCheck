FROM alpine:latest
COPY ./autoCheckhea /app
RUN  sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
	&& sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
	&& apk update && apk upgrade \
	&& apk add gcc && apk add g++ \
    && apk add ca-certificates curl python3-dev \
    && apk add --no-cache libressl-dev musl-dev libffi-dev \
    && apk del curl && rm -rf /var/cache/apk/*
 WORKDIR /app/
 RUN pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple \
 	&& pip3 install -r requirement.txt  -i https://mirrors.aliyun.com/pypi/simple  \
 	&& echo "0       8       *       *       *       /app/./shell.sh" >>/var/spool/cron/crontabs/root && crond  
 CMD gunicorn -w 3 -b 0.0.0.0:8000  web:app --access-logfile log/access.log --error-logfile  log/error.log 
 EXPOSE 8000