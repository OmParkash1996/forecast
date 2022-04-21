# forecast

1. First clone the repository using "git clone https://github.com/OmParkash1996/forecast.git".
2. Install virtual environment and create virtual environment using "virtualenv -p python3.6 venv" and then activate the environment using "source venv/bin/activate".
3. Install the requirements using "pip install -r requirements.txt".
4. Create .env file
5. Create database
6. Write down all required credentials in the env file as described in sample_env file,
	i.   Write down the database credentials.
	ii.  Write down all the required credentials for emailing purpose
      	iii. Also write down the api_key for accessing the forecast
7. Run the command "python manage.py migrate" to migrate the models in the database.
8. After running the previous command, run "python manage.py runserver" in order to run the server.

9. Given below are the end_points,
     i.  user_registration/        (For user sign up)            (e.g http://127.0.0.1:8000/user_registration/)
     ii. user_authentication/      (For user sign in)            (e.g http://127.0.0.1:8000/user_authentication/)
     ii. get_forecast/             (Accessing the forecast)      (e.g http://127.0.0.1:8000/get_forecast/)
 
10. For sending emails daily at 9AM, we have to use cron job.
11. Given below are the steps to create cron job,
	i. Run command "which python" on the terminal (Environment must be activated)
	ii. Copy that path and run command "crontab -e" which will navigate to the editor.
	iii. Write * 09 * * * copied_path manage.py command. (e.g: * 09 * * * /venv/bin/python manage.py forecast_email).
	iv. This will register the cron job and send email at 9 am every day.
