# Mjai Server for Tenhou

This program acts as an Mjai server and at the same time as a Tenhou client.

## Setup

Activate virtual environment. You need *Python 3.10*.

```
$ python3.10 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Usage

First run the following command to establish mjai server. If you run `main.py` with `-d` option, there are no wait time for any actions. There must be a waiting time when using it in PvP.

```
(venv) $ python main.py [-d]
```

Then open another terminal and run any mjai client. To play the game, set the ID of Tenhou in `name` field, and combine room number and game type with an underscore in `room` field. For example:

```json
{"type": "join", "name": "NoName", "room": "0_0"}
```

Enable room numbers:

|room number|meaning|
|:-|:-|
|0|default room|
|1000 - 7999|private room|

Enable game types:

|game type|meaning|
|:-|:-|
|0|test play|
|1|ippan tonpu ariari (PvP)|
|9|ippan tonan ariari (PvP)|

## Tests

### Confirm Communication with Tenhou Server

```
(venv) $ python sample.py
```

### Run Mjai Client

First run the following command:

```
(venv) $ python main.py -d
```

Then open another terminal and run the follwing command:

```
$ ./test.sh 1
```

Note: Install `mjai-manue` in advance.

## Not Implemented

- Timeout with mjai client.
- Restarting game.

## Requirements

- Python 3.10
- websockets 10.2

## References

- http://gimite.net/pukiwiki/index.php?Mjai%20%E9%BA%BB%E9%9B%80AI%E5%AF%BE%E6%88%A6%E3%82%B5%E3%83%BC%E3%83%90
- https://tenhou.net/
- https://websockets.readthedocs.io/en/stable/

## License

MIT License.
