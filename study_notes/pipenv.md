# How to Use pipenv
2018-10-11

**`pipenv` is officially recommended tool for creating virtual environment for Python.**

1. Install python.

2. VS Code will automatically set up pylint by running 'python -m pip install -U pylint --user', or manually run 'pip install pylint'. At this momment, when you run 'pip list',
* You should consider upgrading pip via the 'python -m pip install --upgrade pip' command.
Package           Version
----------------- -------
astroid           2.1.0
colorama          0.4.1
isort             4.3.4
lazy-object-proxy 1.3.1
mccabe            0.6.1
pip               18.1
pylint            2.2.2
setuptools        39.0.1
six               1.12.0
wrapt             1.11.0

3. Run command 'pip install pipenv' to install pipenv.

Package           Version
----------------- ---------
astroid           2.1.0
certifi           2018.11.29 (Newly added)
colorama          0.4.1
isort             4.3.4
lazy-object-proxy 1.3.1
mccabe            0.6.1
pip               18.1
pipenv            2018.11.26 (Newly added)
pylint            2.2.2
setuptools        39.0.1
six               1.12.0
virtualenv        16.2.0 (Newly added)
virtualenv-clone  0.5.0 (Newly added)
wrapt             1.11.0

* pipenv install pylint --dev (optional)

4. Go to the project directory, run 'pipenv install' then this will create a 'Pipfile' and a 'Pipfile.lock' for you. If you just run 'pipenv shell' at this momment, it will only create a 'Pipfile'.

* If you have a requirements.txt file available when running 'pipenv install', pipenv will automatically import the contents of this file and create a Pipfile for you.

5. create 'main.py' that includes

```
import requests

def main():
    res = requests.get('https://httpbin.org/ip')

    print('Your IP is {0}'.format(res.json()['origin']))

if __name__ == "__main__":
    main()
```

5. Now you can run python application by 'pipenv run main.py'. Another way to run is 'pipenv shell' to activate the project's viertualenv and run 'python main.py'. Note that if you run 'python main.py' outside of this virtualenv, it won't run because you don't really have requests module installed in your local environment.

6. Run 'pipenv --rm' to remove project virtualev outside of the virtual shell.

7. 'pipenv install package' to install pip package.

8. 'pipenv uninstall package' to uninstall pip package.

## Auto-generate requirements.txt
* pip freeze > requirements.txt