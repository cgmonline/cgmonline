---
title: "CGM 第42期：Using Machine Learning to Dissect Recombination Landscape"
date: "2018-11-14"
categories:
  - 学术报告
tags: [Machine Learning, Recombination, DNA, Double Strand Break]
show_comments: true
thumbnail: "https://i.imgur.com/BV8MyDe.png"
---


- 题目：Using Machine Learning to Dissect Recombination Landscape
- 时间：2018 年 11 月 14 号（星期三），美西时间（Pacific Time）6:00 PM
- 地点：YouTube live stream 
- 主讲人：王明辉（Minghui Wang）Cornell University

第一次减数分裂前，同源染色体会经历配对，联会和遗传物质重组交换等一系列过程。同源染色体遗传物质重组交换促进了遗传多样性的发生，进而为遗传育种及选种选育提供更多的原材料。减数分裂的重组过程是被严格调控的，它起始于DNA双链的断裂（double strand break），在RAD51及其它蛋白的作用下，DSB通过同源重组修复，一部分形成基因转换（gene conversion）个体，还有一部分形成重组（crossover）个体。玉米研究发现，DSB热点近乎均匀分布在玉米染色体，这些热点具有如下特征：较低的CG与CHG甲基化水平，主要分布在开放的染色质（open chromatin）区域与CG富及DNA结合基序（motif）。利用B73与Mo17回交群体，我们获取高精度的重组区间（<2000bp）。后续的研究发现，重组位置具有跟DSB相似的特征，较低的甲基化，开放染色质区域，较高的H3k4me3组蛋白修饰，此外也有一定特征的DNA基序。基于上述研究，我们认为基因组的与染色质特征，决定DSB与crossover发生位置。由于实验的难度及测序经费问题，目前的研究仅仅局限于B73。因此我们仅仅得到有限的DSB与crossover位置信息。基于已有的数据作为训练集，利用机器学习的方法，我们尝试基因组水平的DSB与crossover位点预测。结果发现，随机森林算法具有较高的精确度，准确度达到92%以上。不同的特征决定了DSB与重组位置的发生，H3K9me2，GC，CC，CG碱基频率与开放的染色质造就了DSB的发生，而DNA甲基化与开放的染色质决定重组位置的发生。

# 幻灯片和Youtube视频

{{< youtube id="16QRVQrcSyQ" autoplay="false" >}}

# 腾讯视频

{{< tencent id="f0883hdp9z1" autoplay="false" >}}

