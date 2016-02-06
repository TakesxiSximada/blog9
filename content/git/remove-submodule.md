Title: Gitのサブモジュールを消し去りたい
Date: 2016-01-10 19:00
Category: GoogleApps
Tags: Git
Author: TakesxiSximada
Summary: Gitサブモジュールを消たくなり毎回やり方を忘れてググっている君(俺)へ

git submoduleを使うと複数のリポジトリをまとめることができます。
しかし開発を続けていくと `この構成じゃ無いな` と思い直すことがあります。
そんなふとした瞬間にサブモジュールを邪魔に感じて消したくなるのです。

さあ今すぐそのサブモジュールを消しましょう。

サブモジュールの位置を確認します。 (path/to/submodule/directoryがサブモジュールとします)

```
$ git submodule
-33658f26c1f9346dfcae92d35da0d98b4beaac61 path/to/submodule/directory
```

`git submodule deinit` でサブモジュールを解除します。

```
$ git submodule deinit path/to/submodule/directory
Cleared directory 'path/to/submodule/directory'
```

サブモジュールの位置にあったツリーを削除します。

```
$ git rm path/to/submodule/directory
rm 'path/to/submodule/directory'
```

コミットします。

```
$ git commit
[feature/delete-submodule 8795ba0] submoduleを消し去る
 2 files changed, 4 deletions(-)
  delete mode 160000 path/to/submodule/directory
$
```

さようなら、サブモジュール。
