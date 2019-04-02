# **Predicting Film Profitability**

This portfolio project is a work in progress. Using a variety of publicly available data about tens of thousands of feature films, the goal is to design a machine learning algorithm (model) that can predict, as accurately as possible:  

**(1)** whether a film's global box office revenue exceeded (or will exceed) its budget, and  

**(2)** by how much its global box office exceeded (or will exceed) its budget (approximation of profits).  

Some additional goals are:  

**(3)** for the model's inputs to be simple and few enough so that it could be used to predict the profitability of a film that has not been made yet (making some assumptions about the unmade film's cast, crew and release), and  

**(4)** for the model to be interpretable, so users can get a sense of what factors make a film profitable vs. unprofitable.  

---------------  
### **Files:**  

- ...  

---------------  
### **Outline of workflow:**  

1. Collect data from The Movie Database's API  
        1.1. Spin up a separate AWS EC2 instance for each table I'd like to collect (film info, credits, releases)  
        1.2. Install necessary packages on each EC2 instance (Anaconda, pip, the API wrapper, aws-cli, tmux)  
        1.3. Create a python script that saves data from the API to a new csv on each EC2  
        1.4. Open a tmux session on each EC2 and run the respective python scripts  
        1.5. Come back to the tmux sessions a day or two later and save the csv files to AWS S3 storage for later use  

2. Clean the data and engineer features (e.g. to measure importance of cast and crew, release date)  
        2.1. ...  
        
3. Visualization and analysis  
        3.1. ...  

4. Saving and deploying the model  
        4.1 ...