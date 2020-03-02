## 展示网址
[hea.wujiashuai.com](http://hea.wujiashuai.com/)
![image.png](http://bkwebsiteimage.oss-cn-shanghai.aliyuncs.com/hzk5o66jqog.png) 
邮件收到展示
![image.png](http://bkwebsiteimage.oss-cn-shanghai.aliyuncs.com/l3ag8c39xx9.png)
![image.png](http://bkwebsiteimage.oss-cn-shanghai.aliyuncs.com/o9cy80uqr9.png)
使用方法,就是将自己的信息填入即可

## 项目运行的方式
我将项目写成了`Dockerfile`的形式,build成docker镜像后,实例化一键部署即可.
### 将该项目下载到本地
### 修改配置文件
`autoCheckhea`文件夹中有一个配置文件`config.py`,将配置文件填写完毕
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///static/data.db'  # 这个是sqlite文件的相对路径,并不需要更改
SQLALCHEMY_TRACK_MODIFICATIONS=True
SECRET_KEY = "xxxxxx" # 这个是csrf的盐,随便随机填写即可
SMTPPASSWD = "xxxxxxx" # 这个是自己qq邮箱的smtp授权码,查看这篇文章即可获得https://www.jianshu.com/p/9efaff9e9437
FROMADDR="xxx@qq.com"# 这个是自己的qq邮箱
```
### 生成docker镜像   
1. 进入项目`cd autoCheckhea`,进入后会发现有一个Dockerfile文件
![image.png](http://bkwebsiteimage.oss-cn-shanghai.aliyuncs.com/t3u84je8vrq.png)
2. 使用命令`docker build -t autochehea:v1 .`
![image.png](http://bkwebsiteimage.oss-cn-shanghai.aliyuncs.com/s1mrgytbgcg.png)

### 实例化对象
```
docker run -tid --name autochehea -p 80:8000 autochehea:v1 
```
![image.png](http://bkwebsiteimage.oss-cn-shanghai.aliyuncs.com/6bl0el3ivpr.png)
浏览器 访问 127.0.0.1即可
![image.png](http://bkwebsiteimage.oss-cn-shanghai.aliyuncs.com/cuhsts4y7z.png)