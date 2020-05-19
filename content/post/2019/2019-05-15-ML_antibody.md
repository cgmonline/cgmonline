---
title: "CGM 第53期：人工智能在抗体中的应用"
date: "2019-05-15T20:00:00.000Z"
archive: ["2019","2019-05","2019-05-15"]
categories:
  - 学术报告
tags: [talks, ML,Antibody]
show_comments: true
thumbnail: "https://i.imgur.com/qfEKyKQ.jpg"
---


- 题目：The quest for the ideal antibody, AI driven product knowledge extraction from scientific publications （人工智能在抗体中的应用）
- 时间：2019 年 05 月 15 号（星期三），美西时间（Pacific Time）6:00 PM
- 地点：YouTube live stream
- 主讲人：陈启翔 (David Qixiang Chen) CTO, Director of AI, BenchSci; PhD Neuroimaging, Institute of Medical Science, University of Toronto


# 英文摘要

The antibody, an important part of the immune system, is a widely used reagent of biomedical experiments. Misuse of antibodies, often due to insufficient data, are responsible for up to 50% of failed experiments, and incur enormous cost in time and money for drug discovery. 

The best evidence of antibody use, and other scientific products, are found in scientific publications. Existing publication search tools (pubmed, google scholar) are not meant for products. We decoded antibody experimental contexts from open and close-source publications with a combination of text mining, bioinformatics, and machine learning. 

At the end of the day, scientists prefer to judge experimental outcome by inspecting the publication images. We linked antibody contexts to its figure image, by identifying the correct product from amongst 4M antibodies, within 9M publications, across 300K contexts, and associate them with over 37M protein aliases. This complex task was computed using Spark and the search served on Elasticsearch. Deep neural nets were used to judge product/context usage relationship (embeddings, LSTM with attention), and to identify technique subpanel (CNN) in figures to fine-tune data accuracy.

The mission for BenchSci is to close the gap between idea to outcome in science. We accelerate the pace of discoveries by removing roadblocks in the scientific iteration cycle. ML has proven to be indispensable, where the scaling of data processing with a small team could only have been achieved through the use of deep learning.


# 参考文献
1.	Baker, M., 2015. Reproducibility crisis: Blame it on the antibodies. Nature News, 521(7552), p.274.
2.	LeCun, Y., Bengio, Y. and Hinton, G., 2015. Deep learning. nature, 521(7553), p.436.





# YouTube

{{< youtube id="2n4r2XV139E" autoplay="false" >}}

# Tencent video

{{< tencent id="q087119gs40" autoplay="false" >}}
