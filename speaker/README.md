# speaker/ — 自动发布讲者报告

把一个讲者的 `.md` 文件放进这个目录并 `git push`，对应的学术报告会自动发布到
[cgmonline.co](https://cgmonline.co)（栏目「学术报告」）。

## 工作流程

1. 复制 [`TEMPLATE.md`](TEMPLATE.md)，重命名（建议 `YYYY-MM-DD_缩写.md`）。
2. 填写 YAML front matter 与正文（`# 主讲人简介`、`# 中文摘要`）。
3. 把讲者照片放到仓库根目录的 `image/`，文件名与 front matter 里的 `photo` 一致
   （建议 `<日期>_<slug>.jpg`）。
4. `git add speaker/你的文件.md image/你的照片.jpg && git commit && git push`。

推送后，GitHub Actions（`.github/workflows/publish-speaker.yml`）自动运行
`scripts/build_speaker.py`，把 `speaker/*.md` 转换成 `content/post/<日期>_<slug>.md`
并提交回仓库。**Netlify** 随即从源码重新构建并发布站点。

## 必填字段

| 字段 | 说明 |
|------|------|
| `title` | 报告题目（脚本会自动加 `MM-DD-YYYY` 前缀） |
| `speaker` | 主讲人姓名 |
| `slug` | 文件名后缀（拼音首字母，如 `THD`） |
| `date` | 报告日期 `YYYY-MM-DD` |

其余字段（`time`、`location`、`zoom_link`、`affiliation`、`position`、`keywords`、
`photo`、`references`）均为可选。

## 注意事项

- **未来日期的报告**：站点的 Netlify 构建需带 `-F`（`--buildFuture`）才会显示尚未到日期的报告，
  仓库里的 `deploy_netlify.sh` 已使用 `hugo -F`。
- 本地预览：`python3 scripts/build_speaker.py && hugo -F`。
- `TEMPLATE.md` 和 `README.md` 会被脚本忽略。
