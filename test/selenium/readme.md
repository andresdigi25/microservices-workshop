# UI Tests

## System Overview
This project was created to run tests using Selenium tool

# <a name="setup"></a>Setup Instructions

### How to run UI Tests Locally
1. Install Python 3.8 or higher
2. Install pyenv(https://github.com/pyenv/pyenv#installation)

3. In your terminal where you want to create a new virtual environment.

    `Run: pyenv virtualenv <name of venv>`
4. In your terminal activate your virtual environment

   `Run: pyenv activate <name of venv>`
5. In your terminal run the next commands:
   1. `export ENV_NAME=qa`
   2. `export BROWSER_NAME=chrome`
   3. `export LOAD_BALANCER_NAME=http://localhost:4444`
   4. `export EXECUTION_TYPE=local`
   5. `export USER_NAME=test`
   6. `export PASSWORD=test`
   7. `pip install -r requirements.txt`
   8. Run the next command in the console:

   `behave ui_test/behave/features/ui.feature`

6. If you want to run the scenario including Allure report, Run the next command in the console: `behave ui_test/behave/features/ui.feature -k --no-capture -f allure_behave.formatter:AllureFormatter -o TEST_REPORT/allure_out/ --format pretty`
7. Generate Allure report: `allure serve TEST_REPORT/allure_out/`

### How to run UI Tests Remotely with Docker
1. Install Docker to run tests remotely
2. In a cmd run executeSelenium.sh:
   
   `./infrastructure/executeSelenium.sh`
3. In a cmd check witch is the URl of our local selenium hub:

   Put `docker ps` in a cmd, find Selenium/hub image and copy URL. Use the port :4444.
   Example: `http://localhost:4444/ui/index.html#/`

4. Install pyenv(https://github.com/pyenv/pyenv#installation)
5. In your terminal, you need to change the following environment variable:
   1. `export EXECUTION_TYPE=remote`
6. You can now use the same behave command when running local.