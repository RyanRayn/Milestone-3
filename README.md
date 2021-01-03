<p align="center"><img src="/static/images/mockup.png" width="400"></p>


# **Keeping TABS**
View the live project [HERE.](https://keeping-tabs-ryan.herokuapp.com/)

***

## **Introduction**

Keeping Tabs is a platform that allows users to audit all their personal relationships by keeping track of daily interactions. Searchable entries for each relationship are organized into three categories, happy, sad, and angry, statistics are then displayed on a profile dashboard giving an idea of that relationships health. In efforts to encourage keeping lines of communication open, the user can send an email expressing their feelings directly from each profile page. Users can also send a "thank you" gift, in this example, it is a Starbucks gift card. Keeping Tabs is not only about keeping track of bad things people do to you but also bringing to light all the positive moments that can sometimes be overlooked.   

***

## **Table Of Contents**

  * [**Introduction**](#--introduction--)
  * [**User Experience (UX)**](#--user-experience--ux---)
    + [User Stories](#user-stories)
    + [Target Audience](#target-audience)
    + [User Goals](#user-goals)
    + [Design](#design)
    + [Wireframes](#wireframes)
  * [**Features**](#--features--)
  * [**Technologies Used**](#--technologies-used--)
    + [Languages Used](#languages-used)
    + [Frameworks, Libraries & Programs Used](#frameworks--libraries---programs-used)
  * [**Testing**](#--testing--)
    + [Testing User Stories from UX Section](#testing-user-stories-from-ux-section)
    + [Further Testing](#further-testing)
  * [**Deployment**](#--deployment--)
    + [Project Creation](#project-creation)
    + [Deployment to Heroku](#deployment-to-heroku)
  * [**Credits**](#--credits--)
    + [Code](#code)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)

***

## **User Experience (UX)**

### User Stories
##### *First Time Users*
* As a first time user, I would like to easily understand the purpose of the site.

* As a first time user, I would like to easily navigate through the site's content.

* As a first time user, I would like to easily understand all the data presented to me.

* As a first time user, I would like to easily understand how the all site's functions work.

##### *Frequent Visitors*
* As a frequent visitor, I would like to regularly see new relationship tips.

* As a frequent visitor, I would like new gifts on offer to send to people.

* As a frequent visitor, I would like to see new statistics and relationship metrics.

### Target Audience
* People in long term relationships
* People having relationship trouble
* People with large families
* People who spend a lot of time in a tight-knit workplace
* People who feel they are often taken advantage of

### User Goals
* Allow users to keep track of relationships with minimal effort
* Clearly display to users easy to understand relationship statistics
* Encourage users to show appreciation for good deeds
* Encourage users to be open and communicate their feelings, good and bad
* Help users understand if they are in a toxic relationship 

### Design
##### *Color Scheme*
* The main four colors repeated throughout the site are:

  1. Blue - rgb(110, 110, 255)
  1. Orange - rgb(255, 187, 0)
  1. Red - rgb(253, 87, 87)
  1. Grey - rgb(155, 155, 155)

##### *Typography*
* Kanit is the font used for all text on the site, with Sans Serif as the fallback font on the occasion the sites other fonts aren't loading properly.

##### *Imagery*
* Each page contains Font Awesome icons that display different emotions to match the purpose of the site and encourage users to share their feelings.

##### *Homepage* 
* All pages were designed for ease of use and avoid confusion. Landing pages on mobile views have a hamburger icon in the top right corner containing a dropdown menu for access to other pages.

<p align="center"><img src="/static/images/mobilehamburger.png" width="400"></p>

* Both mobile and desktop home page views also contain a multiple buttons encouraging new users to register or log in.

<p align="center"><img src="/static/images/tablethome.png" width="400"></p>

* After logging in users are redirected back to the home page that now displays user specific data including a scoreboard with a breakdown of all their entries. 

<p align="center"><img src="/static/images/homedashboard.png" width="400"></p>

* All pages also offer multiple access points for users to make a quick entry or look up profile data.

<p align="center"><img src="/static/images/homeprofiles.png" width="400"></p>

##### *Registration and Log in pages*
* Log in and registration page were designed to be simple, straight forward and welcoming.

<p float="left"><img src="/static/images/login.png" width="400">
<img src="/static/images/register.png" width="400">
</p>

##### *Tabs Page*
* Tabs page is simple in design and user friendly. From this page users can select a tab to view, create a new one, or delete an old.

<p align="center"><img src="/static/images/tabspage.png" width="400"></p>

<p align="center"><img src="/static/images/tabeditdelete.png" width="400"></p>

##### *Profile Pages*
* After selecting a tab to view, users are then redirected to that tabs profile page. Occupying the top half of the screen are three buttons that open different modals to log entries.
<p align="center"><img src="/static/images/profileview.png" width="400"></p>

* Each button and modal has a different theme based on the emotion behind the entry, happy, sad or angry.

<p float="left"><img src="/static/images/happyentry.png" width="250"  height="350">
<img src="/static/images/sadentry.png" width="250"  height="350">
<img src="/static/images/angryentry.png" width="250"  height="350"></p>

* After submitting an entry the user is then redirected to a monthly view of entries made for that tab. From this page they can edit entries, go back to the profile page or perform a search of all entries.

<p align="center"><img src="/static/images/monthly.png" width="400"></p>

* On the bottom half of the profile page is an interactive dashboard for users to view and search data, send emails to comunicate feelings or send a gift.

<p align="center"><img src="/static/images/profiledashboard.png" width="400"></p>

##### *Profile Page Dashboard*
* The relationship status element displays a heart which based off of the users data will grow darker with happy entries and the opacity will fade with angry or sad entries.

<p float="left">
<img src="/static/images/relationshipstatus2.png" width="250">
<img src="/static/images/relationshipstatus3.png" width="250">
<img src="/static/images/relationshipstatus.png" width="250">
</p>

* The search element allows users to search through that specific tabs entries. They can search by month, year, keyword, or emotion they chose when they made the entry. Happy, sad, or angry.

<p align="center"><img src="/static/images/search.png" width="400"></p>

* The scoreboard (also featured on the home page) breaks down all entries made for that tab into three categories, happy, sad, and angry.

<p align="center"><img src="/static/images/scoreboard.png" width="400"></p>

* The EmailJS API was used for the email element. In efforts to encourage open communication and sharing feelings, this feature allows users to send a quick message directly from each tab.

<p align="center"><img src="/static/images/giftemail.png" width="400"></p>

* To provide a way for users to send a quick thank you or a nice reward for a job well done I created the gift box. Featured on the site is a link to send a Starbucks gift card but multiple gifts can be offered to give users options.

##### *Search Results Page*

* After entering an entry search from the profile page, the user is redirected to the results page where all their search results will be displayed. Each result showcases all the details entered and also gives the user an opportunity to edit the description of each entry.

<p float="left"><img src="/static/images/searchresults.png" width="500" height="400">
<img src="/static/images/editentry.png" width="300" height="400">
</p>


* On the top of the results page is an input field for users to perform a different search. there is also a link to return back to the profile page they started the search from.

<p align="center"><img src="/static/images/resultspage.png" width="400"></p>

* For mobile users the results will conveniently be displayed in an accordion to help prevent excessive scrolling.

<p align="center"><img src="/static/images/resultsmobile.png" height="500"></p>

##### *Error Pages*

* For a for a complete user experience, custom error pages have been created to handle 404 and 500 errors.
<p align="center"><img src="/static/images/404.png" width="400"></p>

### Wireframes
* All wireframes can be found [HERE.](https://github.com/RyanRayn/Milestone-3/tree/master/documents/wireframes)

***

## **Features**

* Responsive on all devices.
* Functioning EmailJS API.

***

## **Technologies Used**

### Languages Used
* HTML5
* CSS3
* JavaScript
* jQuery
* Python
* MongoDB
* Flask
* Jinja

### Frameworks, Libraries & Programs Used
1. [Bootstrap 4.5.0:](https://getbootstrap.com/) 
    * Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/) 
    * Google fonts were used to import the "Kanit" font into the style.css file which is used on all pages throughout the project.
3. [Font Awesome:](https://fontawesome.com/)
    * Font Awesome was used on all pages throughout the website to add icons for UX purposes.
4. [jQuery 3.5.1:](https://code.jquery.com/)
    * jQuery was use multiple time throughout this project.
5. [JavaScript 4.5.2:](https://getbootstrap.com/docs/4.0/getting-started/javascript/) 
    * JavaScript was used multiple times, most notably with the EmailJS API and other email functions. JavaScript was also used to get and display current dates.
6. [EmailJS](https://www.emailjs.com/) 
    * The EmailJS API was used for the profile email form.
7. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * The Flask framework was used throughout this entire project.
8. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * Jinja templating language was used throughout this project to pass data into html templates.  
8. [Git:](https://git-scm.com/)
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to Github.
9. [GitHub:](https://github.com/)  
    * GitHub is used to store the project code after being pushed from Git.
10. [Balsamiq:](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes during the design process. 

***

## **Testing**

* The W3C Markup Validator, W3C CSS Validator Services, PEP8 online and JS Hint were used to validate every page of the project to ensure there were no syntax errors in the project.

* All testing validation can be seen [HERE.](https://github.com/RyanRayn/Milestone-3/tree/master/documents/testing) 

### Testing User Stories from UX Section
**First Time Visitor Goals**
1. As a first time user, I would like to easily understand the purpose of the site.
    * Upon entering, users are greeted with an eye-grabbing headline stating exactly what the sites purpose is.

    * The icons to the right of the header supports the sites purpose with emoticons of different feelings.

    * The bottom half of the homepage is a breakdown of the features offered with icons and descriptions. 

   <p align="center"><img src="/static/images/desktophome.png" width="400"></p>
  
2. As a first time user, I would like to easily navigate through the site's content.

    * After logging in or registering on the site, the user has several options. On mobile screens there is a hamburger icon in the right corner offering links to the other pages as well as buttons stratigically placed on the homepage for easier navigation. 
   
    On the desktop view there is a dropdown with alphabetized links to all the users tabs for quick access as well as multiple buttons placed in the navbar and throught the pages. 

   <p align="center"><img src="/static/images/mobilehamburger.png" width="400"></p>

3. As a first time user, I would like to easily understand all the data presented to me.

    * Font Awesome icons were used throughout this site to present data in the simplest way possible. This was done for easability and to make the site user friendly. 

    <p align="center"><img src="/static/images/scoreboard.png" width="400"></p>

4. As a first time user, I would like to easily understand how the all site's functions work.

    * Keeping Tabs was designed for ease of use. Lots of icons were used for buttons and short, detailed instructions were stratigically placed to make functions easy to understand. 

**Frequent Visitors**

1. As a frequent visitor, I would like to regularly see new relationship tips.

    * After logging in, a "Welcome Back" message is displayed with a relationship tip. This message can be changed after a period of time or even rotated through with other tips so there is something new to read every time the user logs in.

2. As a frequent visitor, I would like new gifts on offer to send to people.

    * In this version there is a link for a Starbucks gift card. In future versions I planned to use this feature as a way to monetize the site and offer multiple gifts on a commission basis.

### Further Testing

* The website was tested on Safari, Google Chrome, and Firefox browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPad, iPhone 8, iPhone X, and Samsung devices.
* All the links on every page were tested on all browsers to ensure they are working properly.
* Friends and family members were recruited to play on the site and inform me of any changes they felt needed to be made.

***

## **Deployment**

### Project Creation
To create this project I used the CI Gitpod Full Template by navigating 
[here](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking the 'Use this template' button.

I was then directed to the create new repository from template page and entered in my desired repo name, then 
clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

The following commands were used for version control throughout the project:

* git add *filename* - This command was used to add files to the staging area before committing.

* git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

* git push - This command is used to push all committed changes to the GitHub repository.


### Deployment to Heroku

**Create application:**
1. Navigate to Heroku.com and login.
1. Click on the new button.
1. Select create new app.
1. Enter the app name.
1. Select region.

**Set up connection to Github Repository:**

1. Click the deploy tab and select GitHub - Connect to GitHub.
1. A prompt to find a github repository to connect to will then be displayed.
1. Enter the repository name for the project and click search.
1. Once the repo has been found, click the connect button.

**Set environment variables:**

Click the settings tab and then click the Reveal Confid Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (database name you want to connect to)
4. key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and 
    dbname that you set up in the link).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).

**Enable automatic deployment:**
1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

***

## **Credits**

### Code

* [Bootstrap 4.5.0](https://getbootstrap.com/) and [Bootstrap Flex:](https://getbootstrap.com/docs/4.0/utilities/flex/) The Bootstrap libraries were used throughout the project mainly to make the site responsive using the Bootstrap Grid System.

* [Stack Overflow:](https://stackoverflow.com/) Stack was used as coding support throughout the entire project.

* Aaron Sinnot (Mentor): My mentor Aaron Sinnot helped with some of the code for MongoDB.

* [W3schools.com:](https://www.w3schools.com/) W3 was a great resource for random rules and code while working on this project.


### Content

* All content was written by the developer.

### Media

* All icons for this project were found using [Font Awesome.](https://www.fontawesome.com/)

### Acknowledgements 

* As always... My amazing mentor, Aaron Sinnot for his continuous feedback and support.

* Tutor support at Code Institute for all their efforts, helpfulness, and friendliness.