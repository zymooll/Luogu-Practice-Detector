# Luogu-Practice-Detector（Luogu 做题情况探测器）

This article is writing by Chinese.

## 简介

本爬虫基于 Python3 开发，可以便捷地爬取一段连续时间内的 Luogu 做题情况，方便教练/同学间进行数据分析等。

## 使用前须知

使用前需要对 `forserver.py` 中的 `username` 和 `useruid` 数组进行修改，其中 `username` 填写用户名字（不一定非得是 Luogu用户名），`useruid` 填写用户UID。（无论是对于下面两种部署方式的任何一种，这是必选项）

## Github Actions 部署

本项目自带 Github Actions 部署，使用者只需要将本项目 Fork 下来后，在 设置-秘密与变量-Actions的秘密与变量 中填写自己账号的 Github Token 即可，注意变量名应设为 `TOKEN_FOR_GITHUB`，另外该 Token 应允许 Actions 使用。

另请注意 `.github/workflow/main.yml` 中 `git config --global user.email xxx@xx.com git config --global user.name xxx` 中的 `xxx` 字段替换为自己的昵称和邮箱。

不过出于隐私考虑，作者声明：当对于本项目修改只有 `forserver.py` 中的 `username` 和 `useruid` 数组时，在 Star 本项目的前提下，作者（zymooll）自动放弃 GPL 许可赋予的分发项目开源及相同方式许可的权利。这意味着在仅供使用的情况下，只需要 Star 本项目即可闭源使用 Actions 功能。

默认情况下 Actions 将于 UTC+8 时间的早七到晚十一间，每半小时运行一次，同时也支持手动运行，运行结果将自动提交到项目根目录的 `ret.csv` 中，供下载取用。

## 本地部署

本项目不设 `requirement.txt`，故请自行安装 `requests-html` 库。

安装完之后直接运行 `forserver.py` 即可，运行结果将自动保存到项目根目录的 `ret.csv` 中，环境要求 Python 版本大于 3.8。
