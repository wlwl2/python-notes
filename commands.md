## virtualenvwrapper commands (Windows)

## Set up an environment container folder (Envs)
1. Run: `workon`
2. A list of environments, empty, is printed.
3. Run: `mkvirtualenv env`
4. A new environment, `env` is created and activated.
5. Run: `workon`
6. This time, the `env` environment is included.

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

## lssitepackages
Calling `lssitepackages` shows the content of the site-packages
directory of the currently-active virtualenv.
