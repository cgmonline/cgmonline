# CGMonline

## Requirement:
1. You need a `github` account.
2. Install [hugo](https://gohugo.io/) following this [page](https://gohugo.io/getting-started/quick-start/).
OR:
If you are an `R` user, you can install R package [`blogdown`](https://github.com/rstudio/blogdown) and then install hugo using blogdown.

```{r}
install.packages("devtools")
devtools::install_github('rstudio/blogdown')

### install hugo
blogdown::install_hugo()
```

## How to contribute


#### 1. `Fork` this repo and `clone` it to your disc.
```
git clone git@github.com:<USERNAME>/cgmonline.git
cd cgmonline
git remote add upstream https://github.com/cgmonline/cgmonline.git
git remote -v
```
You should see:
```
origin	https://github.com/<USERNAME>/cgmonline (fetch)
origin	https://github.com/<USERNAME>/cgmonline (push)
upstream	https://github.com/cgmonline/cgmonline (fetch)
upstream	https://github.com/cgmonline/cgmonline (push)
```
Sync your local repo with the main cgm repo:
```
git fetch upstream
git checkout master
git merge upstream/master
```

#### 2. 发布预告

Modify the `content/coming.md` file accordingly.

#### 3. 转移到讨论列表

Create or edit files in `content/post/` in your local repo.
Note, to add a new post, follow our naming convention `year-month-day-some-words-as-title.md`.
You need an imgur account to post a nice picture that normally just obtained from google as a __thumbnail__.

#### 4. Deploy your changes
Run the following command to compile the md file into html, git add and git commit.
```
sh deploy.sh
```
#### 5. Create a new Pull Request on Github


## Copyright & License
The [MIT License](LICENSE) (MIT), Copyright (c) 2019.
