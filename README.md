# GO FIT

Go Fit is a student-made B2C e-commerce application which sells fitness products directly to end customers, but is also intended to give users a place to log their fitness journey and connect with other users that share the same interest in physical improvement. 

The application was deployed using Heroku and can be found here: [GO FIT](https://go-fit-493a972aae08.herokuapp.com/)

It is my final milestone project for the Code Institute Diploma in Full Stack Software Development. The site aims to present users with an attractive and intuitive online shopping experience and encourage return visits through features such as newsletter, social media posts, easy to use user profile function to save customer details, various fitness challenges presented on the web site and "Community" aspect of the site. 

Core part of site is a retail store where users can view, search and filter the products, then select items to add to their shopping cart and purchase through a secure single payment.

All users can view details of the products available for purchase, and can sign up to the company newsletter. In addition, registered users can access their profile where they can keep track of delivery details, order history and community posting history. Community section allows registered users to interact with other users via posts and comments, and incetivises occuring visitors to create an account to join or start various fitness topics. 

Admin users can manage products, challenges, posts and comments. This includes being able to add new products to the store, update product details, add new challenges, update existing ones, approve and edit community posts and comments.

Web marketing strategies I used the project are:
- Organic social - through facebook, instagram and x
- Email - via newsletter subscription managed with Mailchimp


## User Experience (UX)

### User stories

Project was developed following these goals:

As a user, I want to:
- View a list of products
- View a specific category of products
- View individual product details
- Sort the list of available products
- Sort a specific category of products
- Sort multiple categories of products simultaneously
- Search for a product by name or description
- Easily see what I've searched for and the number of results
- Easily see the size and quantity of a product when purchasing it
- View items in my bag to be purchased
- Adjust the quantity of individual items in my bag
- Easily enter my payment information
- Feel my personal and payment information is safe and secure
- View an order confirmation after check out
- Receive an email confirmation after checking out
- Register for an account
- Login/logout
- Receive an email confirmation after registering
- Have a personalized user profile
- View list of community posts
- Open a post
- View comments for Posts
- Manage my posts
- Manage my comments
- Find the site through the web search engines
- View a list of challenges
- Subscribe to newsletter

As a store owner, I want to:
- Add a product
- Edit/update a product
- Delete a product
- Add a challenge
- Edit/update a challenge
- Delete a challenge
- Moderate the Community section


## Technologies Used

This project uses the following languages:

- HTML
- CSS
- Javascript
- Python

The project uses the following technologies and frameworks:

- Bootstrap 4.6 was used for the key layout components
- jQuery was used to enable responsive behaviour on forms and other elements
- Django is the Python framework the backend code uses
- Heroku is the cloud-hosting service the app is hosted by
- PostgreSQL is the database used, provided by Heroku
- SQLite3 was used for data storage in development
- Amazon S3 is used for CSS and media storage
- Visual Studio Code was the IDE used for writing all code
- Stripe provides the technology for processing payments
- Font Awesome is the source of all icons

The following libraries/packages listed below are also used:

- boto3 ensures that the app works with Amazon S3
- dj-database-url allows the app to work with PostgreSQL
- django-allauth is used for all user authentication
- django-countries is for the country field in the profile form
- django-crispy-forms ensures that all Django forms are rendered with Bootstrap styling
- django-storages gives the functionality in a custom storage class needed to connect to S3
- gunicorn is the WSGI server that runs the Python app
- Pillow for image handling on forms
- psycopg2-binary is the PostgreSQL database adapter for Python

## Features

The structure and purpose of the GO FIT project is heavily based on the Code Institute Boutique Ado walkthrough example application.

GO FIT uses a B2C e-commerce model, selling directly to end customers with single online payments to cover purchases.

Current features for the user include:

- User login/registration
- Payments through Stripe
- Existing community posts and comments can be edited/deleted
- Profile information can be edited
- Past orders and posts can be accessed via My Profile
- Access to all other users' posts
- The ability to comment on posts
- The ability to subscribe to newsletter

Future user features will include:

- Selecting colour for Activewear certain products
- Selecting different flavours for Nutrition certain products

Current store owner features include:

- All posts and comments are visible and fully editable

A key future store owner feature will be:

- All user profiles and the most important information is visible as well

### Marketing Related Features

- Subscribe to Newsletter
    As part of the web marketing strategy for the application, functionality to subscribe to a company newsletter was added. The subscribe feature is available by clicking the mailchimp icon in header. On regular screens subscription form is a pop up, while on smaller screens it is in the footer of each page on the site. The user simply has to enter an email address and click on the Subscribe button to sign up. The subscription list is managed by mailchimp website https://mailchimp.com/.

    Subscribe to newsletter (regular sized screen):

    ![Mailchimp1](media/screenshots/mailchimp_1.png)
    
    Subscribe to newsletter (small screens):

    ![Mailchimp1](media/screenshots/mailchimp_2.png)

- Social media
    Another part of the web marketing strategy is to use social media to promote the site. A Facebook and Instagram pages, and X (Twitter) account ware created and a link to this appears in the header of each page on the site.

    1. Facebook (https://www.facebook.com/profile.php?id=61559866552324)

        ![Facebook](media/screenshots/facebook_marketing.png)

    2. Instagram (https://www.instagram.com/gofit8298/)

        ![Instagram](media/screenshots/go_fit_instagram.png)

    3. X (https://twitter.com/fit534457)

        ![x](media/screenshots/xtwitter.png)



## Testing

### General

Regular testing was conducted throughout the course of this project, especially before commits to Github.

Responsive/Mobile-first design was tested using Chrome developer tools to ensure desired layout was achieved. As well as Chrome, and Firefox which successfully affirmed my project's responsiveness. To test responsiveness, the following mobiles were tested Galaxy S8+, Pixel 7, iPhone 14 Pro Max, iPad Pro. All successfully passed in mobile responsiveness of the page.

### Validator Testing

- Html was Validated using the [HTML Validator](https://validator.w3.org/).

- CSS was Validated using the [CSS Validator](https://jigsaw.w3.org/css-validator/).

- Python Validation was performed installing flake8 (command : pip install flake8) and using it (command : python -m flake8). No serious errors reported.

### Manual User Story Testing

- As a user, I want to view a list of products - Pass
- As a user, I want to view a specific category of products - Pass
- As a user, I want to view individual product details - Pass
- As a user, I want to sort the list of available products - Pass
- As a user, I want to sort a specific category of products - Pass
- As a user, I want to sort multiple categories of products simultaneously - Pass
- As a user, I want to search for a product by name or description - Pass
- As a user, I want to easily see what I've searched for and the number of results - Pass
- As a user, I want to easily see the size and quantity of a product when purchasing it - Pass
- As a user, I want to view items in my bag to be purchased - Pass
- As a user, I want to adjust the quantity of individual items in my bag - Pass
- As a user, I want to easily enter my payment information - Pass
- As a user, I want to feel my personal and payment information is safe and secure - Pass
- As a user, I want to view an order confirmation after check out - Pass
- As a user, I want to receive an email confirmation after checking out - Pass
- As a user, I want to register for an account - Pass
- As a user, I want to login/logout - Pass
- As a user, I want to receive an email confirmation after registering - Pass
- As a user, I want to have a personalized user profile - Pass
- As a user, I want to view list of community posts - Pass
- As a user, I want to open a post - Pass
- As a user, I want to view comments for Posts - Pass
- As a user, I want to manage my posts - Pass
- As a user, I want to manage my comments - Pass
- As a user, I want to find the site through the web search engines - Pass
- As a user, I want to view a list of challenges - Pass
- As a user, I want to subscribe to newsletter - Pass
- As a user, I want to add a product - Pass
- As a user, I want to edit/update a product - Pass
- As a user, I want to delete a product - Pass
- As a user, I want to add a challenge - Pass
- As a user, I want to edit/update a challenge - Pass

## Deployment

### Github

Deployed using the Master Branch on hosting platform GitHub Pages.

The following steps were taken:

1. Create a master branch in Github repository
2. Use Visual Studio Code IDE to build the site
3. Commit files to the staging area using bash terminal commands: git status; git add (specify directory); git commit -m "add message"
4. Push files to the working environment using git push, which updates the repository
5. Publish site from master branch using settings tab in the main page of the repository, select source as master branch, then save

### Heroku

Deployed on Heroku using the master branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a requirements.txt file so Heroku can install the required dependencies to run the app.
    - sudo pip3 freeze --local > requirements.txt
2. Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
    - echo web: python run.py > Procfile
3. Sign up for a free Heroku account, create your project app, and click the Deploy tab, at which point you can Connect GitHub as the Deployment Method, and select Enable Automatic Deployment.
4. In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:
    - Key:Value 
    - AWS_ACCESS_KEY_ID      : `<your secret key>` 
    - AWS_SECRET_ACCESS_KEY  : `<your secret key>`
    - USE_AWS                : `True`
    - DATABASE_URL           : `<your postgres database url>`
    - SECRET_KEY             : `<your secret key>`
    - STRIPE_PUBLIC_KEY      : `<your secret key>`
    - STRIPE_SECRET_KEY      : `<your secret key>`
    - STRIPE_WH_SECRET       : `<your secret key>`
5. App should be successfully deployed to Heroku at this point.
6. From the command line of the IDE:
    - Enter heroku postres shell
    - Migrate the database models
    - Create a superuser account in the new database
7. In the heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch and click "Deploy Branch".
8. Once the build is complete, click the "View app" button.

## Credits

### Content

- Content was created and assessed by Matija Stankovic

### Media

- Image Gallery: free images from Pexels.com

### Acknowledgements

- Completion of an app and it's features would not have been possible without the support and advice of my mentor Brian Macharia