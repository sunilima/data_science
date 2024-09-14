# data_science
data science course 

# project1_dataviz
Streamlit web app for data visualization

# Steps

# 1 - Create a repository on github.com and create a branch and then clone the branch on local computer

# 1a - sign up and login to github.com
# 1b - click on "new repository" and we create a new repo with name as project1_dataviz, gitignore, readme and license file
# 1c - create a branch with "pranav"
# 1d - copy the branch url for cloning in vs code
# 1e - vs code click "new window", then "clone git repo", then select folde
r destination and clone
# 1f - open the folder

# 2 - Create virtual environment

# 2a - go to "terminal" , "new terminal", type in terminal  ->> python -m venv myenv
# 2b - if python not found error is coming then add system environment variables
# 2c - if python not found error is coming then Ctrl+shift+P then select Python create environment, then venv, then enter
# 2d - install python from python.org
# 2e - after venv is created then type in terminal myenv/Scripts/activate
       (or .venv/Scripts/activate)
# 2f - Only if problem in creating virtual environment - open "powershell" in admin mode and type 
  Set-ExecutionPolicy RemoteSigned
# 3 - go to branch\
# 3a - write in teminal ->> git checkout nilima
  (because my branch name is nilima on github)
# 3b - add to gitignore file the foldername of vurtual envvironment (.venv/).. (sir's env was myenv)

# 4 - install python libraries/packages
# 4a - type in terminal -> pip install streamlit,pipreqs
# or type in terminal below two lines (one after another) 
#       pip install streamlit
#       pip install pipreqs

# 5 - aim: to create a website on which user will upload a file dataset.csv
# further user will select a column
# if column type is numeric then display the histogram
# if column type is nominal then display the bar chart