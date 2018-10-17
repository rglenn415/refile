"""I created this because I wanted my own simple platform
to compile and run .ipynb files as .py files

I created this not to just compile ipynb files, but
to give me a platform to start adding features to .ipynb files

Hopefully in the future this compiler will be able to take out
html code from real python code in Jupyter and other cool features

Input:
    One .ipynb file

Functionality:
    Parses .ipynb file into .py format then compiles and run contents

Output:
    Decided by .ipynb file ran

"""
import json


def main():
    # Ensures that users can only perform this action on .ipynb files
    if '.ipynb' not in sys.argv[1]:
        raise Exception('Can only compile .ipynb files')

    # Ensures that users know that only 1 .ipynb file can be
    # compiled at a time
    if len(sys.argv) > 2:
        raise Exception('Can only run one .ipynb file at a time')

    # Takes the 1 file that users inputed
    # sys.argv[0] is the name of the file that is running the code
    ipynb = sys.argv[1]

    # Create string that will be put into complier
    # This will be one big string
    # Following this
    # https://www.programiz.com/python-programming/methods/built-in/compile
    mega_string = ''

    with open(ipynb, 'r') as ipynb:
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
                mega_string += line+'\n'

            # Adds a new line char at the end of each cell to replicate
            # that natural division from cells
            mega_string += '\n'

    # Takes mega_string and compiles
    # Syntax errors will be detected here
    codeObejct = compile(mega_string, 'sumstring', 'exec')
    # Runs the code
    # Runtime errors will be detected here
    exec(codeObejct)


if __name__ == '__main__':
    main()
