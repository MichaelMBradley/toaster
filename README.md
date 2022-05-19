# toaster

Helping automate reminder notifications.
Windows only, as there's probably already a better way to do it on Linux.

Add a function to the `Toast` class in `toaster.py`, and it will immediately be callable from the command line.
`toaster.vbs` passes any arguments given to it to the `toaster.py`, but runs it without creating a terminal window.

Next update: a script that automatically generates a `.xml` file that can be imported into Task Scheduler to call the script periodically.

## Setup

Inside the `toaster` folder:

```powershell
py -m venv .venv
.venv/Scripts/Activate.ps1
py -m pip install -r requirements.txt
echo "Any oher Python stuff you want to do, like running a script"
echo "Maybe try:"
echo "py toaster.py -t eye_saver"
deactivate
```

### Explanation

For those unfamiliar with Python virtual environments, this:

```
Creates a virtual environment
Activates the virtual environment
Installs the packages required for the script to run

(Up to you)

Deactivates the virtual environment
```

If you are interested in doing some project in Python and aren't yet familiar with virtual environments, I'd recommend looking into them.
While they're by no means necessary, they help to keep things neat.

If you have issues with access privileges and `Activate.ps1` refuses to run, just replace any reference to `py` afterwards with `.venv/Scripts/python.exe`.
It's also possible that `py` doesn't call Python on your system. In this case, you may need to replace any reference to `py` with `python` or `python3`.
