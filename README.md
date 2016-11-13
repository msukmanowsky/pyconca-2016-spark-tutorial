# From gigabytes to petabytes and beyond with PySpark

> Imagine writing a Python program that could just as easily process a few
gigabytes of data locally or hundreds of petabytes in a distributed cluster
without changing a single line of code? Too good to be true? It isn't, it's
PySpark! In this tutorial we'll learn how to write PySpark that perform basic
analysis and fancy machine learning and can run on your computer or thousands
of servers.

Mike Sukmanowsky ([@msukmanowsky](https://twitter.com/msukmanowsky))

Sunday November 13th, 11:50am - 1pm

# Slides

https://docs.google.com/presentation/d/1Dagrb3Xi7myOU14CjfBfG-q5DmxbQWdLyobfMmseFt8

# Getting Setup

We only have an hour for the tutorial, so to ensure that we don't waste any
time, please go through all the steps below before coming to the session.

If you have troubles installing any of the required software, reach out to Mike
at mike.sukmanowsky@gmail.com or on [twitter](https://twitter.com/msukmanowsky).

- Python (duh), 2 or 3 is fine
- Java >= 1.7
- Git (to clone this repository and get access to examples)
- [Apache Spark 2.0.1 (pre-built for Hadoop 2.7)](http://d3kbcqa49mib13.cloudfront.net/spark-2.0.1-bin-hadoop2.7.tgz)
- [Apache Zeppelin 0.6.2 (binary release)](http://www-us.apache.org/dist/zeppelin/zeppelin-0.6.2/zeppelin-0.6.2-bin-all.tgz)

## Spark

After unpacking Spark to a directory of your choice, try running the following
command:

**Mac/Linux**
```
> cd <path to spark>
> bin/pyspark
```
**Windows**
```
$ cd <path to spark>
$ bin\pyspark.cmd
```

You should see some output and then be dropped into a Python interpreter.

```
Python 2.7.11 (default, Jul 19 2016, 10:14:23)
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel).
16/11/05 21:03:50 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
16/11/05 21:04:00 WARN Utils: Your hostname, MacBook-Pro.local resolves to a loopback address: 127.0.0.1; using 192.168.0.17 instead (on interface en0)
16/11/05 21:04:00 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.0.1
      /_/

Using Python version 2.7.11 (default, Jul 19 2016 10:14:23)
SparkSession available as 'spark'.
>>>
```

Hit CTRL/CMD-D to exit the Python interpreter.

## Zeppelin

Unzip the Zeppelin tarball and create a file `conf/zeppelin-env.sh` with a
single line:

```
export SPARK_HOME="/path/to/spark/spark-2.0.1"
```

Next, confirm that Zeppelin works.

**Mac/Linux**
```
> cd <path to zeppelin>
> bin/zeppelin-daemon.sh start
```

(Use `bin/zeppelin-daemon.sh stop` to stop when done.)

**Windows**
```
$ cd <path to zeppelin>
$ bin\zeppelin.cmd
```

You'll see output similar to:
```
Log dir doesn't exist, create /Users/mikesukmanowsky/.opt/zeppelin-0.6.2-bin-all/logs
Pid dir doesn't exist, create /Users/mikesukmanowsky/.opt/zeppelin-0.6.2-bin-all/run
Zeppelin start                                             [  OK  ]
```

Try navigating to http://localhost:8080/ where you should see this:

![Zeppelin Screen](https://www.evernote.com/l/AAFlPH2qBzNLobKHEuvNgDt4hNLM7ZQb0ZIB/image.png)

## Download the dataset

We'll be analyzing the [February 2015 English Wikipedia Clickstream](https://datahub.io/dataset/wikipedia-clickstream/resource/be85cc68-d1e6-4134-804a-fd36b94dbb82)
dataset. The entire data set is 5.7GB so please download it before the tutorial
to save on precious WiFi bandwidth.

You can download the dataset from this page https://figshare.com/articles/Wikipedia_Clickstream/1305770.
Click on the red "Download all (5.74GB)" link.

## Clone this repo

```
git clone https://github.com/msukmanowsky/pyconca-2016-spark-tutorial.git
```

If you've already cloned, make sure you `git pull` for the latest.

## Import and open the Zeppelin Notebook

With Zeppelin running, head to http://localhost:8080/ and click on the
"Import note" link.

Click "Choose a JSON here", and select the
[zeppelin_notebook.json](zeppelin_notebook.json) file in this repo.

You should now see a "PyCon Canada 2016 - PySpark Tutorial" notebook on your
Zeppelin home screen.
