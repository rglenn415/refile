# Refile
Users can convert multiple .ipynb files to .py using the command line

## How Does it Work?
1. Takes all files from command line  
For all files from command line  
1. Opens existing file and scrapes python code from json in the ipynb file (ignores the rest)
2. Writes to new py file with the same name as original 

## Special Features?
* This application will not allow you to perform these actions on a ipynb file with the same name as the running py file
* If the py file already exist it will check with the user if they want to overwrite

## How to Run?
1. clone repository 

git clone https://github.com/rglenn415/refile.git

2. run file

Here are Some Examples of What You Can Do  
python refile.py *.ipynb

python refile.py run.ipynb

python refile.py app.ipynb helper.ipynb

