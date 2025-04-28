---
title: "Setup"
weight: 10
---

![anaconda](/images/anaconda.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@timothycdykes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Timothy Dykes</a> on <a href="https://unsplash.com/s/photos/anaconda?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}} 

**Vs Code** will be the main entry point for development in the course. It is a text editor that has many extensions for some of the most useful Data Analytics tools. Along with VS Code the three other important tools that will be installed are:

- **Miniconda**: A package manager that brings an up to date version of python along with it, which helps us install lots of different python libraries through the command line. Also provides support for virtual environments
- **IPython**: a terminal based interactive python shell
- **Jupyter Notebook**: a web browser-based python environment (featured in week 2)

Because students come into the course with different types of computers, operating systems, and versions of python, using these 4 platforms is one way to create some standardization across the class.


## The Text Editor

VS Code is a text editor. With it you can open, edit and save plain text files.
*Coding* means first, writing specific instructions into a text file and second, feeding the text into an *interpreter* that executes the statements in the file and outputs the results.

 To write code in the *Python language* you create a text file with the file ending `.py`, e.g.

```bash
my_script.py
text-adventure.py
awesome_data_analysis.py
```

![text editor](/images/vs_code_text_editor.png)

## The Terminal

The terminal is a text-based interface for your operating system. You can create, edit or delete new files or folders, install new software or configure your system. Open a terminal by clicking on `Terminal` in the upper tool bar and then `New Terminal`.  You can use the terminal to 
execute the instructions in a python file. To do that you need to type in:

```bash
python my_script.py
```
![terminal](/images/vs_code_terminal.png)

## IPython

When executing a `.py` file in the terminal the code is executed top down. Another way to execute python code is in the `IPython` shell. This can be activated in the terminal by entering `IPython`. Afterwards python code can be executed and the results are imediately displayed. This is a perfect environment for learning and testing before putting the code into a `.py` script. 

![ipython](/images/ipython_terminal.png)


## Jupyter Notebooks

Notebooks are similar to **IPython** and the software is actually built on top of IPython. Notebooks allow you to write Python code, execute the instructions, inspect the results
and create documentation all in the same environment. Documentation or code is written
into individual *cells* that can be executed separately. 

![notebook](/images/j_notebook.png)


## Project Challenges

{{% notice challenge "Setup: VS Code" %}}

{{% button href="https://code.visualstudio.com/docs/setup/setup-overview" icon="fas fa-external-link-alt" %}}Download and Install VS Code Here{{% /button %}}

### For Mac users
1. Download Visual Studio Code for macOS.
2. Open the browser's download list and locate the downloaded app or archive.
3. If archive, extract the archive contents. Use double-click for some browsers or select the 'magnifying glass' icon with Safari.
4. **Do not open the App yet!** First drag Visual Studio Code.app to the Applications folder, making it available in the macOS Launchpad.
  ![vs_code_to_apps](/images/vs_code_to_apps_mac.gif) 

### For Windows users and Linux 
- Download and install VS Code for your OS

### Next steps
- Open the *VS Code*
- You should see an window similar to the one below

![vs welcome](/images/vs_welcome.png)

- Close VS Code

{{% /notice %}}


{{% notice challenge "Setup: python environment" %}}

{{% button href="https://docs.conda.io/en/latest/miniconda.html" icon="fas fa-external-link-alt" %}}Download and Install Miniconda Code Here{{% /button %}}

1. Download Miniconda for your OS using the graphic installer from the download button above.

2. For **Mac** and **Linux** users follow the installer instructions as given and then skip to step 5. 

3. For **Windows** users follow the instructions until the advanced options portion of the installation. It is important to explicitly add `conda` to the PATH environment variable. This can be done by click on the the appropriate box as seen the screenshots below:

![miniconda](/images/mini_conda_2.png)

A warning is given and can be ignored as this will ensure the usage of the command `conda` in the terminal. Finish the installation. 


4. For **Windows**: Open VS Code. Then in the tool bar at the top click on `Terminal` and open an `New Terminal`. In Windows the default terminal should be `CMD` or the `Command Prompt`. Once the terminal is open navigate the the downward pointing carrot on the right next to the `+` symbol. Click on it and select `Set Default Profile`.  

![terminal](/images/vs_code_terminal_1.png)

The Command Palette will open at the top of the window. There `Command Prompt` should be selected. 

![terminal](/images/vs_code_terminal_2.png)

5. In the terminal type `python --version` To see which python version is being used in the environment. 

![version](/images/python_version.png)

If the python command throws an error then try the extras in the following table or consult your instructor. 

{{% /notice %}}

{{% notice warning "Mac" %}}

Mac computers come with python pre-installed. However it is often a very old version such as 2.7. If the command `python --version` returns a version of python less than 3.0 then please try the following command instead:

```python
python3 --version
``` 

This will explicitly access the newly install version that came with miniconda. 

{{% /notice %}}

{{% notice warning "Windows" %}}

As seen in the screeshots above when Miniconda is correctly installed and the correct terminal has been set as the default then the command prompt will start with `(base)`.


If the base is not activated then execute the command `conda activate base` in the terminal.  If the `conda`command is not recognized then run `conda init`,  close, reopen the terminal and then run `conda activate base` again.

Once the base has been activate then try `python --version`
{{% /notice %}}


{{% notice challenge "Setup: IPython" %}}


- Open VS Code
- Open a *Terminal* window 
- Type in the command `pip install ipython`
- Type in the command `ipython`. After executing this command the termin will change and the result should be similar to the screenshot below:

![ipython](/images/ipython_start.png)

`pip` is a package manager from python. The `pip install` command is used to install various packages and will be revisited later in the course. 

{{% /notice %}}

<br>

{{% notice copyright "Samuel McGuire" %}}
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

{{% /notice %}}