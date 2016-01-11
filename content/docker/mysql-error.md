Title: docker-composeでMySQLを起動しようとすると[ERROR] InnoDB: Operating system error number 13 in a file operation.
Date: 2016-01-11 19:00
Category: Docker
Tags: Docker, docker-conpose, MySQL
Author: TakesxiSximada
Summary: docker-composeでMySQLを起動しようとすると[ERROR] InnoDB: Operating system error number 13 in a file operation.
Status: draft

docker-composeでMySQLを起動しようとすると起動に失敗する状態に陥りました。

docker-compose.ymlは以下のように記述しています。

```
mysql:
  image: mysql:latest
  ports:
    - :3306
  volumes:
    - data_mysql/volumes/mysql:/var/lib/mysql
  environment:
    MYSQL_ROOT_PASSWORD: toor
```

この状態でdocker-compose upします。

```
$ docker-compose up mysql
Attaching to mysql_1
~~~省略~~~
mysql_1 | Initializing database
mysql_1 | 2016-01-11T10:22:03.924035Z 0 [Warning] Setting lower_case_table_names=2 because file system for /var/lib/mysql/ is case insensitive
mysql_1 | 2016-01-11T10:22:03.955354Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
mysql_1 | 2016-01-11T10:22:03.955507Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
mysql_1 | 2016-01-11T10:22:03.956347Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
mysql_1 | 2016-01-11T10:22:03.956420Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
mysql_1 | 2016-01-11T10:22:03.956476Z 0 [ERROR] InnoDB: Cannot open datafile './ibdata1'
mysql_1 | 2016-01-11T10:22:03.956535Z 0 [ERROR] InnoDB: Could not open or create the system tablespace. If you tried to add new data files to the system tablespace, and it failed here, you should now edit innodb_data_file_path in my.cnf back to what it was, and remove the new ibdata files InnoDB created in this failed attempt. InnoDB only wrote those files full of zeros, but did not yet use them in any way. But be careful: do not remove old data files which contain your precious data!
mysql_1 | 2016-01-11T10:22:03.956604Z 0 [ERROR] InnoDB: InnoDB Database creation was aborted with error Cannot open a file. You may need to delete the ibdata1 file before trying to start up again.
mysql_1 | 2016-01-11T10:22:04.560316Z 0 [ERROR] Plugin 'InnoDB' init function returned error.
mysql_1 | 2016-01-11T10:22:04.560517Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
mysql_1 | 2016-01-11T10:22:04.561406Z 0 [ERROR] Failed to initialize plugins.
mysql_1 | 2016-01-11T10:22:04.561800Z 0 [ERROR] Aborting
mysql_1 |
mysql_1 | Initializing database
mysql_1 | 2016-01-11T10:28:42.591518Z 0 [Warning] Setting lower_case_table_names=2 because file system for /var/lib/mysql/ is case insensitive
mysql_1 | 2016-01-11T10:28:42.625407Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
mysql_1 | 2016-01-11T10:28:42.625559Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
mysql_1 | 2016-01-11T10:28:42.626271Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
mysql_1 | 2016-01-11T10:28:42.626857Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
mysql_1 | 2016-01-11T10:28:42.627839Z 0 [ERROR] InnoDB: Cannot open datafile './ibdata1'
mysql_1 | 2016-01-11T10:28:42.627859Z 0 [ERROR] InnoDB: Could not open or create the system tablespace. If you tried to add new data files to the system tablespace, and it failed here, you should now edit innodb_data_file_path in my.cnf back to what it was, and remove the new ibdata files InnoDB created in this failed attempt. InnoDB only wrote those files full of zeros, but did not yet use them in any way. But be careful: do not remove old data files which contain your precious data!
mysql_1 | 2016-01-11T10:28:42.627865Z 0 [ERROR] InnoDB: InnoDB Database creation was aborted with error Cannot open a file. You may need to delete the ibdata1 file before trying to start up again.
mysql_1 | 2016-01-11T10:28:43.230872Z 0 [ERROR] Plugin 'InnoDB' init function returned error.
mysql_1 | 2016-01-11T10:28:43.230906Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
mysql_1 | 2016-01-11T10:28:43.230912Z 0 [ERROR] Failed to initialize plugins.
mysql_1 | 2016-01-11T10:28:43.230915Z 0 [ERROR] Aborting
mysql_1 |
_mysql_1 exited with code 1
Gracefully stopping... (press Ctrl+C again to force)

```

このようにエラーします。


dockerコマンドで起動できることを確認します。

