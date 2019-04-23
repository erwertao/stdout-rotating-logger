# stdout-rotating-logger
python3 stdout rotating logger , save target application output in memory. 

we often use nohup to start a service running in the background, but the output log maybe too large after some time.
and if we disable the output, when the service crashed, no log file can be analysis.

With this script, you can run your target like this:
nohup target | python3 looger.py &

Then you can use:
nc 127.0.0.1 [PORT]
to check the output of target


But if in linux system, the redirect stdout will change from Line buffered to full buffered.
So even if the line has been printed, it won't flush in full buffer mode.
You can use :
   stdbuf -oL target
to run the target with line buffer stdout mode.
stdbuf may not work if your target is python3,you can use:
    python3 -u target.py
to enable line buffer mode.
