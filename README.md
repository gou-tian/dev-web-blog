# 我的网站博客系统
#### 系统架构
 > * 开发环境
  * python 3.6
  * flask 1.0
  * PyCharm
  * windows、linux
### 依赖软件包管理
    *   生成命令
    ```pip freeze >requirements.txt```
    *   软件包部署
    ```pip install -r requirements.txt```
### git密钥生成
```
ssh-keygen -t rsa -C 'dev-web-blog'
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/gousky/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/gousky/.ssh/id_rsa.
Your public key has been saved in /c/Users/gousky/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:V2Wz6nQtDWLSrIAAOgDYidJNuQyAogFZV45NsBeXZp4-1 dev-web-blog
The key's randomart image is:
+---[RSA 2048]----+
|XBo==++ ..    +  |
|X.=.oB ++  o o o |
|*. oo.=+... * o  |
|..  o.  E. = o + |
|        S o o o o|
|         . o . . |
|            .    |
|                 |
|                 |
+----[SHA256]-----+
```
### 蓝图模版设定
```
from flask import Blueprint
Blueprint('main', __name__, template_folder='../../templates')
```
        'mian'为蓝图设定目录，template_folder模版文件不得同目录下，要设定模版文件夹路径。否则会报错 jinja2.exceptions.TemplateNotFound: （文件名）
### 获取环境变量
```
import os
# environ是在os.py中定义的一个dict environ = {}
# 读取环境变量两种方法
# 1.os.environ 
# 2. os.getenv('MAIL_USERNAME')
env_dist = os.environ 
os.getenv('MAIL_USERNAME')

print(env_dist.get('JAVA_HOME'))
print(env_dist['JAVA_HOME'])

# 打印所有环境变量，遍历字典
for key in env_dist:
    print(key + ' : ' + env_dist[key])
# 设置环境变量
# Linux： export FLASKY_ADMIN=<your-email-address>
# windows set FLASKY_ADMIN=<Gmail username>
```



