# horti_job
用Python的Selenium框架爬取园艺类工作的招聘数据

---

1. #### 计划：

计划爬取**拉勾网**，**Boss直聘**，**智联招聘**三个网站的信息，然后汇总进行数据分析，看看园艺类工作的“行情”如何，**学成文武艺，货与资本家**。

---

2. #### 问题记录：

因为现在Boss直聘与智联招聘开始反扒虫，所以简单的用Selenium爬取数据是不可能了，都是卡在加载招聘信息的页面上。后来在网上搜索一番后我发现了一个神器"**后羿采集器**"，相当于可视化版本Selenium，我用它爬取了Boss直聘的数据。可是智联招聘❌依然不能爬取。——2020.5.11

---

3. #### 工作进度：

2020.5.10——拉勾网✅（[代码](https://github.com/Bolonzhang/horti_job/blob/master/lagou2.0.py)、[数据](https://github.com/Bolonzhang/horti_job/blob/master/lagou_jobs.csv)）

2020.5.11——Boss直聘✅([数据](https://github.com/Bolonzhang/horti_job/blob/master/boss_jobs.csv))

---

4. #### 数据数量
| **拉勾网** | **Boss直聘** |
| :----: | :----: |
| 63 | 295 |
| 共358条招聘数据 |

---

5. #### 数据分析报告
个人微信公众号链接：[园艺类工作的招聘数据分析1.0](https://mp.weixin.qq.com/s?__biz=MzI5ODk0MTk4OQ==&mid=2247484528&idx=1&sn=42a47b08723522001354ebec6928664d&chksm=ec9f6f3adbe8e62c0d797aa14332bf4cb5b8c0e923c0e3b0bdf246a9ef227fa6be83b3bf753e&token=1197430884&lang=zh_CN#rd0)

---

6. #### 联系方式
微信公众号：波龙兄/bolonxiong

Email：786445578@qq.com
