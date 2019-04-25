# THE_TIME
## THE TIME BUT NOT LIKE THE ACTUAL TIME

### Setup project on new machine

1. Clone repo `git clone https://github.com/VandalSausage/THE_TIME.git`

2. Create virtual environment in repo dir `python3 -m venv THE_TIME` (see docs for reference https://docs.python.org/3/tutorial/venv.html)

3. Activate virtual environment (on windows) `THE_TIME\Scripts\activate.bat`

4. Install packages into virtual env from requirements.txt
`pip3 install -r requirements.txt`

### Use virtual environment

1. cd into `THE_TIME`

2. Activate virtual environment (on windows) `THE_TIME\Scripts\activate.bat`

### Keep code in your local repo up to date

1. from the `THE_TIME` dir, type `git pull`

### Update or change python packages 

1. Ensure virtual env is activated

2. Run `pip3 install <package>`

3. Update `requirements.txt` with `pip3 freeze > requirements.txt`

### Run tests

1. Run tests before committing code

2. Pytest test in file `test_pytests.py`. Run them by typing `pytest`

3. Behave natural language test steps and python step implementations in the `/feature` directory. Run them by typing `behave`

### Commit your changes 

1. To see changed files, type `git status`

2. To add file to a commit, type `git add <file>`

3. To commit file or files, type `git commit -m "<sensible commit message>"`

4. To sync new commit or commits, type `git push`