```
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest
$ docker rm some-mysql
some-mysql
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest
a713fbc350d89f2c626a792779d81a6503a948a612f8f27d65e6fbdd5d6bd619
$ docker logs -f a713fbc350d89f2c626a792779d81a6503a948a612f8f27d65e6fbdd5d6bd619
Initializing database
2016-01-11T10:32:23.249806Z 0 [Warning] InnoDB: New log files created, LSN=45790
2016-01-11T10:32:23.312733Z 0 [Warning] InnoDB: Creating foreign key constraint system tables.
2016-01-11T10:32:23.370788Z 0 [Warning] No existing UUID has been found, so we assume that this is the first time that this server has been started. Generating a new UUID: 99e768fd-b84e-11e5-888b-0242ac110005.
2016-01-11T10:32:23.372652Z 0 [Warning] Gtid table is not ready to be used. Table 'mysql.gtid_executed' cannot be opened.
2016-01-11T10:32:23.373255Z 1 [Warning] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
2016-01-11T10:32:23.953315Z 1 [Warning] 'user' entry 'root@localhost' ignored in --skip-name-resolve mode.
2016-01-11T10:32:23.953758Z 1 [Warning] 'user' entry 'mysql.sys@localhost' ignored in --skip-name-resolve mode.
~~~省略~~~
```

起動はできているようです。

```
$ docker ps
CONTAINER ID        IMAGE                         COMMAND                  CREATED              STATUS              PORTS                           NAMES
a713fbc350d8        mysql:latest                  "/entrypoint.sh mysql"   About a minute ago   Up About a minute   3306/tcp                        some-mysql
```

コンテナは正しく走っています。dockerコマンドだと正しく実行できるのにdocker-componseだとうまくいきません。volumeの設定を外してみます。

docker-compose.yml

```
$ docker-compose up mysql
Attaching to mysql_1
mysql_1 | Initializing database
mysql_1 | 2016-01-11T10:36:07.474015Z 0 [Warning] Setting lower_case_table_names=2 because file system for /var/lib/mysql/ is case insensitive
mysql_1 | 2016-01-11T10:36:07.512042Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
mysql_1 | 2016-01-11T10:36:07.512206Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
mysql_1 | 2016-01-11T10:36:07.513219Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
mysql_1 | 2016-01-11T10:36:07.514073Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
mysql_1 | 2016-01-11T10:36:07.514914Z 0 [ERROR] InnoDB: Cannot open datafile './ibdata1'
mysql_1 | 2016-01-11T10:36:07.514929Z 0 [ERROR] InnoDB: Could not open or create the system tablespace. If you tried to add new data files to the system tablespace, and it failed here, you should now edit innodb_data_file_path in my.cnf back to what it was, and remove the new ibdata files InnoDB created in this failed attempt. InnoDB only wrote those files full of zeros, but did not yet use them in any way. But be careful: do not remove old data files which contain your precious data!
mysql_1 | 2016-01-11T10:36:07.514937Z 0 [ERROR] InnoDB: InnoDB Database creation was aborted with error Cannot open a file. You may need to delete the ibdata1 file before trying to start up again.
mysql_1 | 2016-01-11T10:36:08.118575Z 0 [ERROR] Plugin 'InnoDB' init function returned error.
mysql_1 | 2016-01-11T10:36:08.118781Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
mysql_1 | 2016-01-11T10:36:08.120180Z 0 [ERROR] Failed to initialize plugins.
mysql_1 | 2016-01-11T10:36:08.121030Z 0 [ERROR] Aborting
mysql_1 |
mysql_1 exited with code 1
Gracefully stopping... (press Ctrl+C again to force)
$
```

うまくいきません。ログをみると `./ibdata1` というファイルが開けないようです。

```
mysql_1 | 2016-01-11T10:36:07.514914Z 0 [ERROR] InnoDB: Cannot open datafile './ibdata1'
```

ググってみると同じような報告が幾つかありました。

https://github.com/docker/kitematic/issues/209
http://stackoverflow.com/questions/30511475/mysql-in-docker-container-cant-run-through-a-mounted-volume-on-os-x

data only containerを使うような記述があるのでデータボリュームコンテナを使うようにしてみます。

data_mysql/Dockerfile

```
FROM busybox

# Create data directory
RUN mkdir -p /data /var/lib/mysql
RUN chmod -R 777 /data /var/lib/mysql
RUN chown -R root:root /data /var/lib/mysql

VOLUME /data
VOLUME /var/lib/mysql
CMD ["tail" , "-f" , "/dev/null"]
```

docker-compose.yml

```
data_mysql:
  build: data_mysql
  volumes:
    - volumes/mysql:/var/lib/mysql
    - volumes/data:/data
```

この状態でbuildしてコンテナを実行しておきます。

mysql用のdocker-compose.ymlの設定を修正します。

