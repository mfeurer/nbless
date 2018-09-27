# You can import any or all of the functions from the nbless package.
# The above imports all 3 functions and is the same as the line below.
# You can also import each function individually
from nbless import nbuild
from nbless import nbexec
from nbless import nbless
from nbless import nbcode
from nbless import nbhtml
nbuild(["plot.py", "notes.txt"], input_path='input_files', output_path="notebooks/")
nbexec("notebooks/raw.ipynb", output_path="notebooks/")
nbcode("out.ipynb", input_path="notebooks/", output_path='output_files')
nbhtml("out.ipynb", input_path="notebooks/", output_path='output_files')
nbless(["index.md", "plot.py", "notes.txt"], input_path="input_files/", nbexec_path="notebooks/")
# Another alternative is to import the package and use it as a namespace.
import nbless

nbless.nbuild(["index.md", "plot.py", "notes.txt"], input_path="input_files/", output_path="notebooks/")
nbless.nbexec("out.ipynb", input_path="notebooks/", output_path="notebooks/")
nbless.nbcode("out.ipynb", input_path="notebooks/", output_path='output_files')
nbless.nbhtml("out.ipynb", input_path="notebooks/", output_path='output_files')
nbless.nbless(["index.md", "plot.py", "notes.txt"], input_path="input_files/", nbexec_path="notebooks/")
