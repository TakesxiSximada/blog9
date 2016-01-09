Title: Pelicanのセットアップ
Date: 2016-01-09 19:00
Category: pelican
Tags: pelican, python, markdown
Author: TakesxiSximada
Summary: Pelicanのセットアップ

# インストール

Pelicanをインストールします。venvなどは適時使ってください。今回はenvという名前でvenv環境を作ります。

```
$ python -m venv env
$ source env/bin/bin/activate
```

env環境のpipを使ってpelicanをインストールします。

```
(env) $ pip install pelican
DEPRECATION: --download-cache has been deprecated and will be removed in the future. Pip now automatically uses and configures its cache.
Collecting pelican
  Using cached pelican-3.6.3-py2.py3-none-any.whl
Collecting docutils (from pelican)
  Using cached docutils-0.12-py3-none-any.whl
Collecting pytz>=0a (from pelican)
  Using cached pytz-2015.7-py2.py3-none-any.whl
Collecting unidecode (from pelican)
  Using cached Unidecode-0.04.18.tar.gz
Collecting six>=1.4 (from pelican)
  Using cached six-1.10.0-py2.py3-none-any.whl
Collecting feedgenerator>=1.6 (from pelican)
  Using cached feedgenerator-1.7.tar.gz
Collecting pygments (from pelican)
  Using cached Pygments-2.0.2-py3-none-any.whl
Collecting jinja2>=2.7 (from pelican)
  Using cached Jinja2-2.8-py2.py3-none-any.whl
Collecting python-dateutil (from pelican)
  Using cached python_dateutil-2.4.2-py2.py3-none-any.whl
Collecting blinker (from pelican)
Collecting MarkupSafe (from jinja2>=2.7->pelican)
Installing collected packages: docutils, pytz, unidecode, six, feedgenerator, pygments, MarkupSafe, jinja2, python-dateutil, blinker, pelican
  Running setup.py install for unidecode
  Running setup.py install for feedgenerator
Successfully installed MarkupSafe-0.23 blinker-1.4 docutils-0.12 feedgenerator-1.7 jinja2-2.8 pelican-3.6.3 pygments-2.0.2 python-dateutil-2.4.2 pytz-2015.7 six-1.10.0 unidecode-0.4.18
```

ReSTで記事を書いていくのもよかったのですが、コードスニペット貼り付けるときにReSTだとインデントしてあげないといけないのと、他のメディアに記述したドキュメントを保持しておくときにMarkdownに直す必要に迫られそうだったので、Markdownで記事を書いていく事にします。Pelicanは[Markdown](https://pypi.python.org/pypi/Markdown)パッケージがインストールされていれば、ファイル名をmdにしておくだけでMarkdownをパースしてHTMLを生成します。そのため[Markdown](https://pypi.python.org/pypi/Markdown)パッケージをインストールします。

```
(env) $ pip install Markdown
DEPRECATION: --download-cache has been deprecated and will be removed in the future. Pip now automatically uses and configures its cache.
Collecting Markdown
  Using cached Markdown-2.6.5.tar.gz
Installing collected packages: Markdown
  Running setup.py install for Markdown
Successfully installed Markdown-2.6.5
```

# scaffolding

pelican-quickstartコマンドを使ってscaffoldingします。


```
(env) $ pelican-quickstart
Welcome to pelican-quickstart v3.6.3.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? sximada 2016
> Who will be the author of this web site? TakesxiSximada
> What will be the default language of this web site? [en] ja
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
> What is your URL prefix? (see above example; no trailing slash) https://takesxisximada.github.io/sximada.2016
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Asia/Tokyo
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N)
Done. Your new project is available at /Users/sximada/ng/var/src/develop/sximada.2016
$
```

# テーマの変更

Pelicanのテーマの多くが[pelican-themes](https://github.com/getpelican/pelican-themes)に集められており、[www.pelicanthemes.com](http://www.pelicanthemes.com/)でスクリーンキャプチャを確認できます。一通り見た中から[pelican-twitchy](https://github.com/ingwinlu/pelican-twitchy)を使う事にします。

[pelican-themes](https://github.com/getpelican/pelican-themes)をまるっと取得すると、ダウンロードのに時間がかかってしまうので[pelican-twitchy](https://github.com/ingwinlu/pelican-twitchy)だけリポジトリのサブモジュールとしてthemes/pelican-twitchyに取得するようにします。

```sh
(env) $ mkdir themes
(env) $ git submodule add git@github.com:ingwinlu/pelican-twitchy.git themes/pelican-twitchy
```

sumoduleを登録し取得したらpelicanconf.pyにthemeの指定をします。

pelicanconf.py:

```python
THEME = 'themes/pelican-twitchy'
```

htmlを生成し直します。


```sh
$ make html
```

# Github Pages

現状のRemoteリポジトリにpushします。

```
(env) $ git remote add origin git@github.com:TakesxiSximada/sximada.2016.git
(env) $ git push --set-upstream origin master
```

Github Pagesはgh-pagesというブランチを作ることで公開されます。Pelicanがscaffolding時に生成するMakefileは`make github`というコマンドが使えるようになっており、github pagesにdeployしてくれます。`make github`ではghp-importというコマンドが使われています。このコマンドはghp-importパッケージが提供しているのでインストールしておきます。

```
(env) $ pip install ghp-import
```

requirements.txtも更新しておきましょう。

```
(env) $ pip freeze > requirements.txt
```

`make github`でHTMLを生成してgh-pagesブランチにpushします。

```
(env) $ make github
```

# CircleCIにdeployさせる

masterにpushしたときに`make github`を実行してdeployするようにします。circle.ymlは以下のように記述します。

```
machine:
  python:
      version: 3.5.0
test:
  override:
    - make html
deployment:
  release:
    branch: master
    commands:
      - git config user.name circleci
      - git config user.email circleci
      - make github
```
