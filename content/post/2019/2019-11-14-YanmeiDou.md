---
title: "CGM 第72期：MosaicForecast: accurate detection of mosaic variants in sequencing data without matched controls"
date: "2019-11-13T20:00:00.000Z"
archive: ["2019","2019-11","2019-11-13"]
categories:
  - 学术报告
tags: [talks, mosaic variant, haplotype phasing, machine learning]
show_comments: true
thumbnail: "https://imgur.com/XquzzUl.jpg"
---


- 题目：MosaicForecast: accurate detection of mosaic variants in sequencing data without matched controls
- 时间：2019 年 11 月 13 号（星期三），美西时间（Pacific Time）6:00 PM
- 地点：Zoom and YouTube live stream
- 主讲人： 窦岩梅，本科毕业于北京科技大学，2011-2017年在北京大学师从魏丽萍教授攻读生物信息学博士学位，现于哈佛医学院 Dr. Peter J Park lab 进行博士后研究。

# 中文摘要

近年来，体细胞突变被证明与越来越多的非癌症人来疾病相关，并且在研究人体发育过程中发挥着重要作用。然而检测健康人群和非癌症疾病人群中的体细胞突变主要存在两大困难：

1. 由于非癌样本中的体细胞突变往往没有选择优势，突变等位基因频率往往很低，很难和测序杂音分开；

2. 由于突变伴随人体发育过程发生，往往存在于多个组织器官中，所以缺乏“对照正常组织”来检测突变。

我们开发了一个机器学习方法“MosaicForecast”，它通过局部haplotype phasing来产生训练集，并提取>30个read-level features来准确检测单个样本NGS测序数据中的体细胞突变（SNV和短indel）。

通过和其他工具的比较，MosaicForecast在维持高灵敏度的情况下载准确度上产生了几倍到几十倍的提高，我们的实验验证显示验证率高达80-90%。

# YouTuBe

{{< youtube id="UFlinXHGpFc" autoplay="false" >}}


# Bilibili

{{< bilibili id="75634831" autoplay="false" >}}


# 参考文献

Dou et al. [Detecting somatic mutations in normal cells](https://compbio.hms.harvard.edu/publications/detecting-somatic-mutations-normal-cells), Trends in Genetics, 2018

Dou et al. [MosaicForecast: accurate detection of mosaic variants in sequencing data without matched controls](https://compbio.hms.harvard.edu/publications/mosaicforecast-accurate-detection-mosaic-variants-sequencing-data-without), Nature Biotechnology, in press, 2019
