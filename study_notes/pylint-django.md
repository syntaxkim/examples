### Using pylint-django in VS Code
2018-10-13

- To use pylint-django, ensure pylint-django is installed and on your path and then execute:
`pylint --load-plugins pylint_django [..other options..] <path_to_your_sources>`

- In visual studio code, it can also be applied by modifying its '.vscode/setting.json' file.
- Command line arguments can be used to load Pylint plugins, such as that for Django:
`"python.linting.pylintArgs": ["--load-plugins", "pylint_django"]`

- However, if you specify a value in pylintArgs or use a Pylint configuration file (see the next section),
- then pylintUseMinimalCheckers which is the default pylint rules is implicitly set to false.
- So, these rules should be manually applied through the following default arguments passed to Pylint
- to implicitly set pylintUseMinimalCheckers to true again.

`--disable=all --enable=F,E,unreachable,duplicate-key,unnecessary-semicolon,global-variable-not-assigned,unused-variable,binary-op-exception,bad-format-string,anomalous-backslash-in-string,bad-open-mode`

- So the ultimate line inside of 'settings.json' would be

`"python.linting.pylintArgs": ["--load-plugins", "pylint_django", "--disable=all", "--enable=F,E,unreachable,duplicate-key,unnecessary-semicolon,global-variable-not-assigned,unused-variable,binary-op-exception,bad-format-string,anomalous-backslash-in-string,bad-open-mode"]`