```
mysql:
  image: mysql:latest
  volumes_from:
    - data_mysql
  environment:
    MYSQL_ROOT_PASSWORD: toor

```

ただこれでも現象は変わりませんでした。試しにdockerコマンドにvolumes-fromを指定して実行してみたら同じ状態になりました。

```
$ docker run --volumes-from data_mysql_1 --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:latest
Initializing database
2016-01-11T11:01:43.008564Z 0 [Warning] Setting lower_case_table_names=2 because file system for /var/lib/mysql/ is case insensitive
2016-01-11T11:01:43.037966Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
2016-01-11T11:01:43.038633Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
2016-01-11T11:01:43.039302Z 0 [ERROR] InnoDB: Operating system error number 13 in a file operation.
2016-01-11T11:01:43.040111Z 0 [ERROR] InnoDB: The error means mysqld does not have the access rights to the directory.
2016-01-11T11:01:43.040496Z 0 [ERROR] InnoDB: Cannot open datafile './ibdata1'
2016-01-11T11:01:43.040517Z 0 [ERROR] InnoDB: Could not open or create the system tablespace. If you tried to add new data files to the system tablespace, and it failed here, you should now edit innodb_data_file_path in my.cnf back to what it was, and remove the new ibdata files InnoDB created in this failed attempt. InnoDB only wrote those files full of zeros, but did not yet use them in any way. But be careful: do not remove old data files which contain your precious data!
2016-01-11T11:01:43.040523Z 0 [ERROR] InnoDB: InnoDB Database creation was aborted with error Cannot open a file. You may need to delete the ibdata1 file before trying to start up again.
2016-01-11T11:01:43.643176Z 0 [ERROR] Plugin 'InnoDB' init function returned error.
2016-01-11T11:01:43.644225Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
2016-01-11T11:01:43.645311Z 0 [ERROR] Failed to initialize plugins.
2016-01-11T11:01:43.646316Z 0 [ERROR] Aborting

$
```


inspectはこのような状態です。

```
$ docker inspect dockerexample_data_mysql
[
{
    "Id": "b2f6538299b9a182f85a47c95deaac1743913f857e3df51418cdea643aa3a787",
    "RepoTags": [
        "dockerexample_data_mysql:latest"
    ],
    "RepoDigests": [],
    "Parent": "c2bdc5db36e75bc637bd8b7561ba3c448a9e0d279cd16d52588f923ffce6c4d8",
    "Comment": "",
    "Created": "2016-01-11T11:10:17.438600922Z",
    "Container": "b9dada046cd21875c56deff948201d1dc4c5f277c615182d7ba30b00d50aff37",
    "ContainerConfig": {
        "Hostname": "ea7fe68f39fd",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": [
            "/bin/sh",
            "-c",
            "#(nop) CMD [\"tail\" \"-f\" \"/dev/null\"]"
        ],
        "Image": "c2bdc5db36e75bc637bd8b7561ba3c448a9e0d279cd16d52588f923ffce6c4d8",
        "Volumes": {
            "/data": {},
            "/var/lib/mysql": {}
        },
        "WorkingDir": "",
        "Entrypoint": null,
        "OnBuild": [],
        "Labels": {}
    },
    "DockerVersion": "1.9.1",
    "Author": "TakesxiSximada \u003csximada@gmail.com\u003e",
    "Config": {
        "Hostname": "ea7fe68f39fd",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": [
            "tail",
            "-f",
            "/dev/null"
        ],
        "Image": "c2bdc5db36e75bc637bd8b7561ba3c448a9e0d279cd16d52588f923ffce6c4d8",
        "Volumes": {
            "/data": {},
            "/var/lib/mysql": {}
        },
        "WorkingDir": "",
        "Entrypoint": null,
        "OnBuild": [],
        "Labels": {}
    },
    "Architecture": "amd64",
    "Os": "linux",
    "Size": 0,
    "VirtualSize": 1113436,
    "GraphDriver": {
        "Name": "aufs",
        "Data": null
    }
}
]

```

どうやらmysql:latestのOSとデータボリューム用のOSが違うために発生している問題のようです。

http://qiita.com/masakielastic/items/9fdc52b47cc7e3850b9f#%E3%83%87%E3%83%BC%E3%82%BF%E3%83%9C%E3%83%AA%E3%83%A5%E3%83%BC%E3%83%A0%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%81%AE%E9%81%B8%E6%8A%9E%E8%82%A2
http://container42.com/2014/11/18/data-only-container-madness/


こちらの記事では平気でbusyboxを使っているようなので、boot2dockerの問題の可能性
http://qiita.com/baster/items/32a66766cbfd28e63a6b

UIDとGIDに不整合が起きていてそのためにファイルがひらけてないようです。
