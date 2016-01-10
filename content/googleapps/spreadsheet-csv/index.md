Title: Google SpreadsheetにCSVを定期的にimportする
Date: 2016-01-10 19:00
Category: GoogleApps
Tags: GoogleSpreadsheet, CSV
Author: TakesxiSximada
Summary: Google SpreadsheetにCSVを定期的にimportする



可視化や集計のためにGoogle Spreadsheetを使用していてデータソースを外部から取得している場合、CSVのデータを定期的に更新したくなります。Google Scriptでそれを解決する方法をまとめます。


# Google Scriptの使い方

Google Spreadsheetのメニューから [ツール] > [スクリプトエディター] を選択します。

![スプレッドシート]({filename}/static/images/google-spread-sheet-capture/spreadsheet.png)

選択すると別のタブでスクリプトエディタが開きます。

![スクリプトエディター]({filename}/static/images/google-spread-sheet-capture/script_editor.png)

ここにスクリプトを書いていきます。

実行するためにはプロジェクトとして保存する必要があるのでC-sで保存しておきます。

![プロジェクトの保存]({filename}/static/images/google-spread-sheet-capture/save_project.png)

# CSVをダウンロードして反映する

Webに公開されているCSVをダウンロードしてシートに反映します。スクリプトエディタで以下のスクリプトを書き保存します。

```


function load_csv(){
  var url = 'http://www.tsuchiya2.org/CSV_file_seisaku/sampleCSV/sample1.csv';
  var sheet_name = 'test';
  var csv_txt = download_csv(url);
  var data = CSVToArray(csv_txt, ',');
  var book = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = book.getSheetByName(sheet_name);
  var record;
  for (var ii=0; ii < data.length; ii++){
    record = sheet.getRange(ii+1, 1, 1, data[ii].length);
    record.setValues(new Array(data[ii]));
  }
}

function download_csv(url) {
  var res = UrlFetchApp.fetch(url);
  var content = res.getContentText('UTF-8');
  return content.toString();
}

// See https://developers.google.com/apps-script/articles/docslist_tutorial
function CSVToArray( strData, strDelimiter ){
  // Check to see if the delimiter is defined. If not,
  // then default to comma.
  strDelimiter = (strDelimiter || ",");

  // Create a regular expression to parse the CSV values.
  var objPattern = new RegExp(
    (
      // Delimiters.
      "(\\" + strDelimiter + "|\\r?\\n|\\r|^)" +

      // Quoted fields.
      "(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +

      // Standard fields.
      "([^\"\\" + strDelimiter + "\\r\\n]*))"
    ),
    "gi"
  );


  // Create an array to hold our data. Give the array
  // a default empty first row.
  var arrData = [[]];

  // Create an array to hold our individual pattern
  // matching groups.
  var arrMatches = null;


  // Keep looping over the regular expression matches
  // until we can no longer find a match.
  while (arrMatches = objPattern.exec( strData )){

    // Get the delimiter that was found.
    var strMatchedDelimiter = arrMatches[ 1 ];

    // Check to see if the given delimiter has a length
    // (is not the start of string) and if it matches
    // field delimiter. If id does not, then we know
    // that this delimiter is a row delimiter.
    if (
      strMatchedDelimiter.length &&
      (strMatchedDelimiter != strDelimiter)
    ){

      // Since we have reached a new row of data,
      // add an empty row to our data array.
      arrData.push( [] );

    }


    // Now that we have our delimiter out of the way,
    // let's check to see which kind of value we
    // captured (quoted or unquoted).
    if (arrMatches[ 2 ]){

      // We found a quoted value. When we capture
      // this value, unescape any double quotes.
      var strMatchedValue = arrMatches[ 2 ].replace(
        new RegExp( "\"\"", "g" ),
        "\""
      );

    } else {

      // We found a non-quoted value.
      var strMatchedValue = arrMatches[ 3 ];

    }


    // Now that we have our value string, let's add
    // it to the data array.
    arrData[ arrData.length - 1 ].push( strMatchedValue );
  }

  // Return the parsed data.
  return( arrData );
}
```

load_csv()とdownload_csv()とCSVToArray()の3つを定義しました。load_csv()はCSVをDLしシートに反映します。download_csv()はCSVをDLしtextにして返します。CSVToArray()はCSV形式のtextをArrayにして返します。CSVToArray()は[Googleのチュートリアル](https://developers.google.com/apps-script/articles/docslist_tutorial)にあるものをそのままコピペしました。

実行するには [実行] > [load_csv] を選択します。load_csvの箇所は関数名になっているので別名で定義した場合は定義した名前になります。このスクリプトではそのSpreadsheetのtestというsheetに対してCSVのデータを反映しています。

![スクリプトの実行]({filename}/static/images/google-spread-sheet-capture/execute_script.png)

# 定期実行

スクリプトエディターでは作成したスクリプトを実行させるトリガーを設定できます。メニューから [リソース] > [現在のプロジェクトのトリガー] を選択します。

![現在のプロジェクトのトリガー]({filename}/static/images/google-spread-sheet-capture/current_trigger.png)

ダイアログが開き現在登録されているトリガーが一覧で確認できます。

![現在のプロジェクトのトリガー(ダイアログ)]({filename}/static/images/google-spread-sheet-capture/current_trigger_dialog.png)

トリガーを追加するにはダイアログの追加をクリックします。今回は一定間隔で定期実行させたいので時間主導型のイベントを設定します。

![トリガーの登録]({filename}/static/images/google-spread-sheet-capture/register_trigger.png)

またスクリプト実行時のエラーを通知できます。通知をクリックすると登録用ダイアログが開きます。

![通知]({filename}/static/images/google-spread-sheet-capture/register_notification.png)

このように登録しておくとSpreadsheetを閉じた状態でもデータを更新し続けます。
