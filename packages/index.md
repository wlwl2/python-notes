# Python Windows Setup

## Install Python
[Download](https://www.python.org/downloads/)

Important: install Python 2.7 to `C:\Python27` and Python 3.6 to `C:\Python36`
(change the version numbers when appropriate). This is because the default
install location for Python 3 is not set to `C:\`.

## Use Command Prompt and not PowerShell!
Always use the Command Prompt and not PowerShell!

## Virtual environments
I guess they work like Node.js packages. Rather than global pip packages for
Python, you can install packages in a local virtualenv/virtualenvwrapper
environment. Global generally means that you can access commands from
any folder on the terminal. Local means that packages are installed in a
particular folder. For Python this is something different compared to node.

## Install virtualenv and virtualenvwrapper
[virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

`pip install virtualenv`

[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

`pip install virtualenvwrapper-win`
Again- always use the Command Prompt and not PowerShell!

## Set up an environment container folder
1. Run: `workon`
2. A list of environments, empty, is printed.
3. Run: `mkvirtualenv foldername`
4. A new environment, temp is created and activated.
5. Run: `workon`
6. This time, the temp environment is included.

By default windows will make a folder in `C:\Users\User Name\Envs`
or you should make this the default folder for storing environments.

## Activating your environment
`\path\to\env\Scripts\activate`

In the cmd prompt you will see your environment name in brackets/parentheses.

## Deactivating your environment
`\path\to\env\Scripts\deactivate`

In the cmd prompt the environment name in brackets/parentheses will disappear.

## Listing installed pip packages from the internet.
`pip freeze` will output a list of installed packages and their versions.
It also allows you to write those packages to a file that can later be used
to set up a new environment.

## Naming modules
https://www.python.org/dev/peps/pep-0008/#package-and-module-names
Modules should have short, all-lowercase names. Underscores can be used in
the module name if it improves readability. Python packages should also
have short, all-lowercase names, although the use of
underscores is discouraged.

When an extension module written in C or C++ has an accompanying
Python module that provides a higher level (e.g. more object oriented)
interface, the C/C++ module has a leading underscore (e.g. _socket).
