open-source energy system modeling - 1st assignment
________________________________________________________________________________________________________________________

Mario Ernst

________________________________________________________________________________________________________________________

Homework assignment  
• Start a new GitHub repository, add a license and a code-quality linter (e.g., ruff)  
• Add functions or small features from any real-life project relevant to your work or interests  
• The codebase should include 2-4 functions, 20-40 lines of code including documentation  
• The repository should work as “stand-alone” project  
(i.e., no need for other parts of your project/work that are not part of this repository)  
• If you need any dependencies/packages, add a simple list in a file requirements.txt  
• Add at least one test per function and make sure that these are executed on CI  
• If data is necessary to understand the scope of the functions, add a stylized dataset  
• The README should explain the scope of the project and the purpose of the functions  
• Invite me as a collaborator to your repository when the project is ready to be reviewed/graded  
Programming languages: Python (preferred), R, Julia  
Invitation to collaborate due by Monday, April 7, 23:59 (please do not push any commits after)  

------------------------------------------------------------------------------------------------------------------------

repository with functions for data preprocessing for time-series forecasting tasks:
  - scale_min_max()         # function to scale data between 0 and 1: x_ = (x - x_min) / (x_max - x_min)  
  - invert_scale_min_max()  # function to invert scale transformation between 0 and 1 to get the original data
  - check_return_datatype() # function to check and return the input datatype in scale and invert scale function

Functions are defined in preprocessing.py. A test scenario is prepared in the main section of preprocessing.py to show
functionality of the functions. Unit tests for all functions for different input data types (list, pd, np)
are prepared in test_preprocessing.py by using the unittest library. For check_return_datatype() the unit test also 
tests if TypeError is raised if e.g. a tupel is used as input

ruff package is used for code-quality linter. Linter check is possible by typing "ruff check" in command line
ruff is also included in .github .workflows as ruff_lint.yml

Scripts can be started in Terminal by "python .\preprocessing.py" or "python .\test_preprocessing.py" when current
working directory is the OSESM_assignment_1 repository.

