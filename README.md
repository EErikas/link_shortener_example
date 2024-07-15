# link_shortener_example
This is an example link shortening application written in Django. This is an example project for students of SMK University of Applied Sciences who are Studying Object-Oriented Programming. 

## Functionality
The purpose of this web app is to shorten provided links, which can be later accessed by entering their code appended to the site URL (functionality similar to bit.ly and other services like this)

## Features

- Shortens provided URL as mentioned above (at the current stage short URL code is generated randomly without user input, though admin can change the value via the admin page)
- Stores saved shortened, and original URLs, as well as IP addresses and clicks for each shortened URL
- Automatically determines its domain (therefore the site can be easily migrated to another domain and stored codes would remain unchanged e.g, if previous shortened link was `example.com/UkLWZg9`, after changing domain to `example2.com`, the `UkLWZg9` code will still be valid, so `example2.com/UkLWZg9` will still work without the need to modify the DB)
- Automatically creates default superuser according to provided environment variables
- Uses [sqids](https://sqids.org/plpgsql) library for PostgreSQL which allows generating unique URL identifiers on the database side and read it back on the system.



## URL Patterns

- `/` - Displays link shortening form and paginated list of 
- `/<link_code>` - Redirects to the corresponding URL, if such URL does not exist, user is redirected back to the homepage
- `/admin/admin` - Link to django admin page

## Set Up
The easiest way to launch the project is by using `docker compose`. 
Before running the `compose.yml`, create `settings.env` and set the following values:
### Database values
These values are used by both Postgres Docker container in a setup process and later in the web app to connect to it:
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

### Django admin values
These values are used to create a Django admin user that is able to connect to the admin panel: 
- `DJANGO_SUPERUSER_USERNAME`
- `DJANGO_SUPERUSER_PASSWORD`
- `DJANGO_SUPERUSER_EMAIL`

### Environment settings
The following values help to define if the application should be running in development or production modes, they set different things, thus it is important to know what they mean:
- `MODE`: the values can be `dev` or `prod`. 
    - `dev` mode runs the application using django development server which is sufficient for debugging but should not be used in production
    - `prod` mode runs the application using `gunicorn` which is the preferred way of running production application
- `DEBUG`: determines weather or not detailed debugging messages should be displayed on the Web UI. Value of `1` enables them and `0` disables them. It is only recommended enable this setting during development. The default value is `0`.
- `ALLOWED_HOSTS`: determines from which hostnames the application should be accessible. If your app was running on `example.com` in production, this value should be set. Multiple hosts can be set by separating values using commas. In development mode this value can be set to `*`
- `SECRET_KEY`: This value is used cryptographic signing. You can read more about it here: https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY

### Optional values
- `DB_HOST`: The hostname of the database server. Default value is `db`
- `DB_PORT`: The port of the database server. Default value is `5432`

### Sample `settings.env` file
```
POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<database name>

DJANGO_SUPERUSER_USERNAME=<admin username>
DJANGO_SUPERUSER_PASSWORD=<admin password>
DJANGO_SUPERUSER_EMAIL=<admin email>

MODE=<can be 'dev' to launch django development server or 'prod' to launch gunicorn>
ALLOWED_HOSTS=<host name of where your site is hosted (e.g., 'example.com') or '*' to allow any host when in development mode>
SECRET_KEY=<randomm secret key value>
DEBUG=<'1' or '0' depending if you're running in development or production>
```
#### Development version
The sample above could be appended with the following values:
```
MODE=dev
ALLOWED_HOSTS=*
SECRET_KEY=<randomm secret key value>
DEBUG=1
```
#### Production version
The sample above could be appended with the following values:
```
MODE=prod
ALLOWED_HOSTS=example.com,test.example2.com
SECRET_KEY=<randomm secret key value>
```
