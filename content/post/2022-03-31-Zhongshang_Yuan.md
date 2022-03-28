---
title: '03-31-2022 两样本孟德尔随机化(Mendelian randomization, MR)联合似然MRAID统计方法进行因果分析推断'
date: '2022-03-31'
archive: ["2022", "2022-03", "2022-03-31"]
categories:
  - 学术报告
tags: [talks, Mendelian randomization, horizontal pleiotropic effects, automated instrument selection, joint likelihood framework, Gibbs sampling]
show_comments: true
thumbnail: ""
---

- 题目：Likelihood based Mendelian randomization analysis with automated instrument selection and horizontal pleiotropic modeling
- 地点：- Zoom会议 ID：861 0146 4725 密码：269044
- Zoom会议链接：https://us06web.zoom.us/j/86101464725?pwd=bXphV2NYdGRZeVRaZys0WnNjczF4Zz09
- 主讲人袁中尚，山东大学生物统计学系教授，博导，齐鲁青年学者，国家健康医疗大数据研究院跨组学研究中心PI，博士毕业于武汉大学概率论与数理统计专业，国际生物统计学会中国分会副秘书长，中国卫生信息与健康医疗大数据学会统计理论与方法专委会委员，中国数学会医学数学专委会委员。先后访问美国北卡大学(UNC-CH)生物统计学系、密歇根大学生物统计学系/统计遗传中心，主要研究方向为跨组学数据整合与系统流行病学统计理论方法，先后主持国家自然科学基金项目4项、省基金重大基础研究1项，国家重点研发计划子课题等，成果以方法学论文先后发表在Science advances、Nature Communications、American Journal of Human Genetics、Statistics in Medicine等杂志, 参编专著1部。

<div align="center">
<img src="https://github.com/cgmonline/cgmonline/blob/master/image/2022_Zhongshang_Yuan.jpg?raw=true" height=250>
</div>

# 中文摘要
Mendelian randomization (MR) is a common tool for identifying causal risk factors underlying diseases. Here, we present a method, MRAID, for effective MR analysis. MRAID borrows ideas from fine mapping analysis to model an initial set of candidate SNPs that are in potentially high linkage disequilibrium with each other and automatically selects among them the suitable instruments for causal inference. MRAID also explicitly models both uncorrelated and correlated horizontal pleiotropic effects that are widespread for complex trait analysis. MRAID achieves both tasks through a joint likelihood framework and relies on a scalable sampling-based algorithm to compute calibrated p-values. Comprehensive and realistic simulations show MRAID can provide calibrated type I error control, reduce false positives, while being more powerful than existing approaches. We illustrate the benefits of MRAID for an MR screening analysis across 645 trait pairs in UK Biobank, identifying multiple lifestyle causal risk factors of cardiovascular disease-related traits.

# 参考文献
Yuan Z, Liu L, Guo P, Yan R, Xue F, Zhou X. Likelihood-based Mendelian randomization analysis with automated instrument selection and horizontal pleiotropic modeling. Sci Adv 2022.

# 关键词
Mendelian randomization, horizontal pleiotropic effects, automated instrument selection, joint likelihood framework, Gibbs sampling
