# CGMonline

## How to contribute to the website

This website is built using R package `[blogdown](https://github.com/rstudio/blogdown)`. 
`blogdown` depends on `[hugo](https://gohugo.io/)`, so we have to install hugo.

```{r}
install.packages("devtools")
devtools::install_github('rstudio/blogdown')

### install hugo
blogdown::install_hugo()
```

