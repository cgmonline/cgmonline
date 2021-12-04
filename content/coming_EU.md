---
title: "欧洲区预告"
date: "2021-12-09"
menu: [top]
weight: 4
---

- 题目：CGM 第199期: 长读长测序组装单倍型基因组方法的开发
- 时间：欧洲中部时间 2021 年 12 月 9 号（星期四）08 PM（美国中部时间 12 月 9 号 01PM，北京时间 12 月 10 号 03AM）
- Zoom会议 ID：861 0146 4725 密码：269044 
- Zoom会议链接：https://us06web.zoom.us/j/86101464725?pwd=bXphV2NYdGRZeVRaZys0WnNjczF4Zz09
- 主讲人：罗宵, 华中科技大学 本科, 中国科学院大学 硕士, 荷兰国家数学与计算机科学研究中心 & 德国比勒费尔德大学 博士


<div align="center">
<img src="https://i.ibb.co/sP9V2zN/L1.jpg" height=250>
</div>

# 中文摘要

生物的遗传与变异使得同一物种的基因组通常有着丰富的多样性。例如，二倍体高等生物含有两个基因组拷贝，其中一个单倍型来自父本，另一个来自母本；病毒在宿主体内发生变异，可能产生新的亚种(毒株)。构建单倍型(haplotype)或者株(strain)水平的基因组序列称为单倍型水平基因组组装，其在基因组学、精准医学、病毒防控等许多领域有着重要的作用。

二代测序由于其较短的读长，因而在单倍型水平基因组组装方面存在不足。近年来随着三代测序(如PacBio, Nanopore)的快速发展，其测序准确度大幅提高(错误率5%~15%, 尤其 PacBio HiFi <1%)，成本也进一步降低。由于其长读长的天然优势被广泛应用于基因组组装，使得单倍型水平基因组组装成为可能。现有的基因组序列组装方法主要包括两类：第一类是从头组装(de novo assembly), 这类方法通常不依赖于参考基因组，一般不考虑单倍型之间的差异，直接组装出共同序列(consensus)， 但损失了一部分单倍型信息; 第二类方法基于参考基因组(reference based)构建单倍型, 通常会引入参考基因组偏差(reference bias)，且依赖于高质量的参考基因组。

为弥补现有研究的不足，我们开发了适用于三代测序数据的单倍型水平基因组从头组装方法：phasebook 用于二倍体的基因组组装，Strainline 用于病毒的基因组组装。在模拟和真实数据上测试结果表明，与现有方法相比，我们的方法在单倍型完整性(haplotype completeness)，错误率(error rate)等指标上表现出明显的优势。

# 参考文献
1.Luo, X., Kang, X. & Schönhuth, A. phasebook: haplotype-aware de novo assembly of diploid genomes from long reads. Genome Biol 22, 299 (2021).

2.Luo, X., Kang, X. & Schönhuth, A. Strainline: full-length de novo viral haplotype reconstruction from noisy long reads. bioRxiv (2021).
