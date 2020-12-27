# Target audience
> All those who want to easily get started, and become professional in Data Science (e.g., students, new grads, or those who want to switch to Data Science from other domain).

# Requirements:
> Participants must bring their own laptops.

# Objective
Help participants in the following topics:
- What are the essential tools used by professional Data Scientists.
- How to setup those tools.
- How to use those tools effectively.
- Some good coding habits.

# Agenda
- Part I, 2 hours:
    * setup essential tools (Visual Studio Code, Anaconda, Jupyter Notebook, Virtual Environment, Git, GitHub).
    * how to use Visual Studio Code and Jupyter effectively.
    * some good coding habits.
- Part II, 2 hours:
    * how to use git effectively.

# Steps

- Brief self-introduction via [LinkedIn](https://www.linkedin.com/in/kaitaoyang/).

- Check how many tools that participants already have.
    > Visual Studio Code, Anaconda, Jupyter Notebook, Virtual Environment, Git, GitHub
- Download and install tools:
    > how to check whether your latop is 32-bit or 64-bit? 

        Windows: Right click "Windows Start" -> Click "System" -> You will see "System Type".

        macOS: Click "About This Mac" -> Click "More Info" -> In the Contents pane, click "Software" -> you will see "64-bit Kernel and Extensions".

        Linux: Press "Windows key" -> Type in "info" -> Click on "details".
    * Visual Studio Code {[Windows](https://code.visualstudio.com/docs/setup/windows), [macOS](https://code.visualstudio.com/docs/setup/mac), [Linux](https://code.visualstudio.com/docs/setup/linux)}
    * [Anaconda](https://www.anaconda.com/products/individual)
    * [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    * You do not need to install `Jupyter Notebook` and `Virtual Environment`, they will come automatically with Anaconda.
    * You only need to register a [GitHub account](https://github.com/) (you do not need to install GitHub desktop).

- [Manage virtual environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
    * Create a virtual environment named `py38cpu`, with specified Python version.
    ```bash
    conda create -n py38cpu python=3.8 -y
    ```
    * Activate a virtual environment by name
    ```bash
    conda activate py38cpu
    ```
    * Delete a virtual environment by name.
    ```bash
    conda remove --name py38cpu --all
    ```
    * Show all availlable virtual environments.
    ```bash
    conda info --envs
    ```

- SSH keys.
    > SSH keys will be used to access a remote machine.
    * Check whether you already have SSH keys
    ```bash
    ls ~/.ssh/
    # Check whether you see the following files.
    id_rsa  id_rsa.pub  known_hosts
    ```
    * Generate SSH keys (private and public key pairs).
    ```bash
    ssh-keygen -t rsa # Aways press `enter`.
    ```
    * Print out the content of your public key
    ```bash
    cat ~/.ssh/*.pub
    ```


- Setup SSH keys on your GitHub account.
    * Click your icon on the right top conner.
    * Click `Settings`
    * Click [SSH and GPG keys](https://github.com/settings/keys)
    * Click `New SSH key`
    * Past your public key content to the `Key` field.
    * Give a meaningful `Title` to this key.


- How to effectively use `Visual Studio Code`.
    * black formatting
    > File -> Preferenes -> Settings -> Python -> Formatting: Provider, choose `black`.
    * line limit of 80 chars
    > File -> Preferenes -> Settings -> (to add rulers)
    ```bash
    "editor.rulers": [80, 120],
    "workbench.colorCustomizations": {"editorRuler.foreground": "#ff4081"}
    ```
    * type hints
    * docstring
    > File -> Preferenes -> Settings -> autoDocstring
    * test driven development
    * further practice
        + [Leetcode practice on Data Structures and Algoriths](https://github.com/labuladong/fucking-algorithm).
        + [System design](https://github.com/donnemartin/system-design-primer).

- How to effectively use `Jupyter Notebook`.
    * install [jupyter notebook extensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html).
        ```bash
        # pip install
        pip install jupyter_contrib_nbextensions 
        # Enable css files
        jupyter contrib nbextension install --user

        ```
    * scratch pad (Ctrl + B)
    * table of contents
    * black formatting
    * line limit of 80 chars
    * debug
    * profiling

- How to use `Git` effectively.
    * Go through [all commands](https://github.com/ykaitao/setting-up-a-professional-data-science-environment/blob/master/how-to-use/git.md).
    * Practice.

- Call on actions:
    * [Voluntary payment](https://docs.google.com/forms/d/e/1FAIpQLScRnLPYE7t_x9smBolZ9RWr6Sisu7C2ws9RCPDfALJ7VPTA2g/viewform?edit2=2_ABaOnucX593H6a9AdGJ1QBXMtIS3xIHsfOvYegn6LaArOQrTXjU0uVeX0YsrmlulCJv509eX03cSiRks).
    * Recommand this workshop to your friends (I will organize this workshop frequently in the future).




