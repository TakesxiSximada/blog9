Title: 特定のブランチだけCircleCIのbuildを走らせない
Date: 2016-01-10 19:00
Category: GoogleApps
Tags: CircleCI
Author: TakesxiSximada
Summary: 特定のブランチだけCircleCIのbuildを走らせない


Github PagesでPelicanをブログを書きCircleCIにdeployをさせているとgh-pagesへpushされた場合にbuildを走らせたくなかったので、その時のメモ。

circle.ymlに以下を書き込むと無視されるようになります。

```
general:
  branches:
    ignore:
      - gh-pages
```

参考にしたサイト

[circleciで特定のbranchの時のみtestを無視する - とある元SEの学習日記](http://cross-black777.hatenablog.com/entry/2015/07/20/231044)
[Configuring CircleCI](https://circleci.com/docs/configuration)