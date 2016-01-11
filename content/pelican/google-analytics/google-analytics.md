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
GOOGLE_ANALYTICS = 'UA-72260316-1'  # Tracking ID
```

これだけです。あとはHTMLを生成し直してHTMLをアップロードすれば良いでしょう。

HTMLを確認します。

```
    <script type="text/javascript">

        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-72260316-1']);
        _gaq.push(['_trackPageview']);

        (function () {
            var ga = document.createElement('script');
            ga.type = 'text/javascript';
            ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(ga, s);
        })();
    </script>
```

上記のようなHTMLが出力されていればきちんと設定できています。簡単ですね。
