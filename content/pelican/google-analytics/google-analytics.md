Title: pelican-twitchyでのGoogleAnalyticsの設定
Date: 2016-01-11 12:00
Category: pelican
Tags: pelican, google analytics
Author: TakesxiSximada
Summary: pelican-twitchyでのGoogleAnalyticsの設定

pelican-twitchyのGoogleAnalyticsの設定は[pelican-twitchyのREADME](https://github.com/ingwinlu/pelican-twitchy#google-analytics)に記載されています。通常のトラッキングIDを設定してみます。

pelicanconf.pyに次の設定を追加します。

pelicanconf.py:

```
GOOGLE_ANALYTICS = 'UA-00000000-1'  # Tracking ID
```

これだけです。あとはHTMLを生成し直してHTMLをアップロードすれば良いでしょう。簡単ですね。
