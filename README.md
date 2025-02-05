# 每天 60 秒读懂世界

《每天 60 秒读懂世界》新闻推送，多种方式可选，持续更新接口。

## 使用

#### 1. 创建仓库分支

[点击创建仓库分支](https://github.com/yanyaoli/daily60s/fork)

#### 2. 添加环境变量

选择自己的分支仓库 -> `Settings` -> `Secrets and Variables` -> `Action` -> `New repository secret`，添加环境变量。

> 请按需选择填写，变量名称请查看 [.env.example](.env.example)

#### 3. 开启自动化

选择自己的分支仓库 -> `Settings` -> `Actions` -> ` General` -> `Workflow permissions`，勾选`Read and write permissions` 和 `Allow GitHub Actions to create and approve pull requests`，然后`Save`保存


## API

|TYPE|API|SRC|
|---|---|---|
|PIC|`https://api.03c3.cn/api/zb`|[03c3](https://api.03c3.cn/)|
|TXT|`https://60s.viki.moe/?encoding=text`|[60s](https://github.com/vikiboss/60s)|
|JSON|`http://60s-api.viki.moe/v2/60s`|[60s](https://github.com/vikiboss/60s)|
|TXT|`https://lzw.me/x/iapi/60s/?e=text`|[60s-php](https://github.com/lzwme/60s-php)|
|JSON|`https://lzw.me/x/iapi/60s/?e=json`|[60s-php](https://github.com/lzwme/60s-php)|

## Demo

<div>
  <img src="https://github.com/yanyaoli/daily60s/assets/120553430/d90bb0e3-0021-43d6-a9af-0df485a025c7" width="300" />
  <img src="https://github.com/yanyaoli/daily60s/assets/120553430/6edefff9-7235-4675-b9b1-db257d3eb693" width="300" />
</div>


# Version