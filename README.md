
# ChatGPT 网站检查器

此脚本用于检查文本文件中列出的 ChatGPT 网站的可用性和响应情况。



## 运行环境

- Python 3.x
- 必要的 Python 包（使用 `pip` 进行安装）：
  - requests
  - bs4（BeautifulSoup）
  - urllib3

## 网络测绘

### fofa

`title="ChatGPT Web"`、`icon_hash="-1656043765"`

### ZoomEye

`title:"ChatGPT Web"`

### Shodan

`http.title:"ChatGPT Web"`

### Hunter

`web.title="ChatGPT Web"`

### Quark

`title="ChatGPT Web"`

## 使用方法

1. 克隆存储库或下载脚本文件。
2. pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
3. 准备一个txt，其中包含要检查的 ChatGPT 网站的 URL 列表。
4. 运行`ChatGPT Website Checker.py`


## 额外配置

- 代理设置：如果您使用代理，请在脚本中的 `proxies` 字典中更新适当的代理 URL。

## 许可证

此脚本基于 [MIT 许可证](http://8.130.80.114:3002/LICENSE) 发布。
