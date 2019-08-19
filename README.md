# **Predicting Film Profitability with ML**
 
```
*“Nobody knows anything... Not one person in the entire motion picture field knows for a certainty what's going to work. Every time out it's a guess and, if you're lucky, an educated one.”*

    ― William Goldman, screenwriter of Butch Cassidy and the Sundance Kid*
```

Making successful movies may never be an exact science, but with publicly available film data and machine learning techniques, we can now start to make better educated guesses about what works and what doesn't. This project specifically looks at data provided by TheMovieDatabase API and other sources – with variables including actors, director, writer, budget, genre, and release date, among others – to discover robust correlates of profitable films and predict profitability with high accuracy and precision.

This project is a work in progress. The goal is to iterate upon models in order predict, as accurately and precisely as possible:  

**(1)** whether a film's global box office revenue exceeded (or will exceed) its budget, and  

**(2)** by how much its global box office exceeded (or will exceed) its budget (approximation of profits).  

Some additional goals are:  

**(3)** for the model's inputs to be simple and few enough so that it could be used to predict the profitability of a film that has not been made yet (making some assumptions about the unmade film's cast, crew and release), and  

**(4)** for the model to be interpretable, so users can get a sense of what factors make a film profitable vs. unprofitable.  

---------------  
### **Files:**  

- **data:** CSVs used in the jupyter notebooks (except for the raw data, which was too large to upload)
- **notebooks:**  
                - `1_API_exploration.ipynb`: exploring how TheMovieDB API works with the tmdbsimple API wrapper  
                - `2_data_collection.ipynb`: drafts of funtions later run in python scripts on an EC2 w/ tmux to collect full raw data  
                - `3_draft_data_cleaning.ipynb`: drafts of functions/workflow to clean the data and engineer new features  
                - `4_full_data_cleaning.ipynb`: final functions/workflow used to clean and feature engineer the full data  
                - `5_EDA.ipynb`: visualizations and other notes on patterns/relationships in the data  
                - `6_modeling.ipynb`: trying different models to see which predicts best, including visualizations of confusion matrices and ROC curves, and parameter tuning for gradient boosting model (also has notes on my approach from a business perspective)  
- **models:** jupyter notebook (draft) and python file (final) scripts that can be used on EC2 to run GridSearchCV on gradient boosting model, and pickled final model (.pkl file)  
- **presentation_vX.pdf:** slide deck presenting/summarizing the project -- check it out!  
- **src** (transition from notebooks to polished scripts in progress):  

```
├── src                <- Source code for use in this project.
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── collect_raw_data.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train, tune and use models to make predictions           
│   │   ├── train_model.py
│   │   └── predict_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       ├── confusion_matrix.py
│       └── visualize.py
```

---------------  
### **Outline of workflow (in progress):**  

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

Time allowing, I might try to improve results by collecting more data via web scraping or other sources, and considering more variables like:  

- Posters and trailers
- Scripts, plot descriptions, and/or keywords
- Marketing budget, channels, number and geography of theaters film was released in  
- Ancillary revenues: video, streaming, merchandise, etc.
- Piracy  
