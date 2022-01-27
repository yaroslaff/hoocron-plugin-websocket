# hoocron-plugin-websocket
Websocket client plugin for Hoocron

## Install
~~~
pip3 install hoocron-plugin-websocket
~~~ 

## Usage
~~~
$ hoocron.py --ws TICK --wsroom myapps::u1 --wsurl http://localhost:8899/ --wssecret myapps-pass
...
started websocket thread, watch room 'myapps::u1' on http://localhost:8899/
Websocket connected to http://localhost:8899/

run TICK from websocket
Tick! (uptime: 6 seconds)
Result(TICK): ticked
~~~

## Server-side
### Redis
`SET ws-emit::secret::myapps myapps-pass`

### ws-emit
`ws-emit.py -a 0.0.0.0:8899 --cors '*' --secret 123`

### curl
`curl -d @/tmp/x.json -H "Content-Type: application/json" -X POST http://localhost:8899/emit`

/tmp/x.json:
~~~
{
	"event": "update",
	"room": "myapps::u1",
	"data": "TICK",
	"namespace": null,
	"secret": "123"
}
~~~

# See also
- [hoocron: cron with hooks](https://github.com/yaroslaff/hoocron) 
- [ws-emit: emit websocket messages from any source, even from CLI with curl](https://github.com/yaroslaff/ws-emit)

