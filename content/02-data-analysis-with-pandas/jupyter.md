---
title: "Jupyter Notebooks"
weight: 10
---

![notebook](/images/notebook.jpg)
{{< credits >}}
Photo by <a href="https://unsplash.com/@m15ky?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mike Tinnion</a> on <a href="https://unsplash.com/s/photos/notebook?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
{{< /credits >}}

{{% notice warmup "Running Python Code" %}}

Collect different ways of running python code. Also discuss advantages and disadvantages.

{{% /notice %}}

## Jupyter Notebook

Install the classic Jupyter Notebook. Open a Terminal window, type in the command:

```bash
pip install notebook
```

To run the notebook:
```bash
jupyter notebook
```

## Jupyter shortcuts

shortcut  |  description
---|---|
`Shift` + `ENTER` | execute cell
`TAB` | display available attributes
`Shift` + `TAB` | instant help
`Esc` | exit editing, enabling commands below
`a` | insert cell above
`b` | insert cell below
`dd` | delete cell
`c` | copy cell
`v` | paste cell
`m` | convert cell to Markdown
`y` | convert cell to Python code
`Ctrl` + `Shift` + `-` | split cells
`Shift` + `m` | merge cells


## IPython Magic Commands

Many commands influence the Jupyter/IPython session directly. They either interact with the Python interpreter or are executed as shell commands.

command  |  description
---|---|
`ls` | list files
`cd <dir>` | change directory
`pwd` | print working directory
`!<command>` | execute any shell command
`%hist` | shows all commands typed so far
`%pprint` | toggles pretty-printing on and off
`%reset` | restarts the current session


## Markdown

When you change a Jupyter cell to Markdown

```markdown
## This is a heading

You can format text in **bold** *italic*
and place [hyperlinks](https://www.spiced-academy.com).
```

This will render to 

![](./jupyter.files/md_heading_bsp.PNG)

You can even include math equations using the Latex notation:

```markdown
$\sum{\frac{a_i}{b^2}}$
```

This will render to 

$$
\sum{\frac{a_i}{b^2}}
$$.

## Exercises

### Task 1

Launch Jupyter Notebook from the command line

1. Open your terminal or the Anaconda prompt
2. Type in `jupyter notebook`
3. What happens if you close the terminal window?

### Task 2

- Open a new Jupyter notebook
- Change the first cell to Markdown by pressing `Esc` then `m`
- Put a headline into the first cell:

   ```markdown
   # Project Baby Names

   ```
- Press `Ctrl`+`ENTER` to render the cell (same as `Shift` + `ENTER`)
- Save the notebook and send it to a team member
- Open the notebook that a team member sent to you


## Project Challenges

{{% notice challenge "Setup your development environment" %}}

1. Launch VS Code and open your `working-folder`.
2. Create a `02_pandas` folder. Inside the `02_pandas` create the following folders:
   - `data`
   - `notebooks`
   - `weekly_project`
3. Download the data from https://www.ssa.gov/oact/babynames/limits.html.
   Take the *"National data"* dataset which is around **7MB large**.
4. Extract the `names.zip` file.
5. Move all files into a `data` folder inside the `02_pandas`
6. Create a new notebook and place it inside the `notebooks` folder.

{{% /notice %}}

## Reading

{{% notice reading "Reading" %}}

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Introduction to Jupyter Notebook](https://realpython.com/jupyter-notebook-introduction/)
- [Pros and Cons of Notebooks](https://betterprogramming.pub/pros-and-cons-for-jupyter-notebooks-as-your-editor-for-data-science-work-tip-pycharm-is-probably-40e88f7827cb)

{{% /notice %}}

<br>

{{% notice copyright "Malte Bonart, Spiced Academy" %}}
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
{{% /notice %}}