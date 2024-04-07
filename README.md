open-source energy system modeling - 1st assignment
______________________________________________________________________________________________________________________

Mario Ernst

______________________________________________________________________________________________________________________

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

repository with functins for data preprocessing for time-series forecasting tasks:

- min_max_scale()	# function to scale between 0 and 1: x_ = (x - x_min) / (x_max - x_min)  
- normalize()		# normalization by subtracting mean and dividing by std to get a mean of 0 and a std of 1: x_ = (x - mean) / std  
- windows() 		# function to get nested lists for serving time-series models  