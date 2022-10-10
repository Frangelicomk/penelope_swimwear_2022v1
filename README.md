<h1 align="center">Penelope Calenti Swimwear Collection 2022</h1>

[Penelope Calenti Swimwear Collection 2022]( https://penelope-c-epimoni.herokuapp.com/)

This is my final project MS4 for Code Institute. Featuring Penelope Calenti Swimwear Collection a real life project requested by a friend.


<h2 align="center"><img src="static/img/testing/responsiveimgweb.png" alt="screenshot taken from AmIresponsivesite showing the webpages responsiveness on a Laptop , Desktop and Mobile"></h2>


## Table of contents
1. [User Experience (UX)](#user-experience-ux)
    + User Stories
    + Design
    + Wireframes
2. [Features](#features) 
    + Existing Features
    + Upcoming Features
3. [Technologies Used](#technologies-used)
    + Languages Used
    + Frameworks, Libraries & Progragms Used
4. [Testing](#testing)
5. [Deployment to Git Hub](#deployment-to-github)
5. [Deployment to Heroku](#deployment-to-heroku)
5. [S3 Amazon Bucket](#aws-s3-bucket-creation)
6. [Credits](#credits)

## User Experience (UX)

+ ### User Stories

    + First Time Visitors

       1. For First time visitors the owner of the collection wished to have a big hero image to attract the viewer.
       2. Landing page to be minimal with few buttons and easy navigation.
       3. First time visitors to be able to view quickly the products see prices and images for each product.
       4. To be able to securely and quickly check out.
       5. To be able to adjust their bag
       6. Receive confirmation emails for their order.
       7. If they wish to send a message regarding a product or an order the visitor must be able to do so using an easy contact form located in the landing
       page.
       8. If they wish to create an account this must be an easy sign up process and also to keep their data secure.
       9. First time visitors should be able to subscribe/unsubscribe to newsletter.

    + Returing Visitors

       1. Should be able to to have all the perks from First time visitors list plus +
          + Able to quickly log in to their profile
          + Have the option to unsubscribe from newsletter if not happy / this will be also do able from the emails received.
          + if they have forgotten their email address to be able to request a password reset email.
          + if they havent got an account yet to be able to register for an account this must be securely done and a confirmation email must be send.
          + Pop up messages to be active so they can see each actions taken while on the site.
          + Design to be minimal and attractive to returning visitors and to showcase products to attract the eye.

    + Frequent Visitors (such as Recruiters/employers/collaborators)
         + Should be able to upload an image to their profile and track past orders.
         + To be able to reset their password by entering their email address and also receive a confirmation email which will contain a secure
         link to reset password HTML and then redirecting them straight to log in page.
         + In the feature will be added a blog and comments for each product so registered visitors should be able to see comments, add comments and also delete their comments.
   
    + Manager, Admin and Staff
         + Should have a superuser account so they can be able to access admin site
         + Staff should be able to review only orders ( This will be sorted later on when the owner decided each staff access to the admin and to the website )
         + Admins should be able to log in and do changes to orders and also to be able to update user accounts.
         + Currently only the Manager ( Founder ) will be able to add products, edit products and Delete Products. ( This will be reviewed again when the site goes live. )
         + Manager and admin should be able to change or add images to the products and also update their profiles.
         + Manager to receive emails from the contact form and also be able to review subscribers from the admin panel ( This will be added into HTML in the feature )
            - The admin should be able to upload and send a file as a formatted email.
            - The admin should access a dashboard to view subscribers and sent emails.



+ ### Design

  + Colour Scheme

     + [CREATIVE-TIM](https://www.creative-tim.com/product/paper-kit-2-pro) for his premium Paper Kit 2 Pro UI KIT which I used to customise my UI and save me some time with CSS and Bootstrap
  
  + Imagery 
     
     + All images are owned be [Penelope Calenti](https://www.instagram.com/penelope.calenti.swimwear/)

+ ### Wireframes
  
   + Wireframes were done by [Penelope Calenti](https://www.instagram.com/penelope.calenti.swimwear/) which I currently do not have as I have deleted the folder accidently from my computer

## Features

+ Responsive on all device sizes


## Upcoming Features 

+ Newsletters with the option to Subscribe/Unsubscribe. ( this has been implemented but will require some further review and changes )
+ Comments on images
+ Blog with Fashion News and where [Penelope Calenti](https://www.instagram.com/penelope.calenti.swimwear/) will be appearing next.
+ A Travel Blog to be added on the site with discounts as requested be Founder.


## Technologies Used 

### Languages Used
+ [HTML 5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/CSS)
+ [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)
+ [PYTHON 3.X](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
1. [Bootstrap v.5 Beta](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
    + Bootstrap was used to assist with the responsiveness and some styling of the website
2. [DJANGO](https://www.djangoproject.com/)
3. [Font Awesome](https://fontawesome.com)
    + Font Awesome used for widgets and icons
4. ~~[Clip Path](https://www.cssportal.com/css-clip-path-generator/): Clip Path used for the design and animation of the hero image~~
5. [Git](https://git-scm.com)
    + Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [Github](https://github.com)
    + GitHub is used to store the projects code after being pushed from Git.
7. [Photoshop](https://www.adobe.com/ie/products/photoshop.html)
    + Photoshop was used to create the logo, resizing images and editing photos for the website.
8. [jQuery](https://en.wikipedia.org/wiki/JQuery)
    + jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
9. [Balsamiq](https://balsamiq.com)
    + Balsamiq was used to create the wireframes during the design process. I accidently deleted this folder in my computer and lost the wireframes :/
10. [Can I Use](https://caniuse.com)
    + Can I Use provides up-to-date browser support tables for support of front-end web technologies on desktop and mobile web browsers.
## Testing

Jshint used to validate Javascript , The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of <br>the project to ensure there were no syntax errors in the project. Color Contrast checker Coolors used to check the contrast and also pick the right colour palette for the website. Also for testing I used CLI to check for errors and fixed the issues showed in Problems tab.
+ [JSHint](https://jshint.com/)
+ [W3C Markup Validator](https://validator.w3.org/#validate_by_uri+with_options)
+ [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
+ [Color Contrast Checker](https://color.a11y.com/)


### Testing User Stories
+ User Stories

  + First Time Visitors

   1. For First time visitors the owner of the collection wished to have a big hero image to attract the viewer.
      - This have been achieved by the hero image on the landing page which is nicely responsive on every device.
        Also it showcases straight away that the site is about fashion/summer and clothing in general.
   2. Landing page to be minimal with few buttons and easy navigation.
      - Landin page is minimal with a nice animated navigation bar which translates into side navigation bar on small devices making access much easier
        for the users.
   3. First time visitors to be able to view quickly the products see prices and images for each product.
      - This have been achieved as the visitor can have a glance of the products on the landing page rather than navigating into collections
   4. To be able to securely and quickly check out.
      - This have been achieved using stripe documentation and the visitor is able to check out without loging in. Stripe takes protection to an other level.
      - Also the user will receive a confirmation email when checking out to his email address, check out withour providing a valid email address is not possible.
      - The form for secure check out requires validation and for security reasons all fields must be completed.
   5. To be able to adjust their bag
      - Users are able to adjust the bag accordingly this have been achieved with Javascript which I followed the instructions from Code Institute Boutique Ado
   6. Receive confirmation emails for their order.
      - Emails are now send to users as a confirmation of their order
   7. If they wish to send a message regarding a product or an order the visitor must be able to do so using an easy contact form located in the landing
   page.
      - This has been achieved as there is a new contact form nicely designed in the landing page and users can send emails directly to the Founder with any queries,
      this will be changed to an info mail when the site goes live.
   8. If they wish to create an account this must be an easy sign up process and also to keep their data secure.
      - This have been achieved by adding a new Sign in and Sign up button, the forms are easy to ready and to be followed and authentication is required. Once the users create
      and accound they will be redirected to the log in page after confirming their email address. On their account they will be able to see past order history.
   9. First time visitors should be able to subscribe/unsubscribe to newsletter.
      - There is a subscription button to newsletter, users must confirm again their email address this is to stop spam and also when they receive news letter they have the 
      option to unsubscribe. This doest work completely as it should be but more about this on the [Known Bugs Sections](##difficulties-encountered-&-bugs)

  + Returning Visitors 
    1. Should be able to to have all the perks from First time visitors list plus +
          + Able to quickly log in to their profile
            - this have been achieved as there is a log in button and also redirects to users profile.
          + Have the option to unsubscribe from newsletter if not happy / this will be also do able from the emails received.
            - While this is in development users receive news letters but the link generated isnt working as it should have been. In the feature will be added
            a button in users profile to instantly unsubscribe/subscribe.
          + if they have forgotten their email address to be able to request a password reset email.
            - This have been achieved using Django Allauth reset password and users are receiving an email with a link to reset their password, in the feature this will
            be more customised.
          + if they havent got an account yet to be able to register for an account this must be securely done and a confirmation email must be send.
            - Achieved again by Django Allauth form, there is a nicely designed sign up form which fields are required and user must confirm their email address before
            they get access to their account. Also due to authentication users can not use already taken emails.
          + Pop up messages to be active so they can see each actions taken while on the site.
            - Pop up messages work on each pages to inform users about their actions, for example when a user adds a product in the bag then a message pop ups on the top
            right which notifies user about the bag content. ( This was achieved with the help from Boutique Ado project. )
          + Design to be minimal and attractive to returning visitors and to showcase products to attract the eye.
           - All pages designed to be minimal with nice colours and slim navigation bars.

  + Frequent Visitors ()

         + Should be able to upload an image to their profile and track past orders.
          - This have been achieved now when the user updates their contact details in the their profile they have the option to add a profile image.
         + To be able to reset their password by entering their email address and also receive a confirmation email which will contain a secure
         link to reset password HTML and then redirecting them straight to log in page.
          - This have been achieved using Django Allauth reset password and users are receiving an email with a link to reset their password, in the feature this will
            be more customised.
         + In the feature will be added a blog and comments for each product so registered visitors should be able to see comments, add comments and also delete their comments.
          - This will be an upcoming feature.

  + Manager, Admin and Staff
         + Should have a superuser account so they can be able to access admin site
          - Currently there is only one superuser account which can create multiple user account from the admin panel and give the permissions required.
         + Staff should be able to review only orders ( This will be sorted later on when the owner decided each staff access to the admin and to the website )
          - Superuser can adjust this from the admin panel
         + Admins should be able to log in and do changes to orders and also to be able to update user accounts.
          - Can be done from the admin panel if authority given by the superuser.
         + Currently only the Manager ( Founder ) will be able to add products, edit products and Delete Products. ( This will be reviewed again when the site goes live. )
          - This achieved only superusers have access to navigation links to add edit and delete products.
         + Manager and admin should be able to change or add images to the products and also update their profiles.
          - This have been achieved as they have custom made profile. In the feature managers will be able to have more tab in their profile so they can check subscribers
          send emails and also post blog posts and comments.
         + Manager to receive emails from the contact form and also be able to review subscribers from the admin panel ( This will be added into HTML in the feature )
          - This have been achieved and the email address is working, the registered email address now receives all emails from the contact form


+ Tested by friends from facebook and colleagues in differnt divices

  + As I did not have many time to create a type form again as I have done in the past so I can gather more feed back for testing and overall functionality. Friends and Colleagues tested all the buttons and links, repsonsiveness have been tested in laptops 13 and 17 inch screens. Computers with 17, 24, 27, 32 and 40 inch screens. and in noumerous off mobile devices. There is an unknown bug when you open the site with Mi navigation pages which HTML content dont load as they should be. I do not know what causing this glitch. Same phone with Chrome open works fine.

+ Feedback
  
  + The site got some nice feed back for the features and the upcoming features. I was not able to fix edit product page as I wanted as I do not personally like adding extra images for the products
  as it is now but I couldnt fix it. Also in the future I will add the option for the super user to be able to delete selected extra images, I didnt have the time to think about how this can be 
  achieved
  + The site over works fine, I am not happy how the newsletter turned up as the functionality doesnt work as I wanted. I will do more research about this.

### Further Testing
+ The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, Opera and Safari browsers.
+ The website was viewed on a variety of devices such as Desktop, Laptop, Samsung S20/S22 Ultra and iPhoneX.
+ A large amount of testing was done to ensure that all pages were linking correctly. 
+ Friends, Colleagues from work and family members were asked to review the site and documentation <br>to point out any bugs and/or user experience issues.
+ I personally have access in 27" 4K Monitor, a 17" Laptop, Android phone which I constatly used for testing.
+ I have used Chrome Developer Tools as Opera Dev Tools to constantly check the website responsivness.
+ As I dont want more images on the markdown please find the testing screenshots on the testing folder. This can be achieved if you navigate on my github page then go to [penelope_swimwear_2022v1](https://github.com/Frangelicomk/penelope_swimwear_2022v1) project there you will find a folder named static
if you click on there you will see img then  a subfolder testing. If you right click on that folder you will see the images I have uploaded.
Alternatively you can click [here](https://github.com/Frangelicomk/penelope_swimwear_2022v1/tree/main/static/img/testing) to see the folder on my github straight away.

### Difficulties Encountered & Bugs

+ This will be a big section it seems. While when you are subscribing onto the email you receive an email to confirm emai this doesnt works as I wanted the generated email doesnt work.
  I tried to fix this but it gets worst every time i touch it, so I will try later again. If you confirm user from the admin panen subscribers then admins can send an email to all subscribers without any issue but again the link to unsubsribe doesnt work either.

+ An other bug was that I couldnt add extra images the way I wanted and every time i clicked add image this was creating instances with no images if it was left blank. Likely a Daisy Mentor from Slack helped me solve this issue. I changed the model field from Null=True to false so now you can not submit the form without adding an image. I know it doesnt look preaty as interface now that I added this feature but I will change it in the future. My plan was to create instances ( I believe with JS ) for every image I upload to create thubnails on the right side of the main image.
I wanted to write a code that for each image > 1 then that images will be automatically added as thubnails and extra images. Also when extra images are created I couldnt get the ID from those.
I think this sounds overall too complicated but I want to learn how to code what I have in my head the easy way.

+ I had a big issue when trying to update an product with no image as the default was not loading. That was very frustrating as the app kept crushing. Slack community helped me to fix this issue by migrating correctly changes in heroku directly.

+ I found it difficult to add staff members, I was thinking to create an app to add staff members with details and the 3 higher ranking to be displayed in the landing page ( team section )
this task was impossible so I gave up and did commit to git hub. I tested it on Vscode. ( When I tried to clone my project locally the vars werent working and I didnt know how to fix this. )

+ The most difficult part was to add extra images and for each extra image to create a carousel entry for the product details. It took me more than 2 days to set this up but I managed to solve it on my own using dev tools and inspecting admin, then I created the form on my own using the inspected attributes which fixed the issue.

+ There was a bug mentioned before if you open the app on Mi navigation the app doesnt load correctly Which still I dont know why. probably due to drivers.

+ I have done a lot of changes and While I Havent encountered many bugs the ones that I encountered took me long time to solve. Sounds easier that it was.

## Deployment to Github

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```


## Deployment to Heroku

### Heroku

The project was deployed to Heroku following the next steps:
1. Create a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`.
2. Create a Procfile with the terminal command `echo web: python manage.py > Procfile`.
3. Proceed with git add and git commit the new requirements and Procfile and then git push the project to GitHub.
4. Create a new app on [Heroku website](https://dashboard.heroku.com/) by clicking the "New" button on your dashboard. Give it a name and set the region to Europe.
5. From the Heroku dashboard of your newly created application, click on "Deploy", "Deployment method" and "select Github".
6. Confirm the linking of the Heroku app to the correct Github repository.
7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:
DATABASE_URL: 
SECRET_KEY :
9. You will also need to add extra vars for sending emails, Stripe payments, and AWS bucket S3 cloud storage.
10. Click on enable deployment.
11. Wait until you get notified a the bottom of the page that your app is deployed and vie the deployment.


## AWS S3 Bucket Creation

### Creating S3 Bucket 

I have followed Code Institute Video + I read the documentation found in [AWS](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html)
When you create and upload your files to your bucket you need to set up the following variables in Heroku.

1. Go to your app_name
2. Click onto settings and the reveal conf vars
3. Add AWS_ACCESS_KEY_ID = YOUR_KEY
4. Add AWS_SECRET_ACCESS_KEY = YOUR_SECRET_KEY
5. USE_AWS = True "This is because in developement we use static files and media files while when our app lunches we will use the S3 Bucket"


## Credits

### Code
+ [Bootstrap v5 Beta](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.
+ All code was written by Michael Kefalas

### Content 
+ All content was written by Developer and Designer Michael Kefalas
+ Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media 
+ Images were shared to me by the owner Penelope Calenti who owns the collection of swimwear.
+ [CREATIVE-TIM](https://www.creative-tim.com/product/paper-kit-2-pro) for his premium Paper Kit 2 Pro UI KIT which I used to customise my UI and save me some time with CSS and Bootstrap
### Acknowledgements 
+ [Adobe](https://www.adobe.com/#) for their tutorials and videos in their youtube channel found [here](https://www.youtube.com/user/AdobeCreativeCloud)
+ Youtubers which i got inspired from :
  + [Kevin Powell](https://www.kevinpowell.co) for his amazing videos regarding CSS and Grid , his approach on designs is something I want to learn and also I am having his
  course as well for Flexbox
  + [Gary Simon](https://dribbble.com/Coursetro) has been a great inspiration and you can follow his discord channel [here!](https://discord.gg/wQQtgNey)
  + [Very Academy](https://www.youtube.com/c/veryacademy) some cool videos to learn Django.
  + [Denis Ivy](https://www.youtube.com/c/DennisIvy) Nice courses for beginners and advanced coders.
+ Fellow Coders from [Slack](https://slack.com/intl/en-gb/)
+ Also I have to thank [Nescafe](https://www.nescafe.com/gb/) which is my go to go Coffee helping me maintain my eyes open while coding late in the evening.This doesnt count as
an ad right? And if i continue like this I will Acknowledge Specsavers as they will soon provide me with glasses :)

