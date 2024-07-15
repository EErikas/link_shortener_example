# link_shortener_example
This is an example link shortening application written in Django. This is an example project for students of SMK University of Applied Sciences who are Studying Object-Oriented Programming. 

## Functionality
The purpose of this web app is to shorten provided links, which can be later accessed by entering their code appended to the site URL (functionality similar to bit.ly and other services like this)

## Features

 - Shortens provided URL as mentioned above (at the current stage short URL code is generated randomly without user input, though admin can change the value via the admin page)
 - Stores saved shortened, and original URLs
 - Automatically determines its domain (therefore the site can be easily migrated to another domain and stored codes would remain unchanged e.g, if previous shortened link was  `example.com/abc123`, after changing domain to `example2.com`, the `abc123` code will still be valid, so `example2.com/abc123` will still work without the need to modify the DB)
 - Automatically creates default superuser if no user with such privileges exists


## URL Patterns

 - `/` - Displays link shortening form
 - `/<link_code>` - Redirects to the corresponding URL, if such URL does not exist, user is redirected back to the homepage
 - `/admin/admin` - Link to django admin page
 - `/show/urls` - Lists all corresponding shortened and original URLs

## Set Up
The project was created and tested using Python 3.12, but newer versions should work as well. Install requirements by calling `pip install -r requirements.txt`
**Note:** If you want to run this project in production environment, you should set *DEBUG* to *false* and add your domain to the *ALLOWED_HOSTS* list  
