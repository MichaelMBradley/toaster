# toaster

Helping automate reminder notifications.
Currently Windows only as there's probably already a better way to do it on Linux.

Add a function to the `Toast` class in `toaster.py`, and it will immediately be callable from the command line.
`toaster.vbs` passes any arguments given to it to the `toaster.py`, but runs it without creating a terminal window.

Next update: a script that automatically generates a `.xml` file that can be imported into Task Scheduler to call the script periodically.
