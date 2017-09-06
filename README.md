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
git clone git@github.com:MYID/cgmonline.git
```

#### 2. Create or edit files in `content/post/`.
Note, to add a new post, follow our naming convention `year-month-day-some-words-as-title.md`.

#### 3. Deploy your changes
Run the following command to compile the md file into html, git add and git commit.
```
sh deploy.sh
```
#### 4. Create a new Pull Request


## Copyright & License
The [MIT License](LICENSE) (MIT), Copyright (c) 2016.
