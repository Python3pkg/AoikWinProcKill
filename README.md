# AoikWinProcKill
Kill Windows processes by matching their full command line with regular expression.

Tested working with:
- Windows  
- Python: 2.7+, 3.2+

[Package on PyPI](https://pypi.python.org/pypi/AoikWinProcKill)

## Contents
- [How to install](#how-to-install)
  - [Install PyWin32](#install-pywin32)
  - [Install via pip](#install-via-pip)
  - [Install via download](#install-via-download)
- [How to use](#how-to-use)
  - [Find the command](#find-the-command)
  - [Run the command](#run-the-command)
- [How to read the funny source code](#how-to-read-the-funny-source-code)

## How to install

### Install PyWin32
AoikWinProcKill has dependency on **PyWin32**.

Download an installer from [here](http://sourceforge.net/projects/pywin32/files/pywin32/).

- Choose the latest build version  (e.g. Build 219 on 2014-05-04).

- Make sure the installer matches with your CPU and Python version,  
e.g. **amd64-py2.7** if you are using an **x64 CPU** and **Python 2.7**.

### Install via pip
Run
```
pip install AoikWinProcKill
```
or
```
pip install git+https://github.com/AoiKuiyuyou/AoikWinProcKill
```

### Install via download
Alternatively download this [single file](/src/aoikwinprockill/aoikwpk.py).

Note installing this way you do not get the executable file that pip creates for you.

## How to use
### Find the command
After the [installation](#how-to-install), a command named **aoikwpk** should be available on your console.

### Run the command
Show usage: 
```
aoikwpk -h
```
```
usage: aoikwpk [-h] [-f] [-i] [-t N] PROC_CMD_REGEX

positional arguments:
  PROC_CMD_REGEX

optional arguments:
  -h, --help      show this help message and exit
  -f              kill processes forcibly by adding /F option to taskkill
  -i              show info about matched processes but not kill
  -t N            ignore processes that have been created for less than N
                  seconds (3 by default).
```

Show processes matched with "notepad":
```
aoikwpk notepad -i
```

Kill processes matched with "notepad":
```
aoikwpk notepad
```

Kill forcibly processes matched with "notepad":
```
aoikwpk notepad -f
```

Ignore processes that have been created for less than 10 seconds:
```
aoikwpk notepad -t 10
```

## How to read the funny source code
For developers interested in reading the source code,  
Here is a flowchart ([.png](/doc/dev/main.png?raw=true), [.svg](/doc/dev/main.svg?raw=true), or [.graphml](/doc/dev/main.graphml?raw=true)) that has recorded key steps of the program.  
![Image](/doc/dev/main.png?raw=true)

The flowchart is produced using free graph editor [yEd](http://www.yworks.com/en/products_yed_download.html).

If you want to copy the text in the graph, it's recommended to download the [.svg](/doc/dev/main.svg?raw=true) file and open it locally in your browser. (For security reason, Github has disabled rendering of SVG images on the page.)

The meaning of the shapes in the flowchart should be straightforward.  
One thing worth mentioning is isosceles trapezium means sub-steps.

The most useful feature of the flowchart is, for each step in it,
there is a 7-character ID.  
This ID can be used to locate (by text searching) the code that implements a step.  
This mechanism has two merits:

1. It has provided **precise** (locating precision is line-level)
  and **fast** (text searching is fast) mapping from doc to code, which is
  very handy for non-trivial project.

  Without it you have to rely on developers' memory to recall the code locations (*Will you recall them after several months, precise and fast?*).

2. It has provided **precise** (unique ID) and **concise** (7-character long) names
  for each steps of a program, which is very handy for communicating between
  members of a development team.

  Without it describing some steps of a program between team members tends to be unclear.
