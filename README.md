
# ChatGPT 白嫖检测器

此脚本用于检查互联网中的 ChatGPT 能否白嫖。

ChatGPT Web源仓库地址：https://github.com/Chanzhaoyu/chatgpt-web

*~~萌新写的第一个公开脚本，希望大佬们多多star。~~*


## 运行环境

- Python 3.x
- 必要的 Python 包（使用 `pip` 进行安装）：
  - requests
  - bs4（BeautifulSoup）
  - urllib3

## 使用方法

1. 克隆仓库到本地 `git clone https://github.com/4O4NtFd/ChatGPT-Website-Checker.git`
2. `pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`
3. 准备一个txt，其中包含要检查的 ChatGPT 网站的 URL 列表。
4. 运行`ChatGPT Website Checker.py`
5. 查看`output.txt`

## 网络测绘

### fofa

`title="ChatGPT Web"`、`icon_hash="-1656043765"`

`title="ChatGPT Next Web"`

### ZoomEye

`title:"ChatGPT Web"`

### Shodan

`http.title:"ChatGPT Web"`

### Hunter

`web.title="ChatGPT Web"`

### Quark

`title="ChatGPT Web"`


## 额外配置

- 代理设置：如果您使用代理，请在脚本中的 `proxies` 字典中更新适当的代理 URL。

## To-do list

- 增加对title="ChatGPT Next Web"的检测

## 贡献

如果您发现了 Bug 或者有改进建议，请随时提交 Issue 或者 Pull Request，我们将非常感谢您的贡献！

## 声明

本项目遵循 GNU General Public License v3.0 开源，在此基础上，所有使用本项目提供服务者都必须在网站首页保留指向本项目的链接

禁止使用本项目进行营利和做其他违法事情，产生的一切后果本项目概不负责
