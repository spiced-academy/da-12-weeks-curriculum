---
title: "Logging"
weight: 91
---

![temp gauge](/images/logbook.jpg)
{{< credits >}}
Photo by Clay Banks on Unsplash
{{< /credits >}}


### What is logging?

Logging is a detailed description of what is going on or what was happening

- They are vital when we want to debug or just know the state of things.
- on your computer you can access the logs using the commands below:

```shell
cd /var/log/
tail syslog
```

or if you're on mac:
```shell
cd /var/log/
tail system.log
```

As the result we can see that our computer is logging what is going on in the background in case it crashes and we need to fix it.

- Logs can be used to generate data that shows the behavior of a user or program
- Server logs can be used to decide on whether to scale up or down

What have we used for logging so far in python?

- print statements
- they let us know if something is working the way we expect it to.

```python
import logging
```

### Logging module

Python has a logging module that can do more than just print statements: https://docs.python.org/3/library/logging.html

```python
import logging
```

The logging module has many functions but  it is best to focus on the following:

- loggers: create log messages
- handlers: send logs to terminal, file, email
- formatters: format the messages to your specifications

When using the logging module it is best to initially use the basic configuration:

```python
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H-%M-%S',
                    filename='test.log', filemode='w' 
                )  
```

This is defined after your import statements. Let's dissect what is in the basicConfig:

-  level: this sets the root logger level to the specified [level](https://docs.python.org/3/library/logging.html?highlight=basicconfig#levels):

```python
# filters/level: priority of log messages
## DEBUG: detailed diagnostic output
## INFO: status monitoring, everything works as expected
## WARNING: no imediate action required but something unexpected happened (low diskspace)
## ERROR: some exception that we need to solve, software unable to perform function
```

- format: Use the specified format string for the handler. Defaults to attributes `levelname`, `name` and `message` separated by colons. This is like an old school f-string that formats the way the output of the log will look like
- datefmt: same but for the date
- filename: Specifies that a [`FileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler) will be created, using the specified filename, rather than a [`StreamHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler). This is where the log will be saved for later use. Without this the handler will send the log to the terminal and not save it anywhere
- filemode: If *filename* is specified, open the file in this [mode](https://docs.python.org/3/library/functions.html#filemodes). Defaults to `'a'`. Here is a table of the other options. 'w' and 'a' would be used the most for starters. 

| Character | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| `'r'`     | open for reading (default)                                   |
| `'w'`     | open for writing, truncating the file first                  |
| `'x'`     | open for exclusive creation, failing if the file already exists |
| `'a'`     | open for writing, appending to the end of file if it exists  |
| `'b'`     | binary mode                                                  |
| `'t'`     | text mode (default)                                          |
| `'+'`     | open for updating (reading and writing)                      |

Now you can do a simple example of logging:

```python
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)>
                    datefmt='%Y-%m-%d %H-%M-%S',
                   filename='test.log', filemode='w' #start with this line missing and the logs will be printed in the terminal, add the line and it will save the messages in test.log
                )  

logging.debug('this is my test log DEBUG')
logging.warning('this is my test log WARNING')
```

The output whether in the terminal in saved in `test.log` will look something like this:

```shell
2021-12-16 10-31-31 - root - DEBUG - this is my test log DEBUG
2021-12-16 10-31-31 - root - WARNING - this is my test log WARNING
```

We can see here that the messages start with the data format we set up then the handler (root by default), the level of the log and then the message we put in it. 

Keep in mind if we set the `level=logging.WARNING` that the debug message will not be saved. Setting this let's the user decided the level of detail they would like to see in the log. 

Depending on time and the group you can write a program with more logging or use a program that is already written and has `print` statements. Live coding can be done where the `basicConfig` is added to the program and the `print` statements are all changed to `logging` statements of various levels. 
<br>

{{% notice copyright "Malte Bonart, Samuel McGuire" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}