import json
import sys
import os


class file():
    """Created this class to store the .ipynb and .py file names

    At one point recently I wanted to completely remove this class
    and switch to some simpler version of reducing the word to just
    the prefix and use a set to play with them, but than I said
    to my self if it ain't broke, don't fix it

    """
    def __init__(self, ipynb, py):
        self.ipynb = ipynb
        self.py = py


def retrieve_arguments():
    """Some Dense ranting comment here to make the docstring a style I enjoy.

    I really just made this function to
    remove a big chunk of code from the main.

    So here I went through a realization why
    ('.ipynb','.py') was better than ('ipynb','py') <- which I had earlier
    My initial thoughts were to minimize the characters I was touching, but
    I realized that by not checking for the dot these characters could be
    found in the file [Which would not be that weird for an .ipynb file]
    So by that now the replace will hopefully only work on file extensions

    Functionality:
        Takes files user inputs on command line and creates
        file instances with the ipynb and py file extensions.

    Ouput:
        list of file class instances

    """
    # Takes all files that user inputs on command line
    # sys.argv[0] is the file name so we want to exclude that
    arg_files = sys.argv[1:]

    files = []
    for ipynb in arg_files:
        # Raise error if file is not .ipynb extenstion
        if 'ipynb' not in ipynb:
            raise Exception(f'{ipynb} is not an IPython Notebook (.ipynb)')

        # Sets the file extension to .py
        py = ipynb.replace('.ipynb', '.py')

        new_file = file(ipynb, py)
        files.append(new_file)

    return files


def main():
    """I really like how IPython Notebooks don't really have main functions

    For the user_input line the line was originally too long
    I went through many iterations to change the variable name, but
    was always disliking the name I picked because it didn't have that
    inherent readability I like

    I then thought to change the statement to be shorter and more concise

    Should the user_input prompt be CAPTILIZED OR uncapitalized?

    For now I will keep it CAPTILIZED until someone tells me not to
    I think it gives a small burst of fear
    I created this functionality after I had previously deleted
    my first version of the code

    My original refile.py ended up overwritten because I put
    refile.ipynb as a parameter to test multiple files being
    passed in through the command line

    This caused my file to become my old garbage test version
    I had passed my final functionality test and deleted all my work

    I instantly rewrote it, but I had spent a lot of time on
    real time comments

    Input:
        .ipynb files from the command line

    Functionality:
        Converts .ipynb files to .py files

    Output:
        n .py files in current directory
    (-> where n = # of ipynb from command line <-)
    """
    # files will contain file instances that contain .ipynb and .py file names
    # for every .ipynb file inputed from the command line
    files = retrieve_arguments()

    for file in files:
        # User has to decide if they want to overwrite the file
        if os.path.isfile(file.py):
            # Will not allow you to perform this action
            # on a file with the same name as this python file
            # sys.argv[0] is the current file name
            if file.py == sys.argv[0]:
                print(f'You cannot rewrite {sys.argv[0]}!!!')
                print('Ryan already had to rewrite the whole thing once')
                continue

            # Confirms with the user that they are want to overwrite
            # The existing file
            user_input = input(f'OVERWRITE {file.py}?\nProceed ([y]/n)? ')
            if user_input == 'y':
                continue
        # Opens the .ipynb file
        # Creates (or overwrites if the user has given consent) the .py file
        with open(file.py, 'w'), open(file.ipynb, 'r') as py, ipynb:
            # Creates a json object from .ipynb file
            ipynb_json = json.load(ipynb)

            for cell in ipynb_json['cells']:
                # Only writes contents from code cells
                if cell['cell_type'] != 'code':
                    continue
                for line in cell['source']:
                    # Replaces new line chars because not every line has one
                    # By removing new line chars and appending at the end
                    # we create consistent styling in the new file
                    line = line.replace('\n', '')
                    py.write(line)
                    py.write('\n')
                # Adds a new line char at the end of each cell to replicate
                # that natural division from cells
                py.write('\n')


if __name__ == '__main__':
    main()
