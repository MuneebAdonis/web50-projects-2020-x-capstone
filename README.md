# CS50W Capstone Slide Image Database
## Introduction
My capstone project is a slide image database. It allows slide images to be stored, searched and downloaded. It was built to store histological images. Histological slide images are fairly large files (roughly 1GB), making it difficult to share easily via email or USB (long copy/ paste times). Typically they are labelled with a random number and that number corresponds to a hardcopy report filled in at the time of specimen collection. Manually searching and matching up slide and case numbers takes a lot of time. With this platform, when the image is scanned it is uploaded to a database, and the corresponding information is captured with it. 
### Distinctiveness and Complexity
I think this site is distinct as there are not many systems which allow for the storage and search of these histological images. It is a fairly niche field. I think the ability to comment is also a distinct feature, which will allow the site to gain information from its users rather than just display the limited information that was available at the time of upload.
The site has many complex features. The search feature is the main one. It allows to search either using just one field or by chaining many fields together. The system to tissue relationship also means that once a system is selected only the appropriate tissues are searchable.  This one-to-many relationship is displayed using JavaScript. This allows it to change during use without having to made additional calls to the server. The comments section also uses JavaScript to post comments to server; this allows the latest comments to pop up without the user having to refresh the page manually. 
## File Contents
### HTML, CSS, JS
+ layout.html
	+ This file contains the HTML structure for the entire project. It contains the nav-bar as well as links to the google fonts, CSS stylesheet and JS functions.
+ login.html
	+ This page is allows the user to sign in
+ index.html
	+ This page contains the search function. The most important part of the project.
+ image.html
	+ This page contains additional slide information as well as a link to download the slide for offline work and the comments section.
+ profile.html
	+ This page contains the user information. If it is the logged in user they may change user information or their password. If they have permission they may sign up a new user.
+ signup.html
	+ This page has the form a new user is required to submit in order to sign up to use the site.
+ styles.css
	+ This file contains all the CSS styling used in this app.
+ database.js
	+ This file contains all the JavaScript functions used in this app. These include;
	 	+ update_min –This function updates the minimum value of the max age when searching this prevents the max age being less than the min age.
		+ commentJS –This function allows the comments to be made in JS so the user doesn’t have to refresh the page to update the list of comments.
		+ get_system –This function filters tissues based on the system selected. This ensures once a system is chosen only the tissues available to that system can be selected.
		+ char_left –This function calculates the amount of characters left as the user is typing a comment.
		+ edit_profile –This function shows or hides the form required to edit a user’s profile information.
		+ change_password – This function shows or hides the form required to change a user’s password.
		+ checkpword –This function ensures that passwords match up when changing a password or when a new user is signing up.
### Python
+ models.py
	+ This file contains all the SQLite models used in this app. These include;
		+ Title –This model is simply a list of possible titles for Users to choose from.
		+ User –This model is Users.
		+ Stain –This is a list of possible stains for the Slide model.
		+ System –This is a possible list of systems for the Tissue model.
		+ Tissue –This is a list of tissues for the Slide model. There is a many-to-one relationship between the tissues and systems.
		+ Gender –This is a list of possible genders for the Slide model.
		+ Diagnosis –This is a list of possible diagnosis for the Slide model.
		+ Slide –This is model which is searched for with the search function on the index page. It references all the above mentioned models.
		+ Comment –This is the comment model. It contains comments linked to a specific slide. It also contains information such as date and commenter (which is a User).	
+ admin.py
	+ This file contains the models accessible from Django’s admin app.
+ urls.py
	+ This file contains the routing for each html page and the JavaScript APIs.
+ views.py
	+ This file contains all the back-end Python functions used in this app. These include;
		+ tissue_filter –This function is linked to the get_system JavaScript function. It filters the tissues according to the system selected.
		+ comment –This function is linked to the commentJS JavaScript function. It makes the comment, updates the model and sends the updated comments to the front-end.
		+ index –This function renders the index page. It also contains the search function, the most important part of this project.
		+ image_page –This function renders the image page based on the slide selected.
		+ profile_page –This function renders the profile page. It also allows users to change information and passwords.
		+ signup –This function renders the signup page. It also allows new users to be signed up.
		+ login_view –This function renders the login page. A user needs to login to use the site.
		+ logout_view –This function logs the user out. It then redirects to the login page. 
## How to Run
To run the program, runserver, login and search using as many or few search fields as you desire. If you do not have a user account, a user will have to set up an account for you. If this is not possible a superuser profile can also be created.
