# deepcube-project
高级软工大作业，包括前端、后端和deepcube模型。


# 模型环境配置
1)系统依赖库安装：\
apt-get update && apt-get install -y --no-install-recommends "build-essential=12.4ubuntu1" "libboost-all-dev=1.65.1.0ubuntu1"  "libboost-dev=1.65.1.0ubuntu1" && rm -rf /var/lib/apt/lists/*

2)开发平台(安装了 conda)：\
conda install --yes python==2.7.5 tensorflow-gpu==1.8.0 && conda clean --yes --all

3)平台依赖库：\
pip install --upgrade dm-sonnet==1.10 matplotlib==2.2.3

# 模型的前端部分具体见front-end

1) docker 运行镜像并做端口映射命令
   docker run -idt -d 8000:8000 xxxx  project.tar
2) django 对应的python版本:python2
3) 启动django命令: 
   python manage.py runserver 0.0.0.0:8000
   或者以后台命令方式启动:
   nohup python manage.py sunserver 0.0.0.0:8000 &


# 后端部分详见back-end



