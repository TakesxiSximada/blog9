Title: GoogleAnalyticsの情報をSlackに通知する
Date: 2016-01-21 19:00
Category: GoogleApps
Tags: GoogleAnalytics, Slack
Author: TakesxiSximada
Summary: GoogleAnalyticsのレポートをブラウザでいちいち閲覧しにいくのは面倒なのでSlackに定期的に通知します。

GoogleAnalyticsのレポートをブラウザでいちいち閲覧しにいくのは面倒なのでSlackに定期的に通知します。

# Slack側

## Incomming Webhook URLを取得する

WebhookでSlackにメッセージを送るための`Incomming Webhook`というインテグレーションがあります。その機能を有効化します。
https://<YOUR-DOMAIN>.slack.com/home にアクセスすると設定されているインテグレーションを確認できます。

![https://<YOUR-DOMAIN>.slack.com/home]({filename}/static/images/slack-capture/intergrations-incomming-webhook.png)

このような表示があればすでに設定されています。なければインテグレーションを有効化してください。有効化は`Add Application`ボタンから追加できます。
有効化したらWebhookのURLを発行します。

![IncommingWebhook URLの発行.1]({filename}/static/images/slack-capture/add-configuration-incomming-webhook.png)

`Add configuration`で追加画面に遷移します。

![IncommingWebhook URLの発行.2]({filename}/static/images/slack-capture/add-incomming-webhook-integration.png)

追加画面では通知先のチャネルを指定して `Add Incomming Webhook Integration` を押下します。すると以下のようなページが表示され、WebhookのURLを確認できます。

![Incomming Webhook]({filename}/static/images/slack-capture/webhook-url.png)

ここで生成したURLはどのようなクライアントからでも受け付けてくれます。

# Google Apps側

Google Apps側の設定をしていきます。

## Google Analyticsのidsを取得する

GoogleAlalyticsの情報を読み取るためにはAnalyticsのidsを使います。そのためまずこのidsを確認します。
事前にAPIの有効化を行います。APIの有効化は[Google Developpers Console](https://console.developers.google.com/apis/library)とSpreadsheetの両方で行う必要があります。
次にSpreadsheetにGoogleAlalytisc addonを入れます。正常に入ると`Google Analytics`というメニューが追加されます。

![GoogleAlalytisc addon]({filename}/static/images/google-spread-sheet-capture/google-spreadsheet-google-analytics-addon.png)

続いて `Google Analytics` > `Find Profile / ids` を実行します。このときにアクセス権を求められるので許可します。

![Find Profile / ids]{filename}/static/images/slack-capture/get-gaids.png)

実行結果はこのように出力されます。`ids`が今回使う値になります。

## GoogleAnalyticsの情報を取得してSlackに通知するGoogle Apps scriptを書く

スクリプトエディタを開いて以下のコードを書きます。先ほど取得したSlackのIncomming Webhook URLとGoogl Analyticsのidsはとりあえずコードの中に埋め込んでしまいました。
必要であればSpreadsheetから取得するようにしても良いかもしれません。

```
function notify(){
  var ga = Analytics.Data.Ga.get(
    "ga:*********",  // GoogleAnalyticsのids
    "2016-01-01",  // 集計対象の開始日
    "2016-12-31",  // 集計対象の終了日
    "ga:visits,ga:pageviews");  // レポート項目(訪問者数,PV数)

  var msg = '[GoogleAnalytics] \n'
  var name = '';
  var value = '';
  for each(var name in ga.query.metrics){
    value = ga.totalsForAllResults[name]
    msg += name + ': ' + value + '\n';
  }

  // Slackに送るリクエストのオプションを作成
  var options  = {
    "method": "post",
    "Content-type": 'application/json',
    "payload": '{"text":"' + msg + '"}',
    };
  // SlackにPOST
  UrlFetchApp.fetch("https://hooks.slack.com/services/*********/*********/************************", options);
}
```

## 手動実行する

スクリプトを手動実行します。関数名をプルダウンで洗濯し再生ボタンで実行できます。ブレイクポイントをはって、虫マークでデバッグ実行もできます。
初回実行時には権限の許可を確認するダイアログが表示されます。それを許可します。

## トリガーを設定して定期実行する

トリガーを設定することで、一定間隔や決まった時間にスクリプトを実行できます。
今回は1日1回通知されればよいので、`時間主導型`, `日タイマー`, `正午〜午後1時`のトリガーを設定しました。

![トリガーの設定]({filename}/static/images/google-spread-sheet-capture/current_trigger.png)

## 通知を待つ

心を落ち着けて通知を待ちましょうw
