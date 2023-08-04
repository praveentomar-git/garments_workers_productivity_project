### garments_workers_productivity_project

### Software and account requirements.
Github Account
Heroku Account
VS Code IDE
Git cli

### To create virtual environment in the same folder 

```
conda create -p venv python==3.7 -y   
```

### To activate virtual environment
```
conda activate venv/
```

### To install the required libraries
```
pip install -r requirements.txt
```

### Git configuration
```
git config --global user.name "Praveen_Tomar"
```

```
git config --global user.email "ch.praveentomar@yahoo.in"
```
### To add all the files in git
```
git add .
```
### To check the status
```
git status
```
### It commits with message
```
git commit -m "commit message"
```
### To check the logs
```
git log
```
### To push the data on git
```
git push origin main
```
### To pull the data from git
```
git pull origin main
```

### To check remote url
```
git remote -v
```

### To set CI/CD pipeline in heroku we need 3 informations

HEROKU_EMAIL = ch.praveentomar@gmail.com
HEROKU_API_KEY = <>
HEROKU_APP_NAME = garmentsworkersproductivityapp


### BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

### To list docker image

docker images

### RUN docker image

docker run -p 5000:5000 -e PORT=5000 f89e99843ab3

### To check running containers in docker

docker ps

### To stop any docker container

docker stop <container_id>

### Install setpy.py file
```
python setup.py install
```


### Summary
```
The Garment Industry is one of the key examples of the industrial globalization of this modern era. It is a highly labour-intensive industry with lots of manual processes. Satisfying the huge global demand for garment products is mostly dependent on the production and delivery performance of the employees in the garment manufacturing companies. So, it is highly desirable among the decision makers in the garments industry to track, analyse and predict the productivity performance of the working teams in their factories. 
```

### Attributes Information
```
01	date			:	Date in MM-DD-YYYY
02	day			    :	Day of the Week
03	quarter			:	A portion of the month. A month is divided into four/five quarters
04	department		:	Associated department with the instance
05	team_no			:	Associated team number with the instance
06	no_of_workers		:	Number of workers in each team
07	no_of_style_change	:	Number of changes in the style of a particular product
08	targeted_productivity	:	Targeted productivity set by the Authority for each team for each day.
09	smv			         :	Standard Minute Value, it is the allocated time for a task
10	wip			         :	Work in progress. Includes the number of unfinished items for products
11	over_time		     :	Represents the amount of overtime by each team in minutes
12	incentive		     :	Represents the amount of financial incentive (in INR) that enables or motivates a particular course of action.
13	idle_time		     :	The amount of time when the production was interrupted due to several reasons
14	idle_men		     :	The number of workers who were idle due to production interruption
15	actual_productivity	 :	The actual % of productivity that was delivered by the workers. It ranges from 0-1.
```

### Analysis
```
●	It is a regression problem.

●	Various visualization techines used to see how the data is distributed and features are related to each other.

●	Missing values filled in wip feature using median.

●   Various feature engineering techniques such as outlier detection, encoding and scaling technique implemented.

●   Machine Learning Algorithms such as Logistic Regression, Ridge, Lasso, Decision Tree, Random Forest & XGBOOST used for training.

●   XGBOOST algorithm gives the best perfomance.

●   Dataset link : https://archive.ics.uci.edu/ml/datasets/Productivity+Prediction+of+Garment+Employees
```

### Heroku app link
```
https://garmentsworkersproductivityapp-3e5cc9ce814a.herokuapp.com/
```