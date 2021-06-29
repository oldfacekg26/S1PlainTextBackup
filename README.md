# 简介 
![Update S1](https://github.com/TomoeMami/S1PlainTextBackup/workflows/Update%20S1/badge.svg)

本仓库用来存放S1部分高楼的纯文本备份，以50楼为一份文件，请善用搜索功能。

本仓库仅存放半个月内翻过页的、超过4页的帖子。

若半个月内没有翻页，该帖子的纯文本备份会被挪到此仓库：

2020-2021年历史存档 https://github.com/TomoeMami/S1PlainTextArchive2021

如果内容与时间无强相关，则会被挪至此仓库：

S1跨越年限的高楼纯文本归档 https://github.com/TomoeMami/S1PlainTextGeneral

## 全文搜索方式：
网页栏里在github后面加上1s，变成github1s.com，按下回车即可在网页版vscode中打开本repo，然后在左侧边栏点击第二个图标，即可进入搜索界面。

本仓库的搜索界面：https://github1s.com/TomoeMami/S1PlainTextBackup

## 2021-01-08 增加GithubAction支持

#### 触发方式

- 每隔15分钟定时执行+推送后立即执行

- 自定义：.github/workflows/S1.yaml 编辑

#### 使用用法
- 点击右上角 `Fork` 项目
- `Settings` -> `Secrets` 中添加s1的账号Cookie
    - `S1_COOKIE`：账号Cookie

### 目前支持的特殊效果

- 粗体
- 链接
- 图片
    - jpg
    - jpeg
    - png
    - gif
    - tif
    - webp
- 评分

 ## 脚本使用须知

- `RefreshingData.json`的数据格式（可用`simpleadd.py`快速添加）：
    - id：代表帖子id
    - totalreply：新帖子为0
    - title：代表帖子标题
    - lastedit：代表最后更新时间
    - category：代表放进哪个文件夹
    - active：标为false的帖子不会被更新
- 为确保可被GitHub网页渲染，单个文件大小需控制在1M以内，故以50页为限，拆分成多个文件。
- 所有图片采取markdown格式链接，均为网络图片，不保证可用性。
    - 如果加载不出来请采用网络加速手段，因为GitHub的markdown预览会把图片先自己缓存一次，所以你获取图片的来源就变成了GitHub了。
    - 也可以把md文件下载到本地用本地markdown客户端进行预览，这样你就是直连的图片源。
    - Gitee不会帮你缓存图片，会和本地markdown客户端一样直连图片源。
- `sactive.py` 运行之后会把`RefreshingData.json`里的帖子一一比对，距离上次回帖1个月以内的帖子会设置为`"active": true`。
- `sclean.py` 运行之后会把`RefreshingData.json`里的`"active": false`帖子全部删除，仅留`"active": true`帖子。
- 如需要本地图文备份，请采用这个备份工具：[S1Downloader](https://github.com/shuangluoxss/Stage1st-downloader)
- 代码写得很烂，还请多多包涵！如果有需要我保存的专楼，可以给我提issue或者在S1私信我。
- 三号四号疫情专楼的备份来自于https://gitlab.com/memory-s1/virus 
- 2021-06-08 更新方式改为增量更新，如遇S1炸了出现大量【已归档】[]文件，则需完全回退，或利用`sactive.py`重新激活。
