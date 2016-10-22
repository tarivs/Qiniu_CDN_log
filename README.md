# 七牛CDN日志下载 #

通过七牛CDN日志接口实现查询域名日志列表，获取日志的下载外链

> 日志下载接口可以查询域名日志列表，获取日志的下载外链，只提供 30 个自然日内的日志下载，例如当前日期为 2016-08-31，则只提供 2016-08-01 ~ 2016-08-30 的日志。
> http://developer.qiniu.com/article/fusion/api/log.html

## 运行环境

python 2.7

## 配置环境

pip install -r requirements.txt

## 使用方法

```python
    access_key = "..."
    secret_key = "..."
    # 初始化Auth状态
    q = Auth(access_key=access_key, secret_key=secret_key)
    buck = BucketManager(q)

    # 日期
    day = "2016-10-13"

    # 域名列表，以英文分号 ; 分割
    domains = "a.qiniu.com;b.qiniu.com"

    ret, eof, info = buck.list_log(day, domains)

    print 'ret :', ret
```

在examples/list_log.py中可查看完整调用。

# 说明
因七牛目前python版本的SDK中未包括CDN日志实现内容，故根据七牛目前的sdk改写而成。

代码架构及部分内容来自于七牛SDK ：https://github.com/qiniu/python-sdk