## console-pomodoro
The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for 'tomato', after the tomato-shaped kitchen timer Cirillo used as a university student. _(Source: Wikipedia)_

### Usage
The script provides a minimal console line interface. So just start the it in the usual way:
```
$ python3 main.py --help
usage: main.py [-h] -c

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. -Wikipedia

optional arguments:
  -h, --help     show this help message and exit
  -c , --cycle   set the number of doing/pause cycles
```

Otherwise you can use the Docker image:
```
$ docker build -t pomodoro .

$ docker run pomodoro:latest --help
usage: main.py [-h] [-c]

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. -Wikipedia

options:
  -h, --help      show this help message and exit
  -c , --cycles   set the number of doing/pause cycles
```