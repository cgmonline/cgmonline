args = commandArgs(trailingOnly=TRUE)
#devtools::install_github("Shicheng-Guo/openxlsx")
library("tidyverse")
library("openxlsx")
Sys.setlocale(category="LC_ALL",locale="chinese")
data<-read.xlsx("R/Hanqing_Liu_CGM_SpeakerInfoRequest.xlsx",sheet = 1,colNames = F)
data
firstname<-data[9,2]
lastname<-data[10,2]

l1<-"---"
l2<-"title: \"北美区预告\""
l3<-paste0("date: \'",data[3,2],"\'")
l4<-"menu: [top]"
l5<-"weight: 4"
l6<-"---"
l7<-paste0("- 题目：",data[1,2]," ",data[2,2])
l8<-"- 地点：Zoom and YouTube live stream"
l9<-"# 主讲人"
l10<-data[5,2]
l11<- '<div align="center">'
l12<- paste0('<img src="https://github.com/cgmonline/cgmonline/blob/master/image/2022_',firstname,"_",lastname,'.jpg?raw=true" height=250>')
l13<- '</div>'
l14 <-'# 中文摘要'
l15<-data[6,2]
l16 <-'# 参考文献'
l17<-data[7,2]
l18 <-"# 关键词"
l19<-data[4,2]
l20<-"参加方式"
l21<-"- Zoom会议链接: https://us06web.zoom.us/j/87870509801?pwd=SGpvdEc3YVRQL2twTmJyenhnTDFrZz09"
l22<-"- Zoom会议ID：878 7050 9801"
l23<-"- 密码：207409"
ll<-rbind(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23)
write.table(ll,file="./content/coming_US.md",sep="",quote=F,col.names = F,row.names = F)


l1<-"---"
l2<-paste0("title: \'",data[1,2]," ",data[2,2],"\'")
l3<-paste0("date: \'",data[3,2],"\'")
l4<-'archive: ["2021","2021-12","2021-12-22"]'
l5<-"categories:"
l6<-"  - 学术报告"
l7<-paste0("tags:[talks,",data[4,2],"]")
l8<-"show_comments: true"
l9<-'thumbnail: ""'
l10<-"---"
l11<-paste0("- 题目：",data[1,2],"-",data[2,2])
l12<-"- 地点：- Zoom会议 ID：861 0146 4725 密码：269044"
l13<-"- Zoom会议链接：https://us06web.zoom.us/j/86101464725?pwd=bXphV2NYdGRZeVRaZys0WnNjczF4Zz09"
l14<-paste0("- 主讲人",data[5,2])
l15<- '<div align="center">'
l16<- paste0('<img src="https://github.com/cgmonline/cgmonline/blob/master/image/2022_',firstname,"_",lastname,'.jpg?raw=true" height=250>')
l17<- '</div>'
l18 <-'# 中文摘要'
l19<-data[6,2]
l20 <-'# 参考文献'
l21<-data[7,2]
l22 <-"# 关键词"
l23<-data[4,2]
ll<-rbind(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23)
datex<-unlist(strsplit(data[3,2]," "))[1]
opt<-paste0("./content/post/",datex,"-",firstname,"_",lastname,".md")
opt
write.table(ll,file=opt,sep="",quote=F,col.names = F,row.names = F)



