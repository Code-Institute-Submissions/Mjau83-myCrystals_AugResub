# myCrystals
### A handy way to organize your crystals


![Responsive Image](assets/images/responsive-image.png)


## Project Goals
**What is it?** 
A simple way to store information about your crystals so that you can access the information when you need it.

**Who is it for?**
This is for any healer, witch, yogi or anyone that likes spriritual stuff and might use crystals in their daily life, 
in rituals, meditaion or other practices. 

**Why am I building it?**
Almost everytime when I'm going to use a crystal for a specific purpose I need to check my crystal box to see what 
I have, and if I can't remember what it's used for I also need to turn to Google to find out the specific properties.
After asking around in different spriritually themed communities it turned out that I wasn't alone. I hope that this 
site can help us get a little bit more organized.


## Table of Content

* [**UX**](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owner Goals](#site-owner-goals)
    * [Design](#design) 
* [**Wireframes**](#wireframes)
* [**Database Structure**](#database-structure)
* [**Features**](#features)
* [**Technologies Used**](#technologies-used)
    * [Languages](#languages)
    * [Frameworks Libraries Programs](#frameworks-libraries-programs)
* [**Testing**](#testing)
    * [Bugs](#bugs)
    * [To Do](#to-do)
* [**Deployment**](#deployment)
    * [GitHub Pages](#gitHub-pages)
* [**Credits**](#credits)


## UX

### User Goals
* The site should work on all devices
* The User should be able to register a Username
* The site should have a clear dashboard that is easy to navigate
* The User should be able to add multiple crystals
* The User shoud be able to check if a crystal is waterproof and/or sunproof
* The User should be able to add information like name, color, properties etc about each crystal

### User Stories

* As a user I want to, be able to register a uniqe Username and a Password
* As a user I want to, be able to Login and Logout
* As a user I want to, add/create as many crystals as I want to
* As a user I want to, add information about each crystal
* As a user I want to, be able to search for specific properties 
* As a user I want to, be able to edit/update my information
* As a user I want to, be able to delete a crystal 
* As a user I want to, be able to journal when a crystal last was used

### Site Owner Goals
* To have a site that is attractive to the spiritual community
* Have good functionallity for the User

### Design

#### Fonts:

I used fonts from [Google Fonts](https://fonts.google.com/)
* [Fontname] text

#### Images:

Text about image source

#### Color: 

Text about colors

![Color palette](assets/images/color-palette.png)

[Back to top](#table-of-content)


## Wireframes
Balsamiq was used to create the wireframes for this project

* Desktop Wireframes
    * [Index](wireframes/index.png)
    * [ ]( )
    
* Tablet Wireframes
    * [Index](wireframes/index-tablet.png)
    * [ ]( )

* Smartphone Wireframes 
    * [Index](wireframes/index-sp.png)
    * [ ]( )

[Back to top](#table-of-content)


## Database Structure

Add tables here

[Back to top](#table-of-content)


## Features
* Responsive on different devices
* Login and Logout functionallity
* Search crystals by properties, color or journal
* CRUD:
    * Create - Possability to add new crystals and to journal the usage
    * Read - Possability to view the added information about each crystal and to see when and how it was last used
    * Update - Possability to update the information and the journal for each crystal 
    * Delete - Possability to delete a crystal and/or the journal 

[Back to top](#table-of-content)

## Technologies Used
### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks and Libraries 
* [Google Fonts](https://fonts.google.com/) was used to import the fonts mentioned above 
in the project
??* [Coolors](https://coolors.co/) was used to decide on th colors and to create the color 
palette
* [Am I Responsive](http://ami.responsivedesign.is/) was used to make the mockup
??* [Boostrap](https://getbootstrap.com/) was used to make the site responsive

### Tools
* [Balsamic](https://balsamiq.com) was used to create wireframes in the beginning of 
the project
* [WebAIM](https://webaim.org/resources/contrastchecker/) was used to check that the contrast is ok
??* [Gimp](https://www.gimp.org/) was used to edit photos.
* [Favicon.cc](https://www.favicon.cc/) was used to create the fave icon
* [Webformatter](https://webformatter.com/html) was used to beautify the code
??* [Copressor.io](https://compressor.io/) was used to compress the background image
* [Gitpod](https://gitpod.io/) was used for coding the project
* [Github](https://github.com/) was used to save and stored on the project after being 
pushed from Gitpod. Github was also use to deploy the site

[Back to top](#table-of-content)


## Testing

?? The was tested for Android on Samsung A50 and Xperia 10. It was also tested on laptop
and desktop view (PC).

The code was tested with:
* [W3C Markup Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JSHint](https://jshint.com/)

**Lighthouse**

* Test 1

![Lighthouse test 1](assets/images/lighthouse-test1.png)
* Test 2

![Lighthouse test 1](assets/images/lighthouse-test2.png)


## User Stories
**As a user I want to, be able to register a uniqe Username and a Password**

* Plan

I want to create a form that the user can use for registration to add a uniqe username. If no other
user have the same username the user can register a password that the user like.

* Implementation

I created a form for the user to fill in when they click on "Register". Here the user can choose a username
and a password. If the username already exsists a flash message will be displayed to the user that the
"Username already exists", and the user will be redirected to a empty registration form to try again.
If the username dosn't exist in the db the new user will be inserted to the db and the user gets logged in
to start add crystals to the userprofile.

* Test

I tried to add three different users to see that the registration form worked properly. At sometime I tried
to add a username that already was in the db, and that showed me the flash message telling me to try again.


* Result

The new user is registered to the db only if the username doesn't exsist in the db already, and a new user
can't register a username that already exsist

* Verdict 

The registration form works as planned.

**As a user I want to, be able to Login and Logout**

* Plan

I the user already is registered I want them to be able to log in using the password they choose at
the point of registration. I also want them to be able to log out from the session when they like to.

* Implementation

When the user enters the website they can choose to log in if they have registered befor. The form checks to 
see if the username is in the db, and if it, is it check so that the username matches. If it's a match the
user gets logged in and can view all the crystals they have added. If the user doesn't exist in the db, or
if the username doesn't match, and the user will be redirected to a empty log in form to try again. When the
user wishes to log out they can click on the "Log Out" link in the navbar and that will end the session and 
take them back to the log in form.

* Test

I have tried to log in with a password that doesn't match the registered user, and I have tried to log in 
with a username that doesn't exists in the db. Both shows the flash message telle me "The Username and/or 
Password is incorrect. Please try again". I have also tried logging out using both the log out link in the
navbar and the link in the mobile sidenav, and both are redirecting me to the log in form again so that I
can log in again if I like.

* Result

A unregistered user can't log in, neither can a registered user that uses the wrong password. Both gets a
message to try again. When the user want to log out they are redirected to the log in page after logging out.

* Verdict 

Both log in and log out function works as planned

**As a user I want to, add/create as many crystals as I want to**

* Plan

Text

* Implementation

Text

* Test

Text

* Result

Text

* Verdict 

Text

**As a user I want to, add information about each crystal**

* Plan

Text

* Implementation

Text

* Test

Text

* Result

Text

* Verdict 

Text

**As a user I want to, be able to search for specific properties**

* Plan

Text

* Implementation

Text

* Test

Text

* Result

Text

* Verdict 

Text

**As a user I want to, be able to edit/update my information**

* Plan

Text

* Implementation

Text

* Test

Text

* Result

Text

* Verdict 

Text

**As a user I want to, be able to delete a crystal**

* Plan

Text

* Implementation

Text

* Test

Text

* Result

Text

* Verdict 

Text

**As a user I want to, be able to journal when a crystal last was used**

* Plan

Text

* Implementation

Text

* Test

Text

* Result

Text

* Verdict 

Text

[Back to top](#table-of-content)


## Bugs

**Opacity bug**
* **Bug**

The opacity of the background image in index.html and register.html affects
all the content on the page so that the card and form also gets more transparent.

* **Fix**

At first I had just added opacity to the #crystal-background in style.css.
I then tried adding a div with the class of "opaque-overlay" after the "crystal-background" div, 
and then giving it a z-index of -1 and the crystal-background a z-index of -2.
I then gave opaque-overlay background-color of #ffffff and a opacity of 0.5
That didn't solve the problem.
After some reading on W3 Schools I change hex to rgba, and got it to work. 

* **Verdict**

The background image is showing with a white opaque overlay without affecting the rest of the
content on the page.

**Clickable bug**
* **Bug**

After adding the opaque overlay properly everything looked good, but it turned out
that nothing on the page was clickable. Everthing worked fine in the navbar, but 
the pointer wouldn't change when hovering over "Register" or "Log In" on index.html

* **Fix**

Once again I tried laborating with the z-index back and forth to see what could be
the issue. As soon as I commented out #crystal-background in style.css everything
worked again. After using developer tools and gotten some help from my mentor 
understanding what was happeing, it turned out that the issue was within the card 
class. So after adding *pointer-events* in style.css and setting it to *auto* and 
changing the z-index to positive values for #crystal-background and .opaque-overlay
I finaly got it to work.

* **Verdict**

Everything on the index.html page is now clickable and working as it should. 


**Username bug**
* **Bug**

The username won't show at the top of the crystals.html

* **Fix**

Instead of just using {{ username }} in profile.html I changed it to url_for('profile', 
username=session['user']). This shows */profile/username* at the top. I tried to figure out
where this was comming from, and removed "/profile" from @app.route in app.py ending up with
*@app.route ("/< username >"*. Now the profile.html shows *Hello /username* at the top, but
I still got a "/" to much. 

* **Verdict**

Text

**Add crystal bug**
* **Bug**

After creating the edit_crystal_form.html and creating the functionallity 
for it in app.py the Add Crystal link in the navbar stopped working, and it displayed
an "undefined" error saying *'crystal' is not defined*. I had a hard time figureing out
exactely what it meant, and how to read the traceback. So after trying to search on google
without getting any smarter I turned to Tutor Support. 

* **Fix**
The code snippet that seem to be causing the error was *return render_template("pages/
add_crystal.html", chakras=chakras)* in on line 123 in app.py. So I tried adding *crystal=
crystal* to it since crystal wasn't defined. It didn't help. I also tried creating a variable
above the *chakra* variable on line 122, and move *mongo.db.crystals.insert_one(crystal)* to it.
But with no success. After talking with Jo on Tutor Support it seemed like the error wasn't really
in app.py, but in *chakras.html* which was included in both *edit_crystal_form.html* and 
*add_crystal_form.html*. So instaed of using {% include "components/chakras.html" %} in *add_
crystal_form.html* I pasted the code from chakras.html, and removed the if statement. Now the 
Add Crystal link finally worked!

* **Verdict**

The Add Crystal form shows up when clicking the link in the navbar and adds a new crystal 
to the db.


**Modal bug**
* **Bug**

Modal won't show when the Delete button is clicked in crystals.html

* **Fix**

I tried some solutions that I could find on Stackoverflow; like changing *href* to *onclick*
and use *$('#delete-crystal').modal('open');* and also adding *$('#delete-crystal').modal();*
to the js file. I also tried using *$('.trigger-modal').modal();* and removing the modal class.


* **Verdict**

Text

* **Verdict**

Text

**name bug**
* **Bug**

Text

* **Fix**

Text

* **Verdict**

Text

[Back to top](#table-of-content)


## To Do
* 
* 
* 

[Back to top](#table-of-content)


## Deployment
### GitHub Pages
How to deploy project using Github pages:

1. Go to Github
2. Log in and click on “Repositories” tab in the top middle of the screen
3. Choose this repository
4. Click on the "Settings" tab (with a gear icon)
5. Scroll down on the page until you find the "Github Pages" section
6. Under "Source" you'll find a dropdown which is set to "none"
7. Change it to "Master"
8. Then click the save button. This will reload the page.
9. Scroll back down to "Github Pages"
10. A green alert box will now tell you that your site been published and provide you a link to the site.

![Deployment Image](assets/images/deployment.png)

[Back to top](#table-of-content)

## Credits
#### Inspiration 
* [ ]( )
* [ ]( )

* Thank you to...
* A huge thank you to my mentor Simen Eventyret_mentor for all the good advices, feedback 
and most of all patience.
* Thank you to my older brother David who’s been a wonderful support in me deepest times of 
dispear and helped me with testing and good advices to help me get a better understanding for the code.
You're the best!

[Back to top](#table-of-content)