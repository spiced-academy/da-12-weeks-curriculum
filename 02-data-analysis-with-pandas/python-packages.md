---
title: "Python Packages"
weight: 80
---

![python packages](/images/modules.svg)


{{% notice warmup "Which Python packages do you know already?" %}}

Write down as many Python packages as possible in 1 minute.

{{% /notice %}}

## Key Concepts

command  |  description
---|---|
module                                   | an importable python file (ends with `.py`)
package                                  |    a folder with Python modules
PyPI                                     | online package index that contains all installable packages
`pip install <packagename>`              | install new packages
`pip list`                             | list all packages currently installed
`import matplotlib.pyplot as plt`        |   set an alias for the module

## How to install packages

### Step 1: Open the terminal

Open your terminal in VS code.


You’ll then see the following screen with your user name:

```shell
(base) C:\Users\Kristian>
```

### Step 2: Install the Package

To install a Python package in Terminal, use the `pip install` command and the name of the package:

```shell
(base) C:\Users\Kristian> pip install pandas
```

### Step 3: Verify that the package was installed

Once the package is successfully installed, a status report will be printed out in the terminal:

```shell
Installing collected packages: pandas
Successfully installed pandas
```

{{% notice info "Removing packages" %}}

You can remove a package by typing in 

```bash
pip uninstall <package-name>
```

{{% /notice %}}

## Package Documentation

Many Python package also publish a detailed documentation. Look at the section 
*quickstart* or *getting started* for a quick introduction into a library

Here is any example from [https://pandas.pydata.org/docs/getting_started/](https://pandas.pydata.org/docs/getting_started/):

![pandas](/images/pandas_package.png)


## Exercises

### Install a Package

1. Open the terminal in VS Code
2. Install the [`imageio` **package**](https://pypi.org/project/imageio/)
3. Verify that `imageio` was installed by importing it in a Jupyter notebook


### Explore a Python Package

- Pick one Python package from [**here**](https://www.academis.eu/blog/tags/python_packages)
- Install the package (if necessary)
- Run the code examples
- Find out what the package does
- Present the package to the group


### List files in a directory

1. Open empty notebook
2. Import the built-in `os` package
3. Run the code below. What does the code snippet return?

   ```python
   import os
   os.listdir()
   ```
4. How could you use this function in this weeks project to read in and parse the datasets?


### Produce an animated gif image with the `imageio` library

This will become useful for next week!

1. Download the attached files into a new folder 
2. Use `os.listdir(directory)` to produce a list of file names
3. Loop over the paths and read in each image
   ```python
   img = imageio.imread('path/to/img.png')
   ```
4. Append each `img` to a list `images`
5. Save the sequence of images as a `gif` file:

   ```python
   imageio.mimsave('path/to/data/test.gif', images, fps=5)
   ```

{{% attachments title="Related files" /%}}

## Reading

{{% notice reading "Documentations" %}}

- [`imageio`](https://imageio.readthedocs.io/en/stable/)
- [`os`](https://docs.python.org/3/library/os.html)
- [`pandas`](https://pandas.pydata.org/docs/)

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire, Malte Bonart" %}}

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}
