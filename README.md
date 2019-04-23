# stdout-rotating-logger
python3 stdout rotating logger , save target application output in memory. 

we often use nohup to start a service running in the background, but the output log maybe too large after some time.
and if we disable the output, when the service crashed, no log file can be analysis.

With this script, you can run your target like this:
nohup target | python3 looger.py &

Then you can use:
nc 127.0.0.1 [PORT]
to check the output of target
