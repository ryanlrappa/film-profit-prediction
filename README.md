# **Predicting Film Profitability (v1)**

This portfolio project is a work in progress. Using a variety of publicly available data about thousands of feature films, the goal is to design a machine learning algorithm (model) that can predict, as accurately as possible:  

**(1)** whether a film's global box office revenue exceeded (or will exceed) its budget, and  

**(2)** by how much its global box office exceeded (or will exceed) its budget (approximation of profits).  

Some additional goals are:  

**(3)** for the model's inputs to be simple and few enough so that it could be used to predict the profitability of a film that has not been made yet (making some assumptions about the unmade film's cast, crew and release), and  

**(4)** for the model to be interpretable, so users can get a sense of what factors make a film profitable vs. unprofitable.  

---------------  
### **Files:**  

- csv_files: CSVs with data used in the various jupyter notebooks (except for the full raw data, which was too large to upload here)
- jupyter_notebooks:  
        - 1_API_exploration.ipynb -- Just exploring how TheMovieDB API works with the tmdbsimple API wrapper  
        - 2_data_collection.ipynb -- Drafts of funtions later run in python scripts on an EC2 w/ tmux to collect the full raw data from the API  
        - 3_draft_data_cleaning.ipynb -- Drafts of functions/workflow to clean the data and engineer new features  
        - 4_full_data_cleaning.ipynb -- Final functions/workflow used to clean and feature engineer the full data  
        - 5_EDA.ipynb -- Visualizations and other exploration of patterns/relationships in the data  
        - 6_modeling.ipynb -- Trying various models to see which can predict most effectively, including visualizations of confusion matrices and ROC curves, and parameter tuning for gradient boosting model (also has notes on my approach from a business perspective)  
- pickle_files: jupyter notebook (draft) and python file (final) scripts used on EC2 to run GridSearchCV on gradient boosting model, and pickled final model  
- presentation slides pdf: my initial slide deck presenting/summarizing the project -- please check this out!  

---------------  
### **Outline of workflow:**  

1. Collect data from The Movie Database's API  
        1.1. Spin up a separate AWS EC2 instance for each table I'd like to collect (film info, credits, releases)  
        1.2. Install necessary packages on each EC2 instance (Anaconda, pip, the API wrapper, aws-cli, tmux)  
        1.3. Write a python script that saves relevant data from the API to a csv on each EC2  
        1.4. Open a tmux session on each EC2 and run the respective python scripts  
        1.5. Come back to the tmux sessions a day or two later and save the csv files to AWS S3 storage for further use  

2. Clean the data and engineer features (e.g. to measure importance of cast and crew, release date)  
        2.1. ...  
        
3. Visualization and analysis  
        3.1. ...  

4. Save and deploy the model(s)  
        4.1 ...


---------------  
### **Possible extensions of the project:**  

Time allowing, I might try to improve results by incorprating/modeling more features, such as:  

- Film posters (perhaps there are certain kinds of posters that are more appealing than others)  
- Film scripts, descriptions, and/or keywords (experience suggests that premise, plot, character arcs, etc matter)  
- Data on marketing strategy such as budget, channels, number+locations of theaters film was released in  
- Additional revenue: video, streaming, merchandise, etc (within the first year or two after release)  
- Data on contemporaneous piracy  

I would also try to gather much more data, possibly via web scaping, because The Movie Database only has reliable budget and revenue data for a few thousand films. And I'd like to experiment more with deep learning approaches, e.g. neural nets.  

**Another thing to note:** if the film industry shifts away from theatrial releases in a major way, toward substantially more straight-to-streaming releases, subsequent iterations of this project must rely on more comprehensive revenue data – not just global box office – in order to approximate film profitability (if such data is available).