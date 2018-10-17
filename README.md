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
```bash
python refile.py *.ipynb
```
```bash
python refile.py run.ipynb
```
```bash
python refile.py app.ipynb helper.ipynb
```
# compile_ipynb
Functionality: Users can compile/run .ipynb like .py files

## How Does it Work?
1. Takes in file from command line
2. Reads file into string
3. Compile and run contents from .ipynb file as .py

## Special Features?
* Checks that user only inputs .ipynb files
* Checks that user only inputs one file

## How to Run?
### Input:
* One .ipynb file that containa code designed with a 
```python
def main():
``` 
* Must have 
```python
if __name__ == '__main__':
    main()
```
### Run with:
```bash
python compile_ipynb.py test.ipynb
```


