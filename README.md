<p align="center"><img src="/static/images/mockup.png" width="400"></p>


# **Keeping TABS**
View the live project [HERE.](https://keeping-tabs-ryan.herokuapp.com/)

***

## **Introduction**

Keeping Tabs is a platform that allows users to keep records of all their personal interactions. Searchable entries for each relationship are organized into three categories, happy, sad and angry, and then statistics giving an idea of relationship health are displayed on a profile dashboard. In efforts to encourage keeping lines of communication open, the user can send an email expressing their feelings directly from each profile page. Users can also send a "thank you" gift, in this example, it is a Starbucks gift card. Keeping Tabs is not only about keeping track of bad things people do to you but also bringing to light all the positive moments that can sometimes be overlooked.   

***

## **Table Of Contents**

 
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
* Tabs page is simple in design and user friendly. From this page users can select a tab to view, create a new one or delete an old.

<p align="center"><img src="/static/images/tabspage.png" width="400"></p>

<p align="center"><img src="/static/images/tabeditdelete.png" width="400"></p>

##### *Profile Pages*
* After selecting a tab to view, users are then redirected to that tabs profile page. Occupying the top half of the screen are three buttons that open different modals to log entries.
<p align="center"><img src="/static/images/profileview.png" width="400"></p>

* Each button and modal has a different theme based on the emotion behind the entry, happy, sad or angry.

<p float="left"><img src="/static/images/happyentry.png" width="400">
<img src="/static/images/sadentry.png" width="400">
<img src="/static/images/angryentry.png" width="400"></p>

* On the bottom half of the profile page is an interactive dashboard for users to view and search data, send emails to comunicate feelings or send a gift.

<p align="center"><img src="/static/images/profiledashboard.png" width="400"></p>

##### *Profile Page Dashboard*
* The relationship status element displays a heart which based off of the users data will grow darker with happy entries and the opacity will fade with angry or sad entries.

<p float="left">
<img src="/static/images/relationshipstatus2.png" width="250">
<img src="/static/images/relationshipstatus3.png" width="250">
<img src="/static/images/relationshipstatus.png" width="250">
</p>

* The search element allows users to search through that specific tabs entries. They can search by month, year, keyword or emotion they chose when they made the entry, happy, sad or angry.

* The scoreboard (also featured on the home page) breaks down all entries made for that tab into three categories, happy, sad and angry.

<p align="center"><img src="/static/images/scoreboard.png" width="400"></p>

* The EmailJS API was used for the email element. In efforts to encourage open communication and sharing feelings, this feature allows users to send a quick message directly from each tab.

<p align="center"><img src="/static/images/giftemail.png" width="400"></p>

* To provide a way for users to send a quick thank you or a nice reward for a job well done I created the gift box. Featured on the site is a link to send a Starbucks gift card but multiple gifts can be offered to give users options.

##### *Search Results Page*

* After entering an entry search from the profile page, the user is redirected to the results page where all their search results will be displayed. Each result showcases all the details entered and also gives the user an opportunity to edit the description of each entry.

<p float="left"><img src="/static/images/searchresults.png" width="400">
<img src="/static/images/editentry.png" width="400">
</p>


* On the top of the results page is an input field for users to perform a different search also a link to return back to the profile page they started the search from.

<p align="center"><img src="/static/images/resultspage.png" width="400"></p>

* For mobile users the results will conveniently be displayed in an accordion to help prevent excessive scrolling.

<p align="center"><img src="/static/images/resultsmobile.png" height="500"></p>

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
   * Upon entering, users are greeted with an eye-grabbing hero image of a skier on a mountain. To the left of the skier is a large header and subheader with the name of the site and a one-line description explaining the purpose of the site.

   * The background image of the skier immediately lets the user know the website has to do with skiing/snow sports.

   * The header and subheading next to the skier tell the exact purpose of the site.
   <p align="center"><img src="/assets/images/desktop2.png" width="400"></p> 
  
2. As a first time user, I would like to easily navigate through the site's content.

   * When arriving at the site, the user has several options. In the top corner is a hamburger menu icon that navigates around the site.

   * In the bottom corner of the hero image is a strategically placed call to action link that will bring visitors to the maps page.

   * Users can also scroll down for more content and another large button that will bring them to the information page to find out more.

   * Each page has a dropdown menu that navigates the site in the same convenient location.

   * Due to the length of the info page, I have placed a "scroll to top" button that will automatically bring you to the top menu when pressed.

   * A button leading to the maps page has also been placed at the bottom of the info page for easy access.
   <p align="center"><img src="/assets/images/navigation.png" width="400"></p>

3. As a first time user, I would like to easily access the website for each resort and season pass for more information.

   * On the maps page, each location has an infobox connected to its marker when clicked. The marker contains a link to that resort's website.
   <p align="center"><img src="/assets/images/infobox.png" width="400"></p>

   * On desktop view, when a passes locations are shown on the map a container pops up underneath with a list of all resorts that pass offers. Each line item is an active link to that mountain's website.
   <p align="center"><img src="/assets/images/resortlinks.png" width="400"></p>

   * On the information comparison page, an active link has been placed on each mountain name every time it is mentioned.

**Returning Visitors**

1. As a returning visitor, I would like to see up to date information on mountains and prices.
   * In the footer of each page are links to our social media accounts as well as a callout to follow us for up to date information and sales.

**Frequent Visitors**

1. As a frequent visitor, I would like easy access to the site's social media accounts.
   * Icons that link to our social media accounts are placed in the footer of each page as well as in the dropdown menu for constant reminders to follow.

2. As a frequent visitor, I would like social media accounts to be up to date with current promotions.
   * Social media accounts will be continuously updated with new information and sales.

### Further Testing

* The website was tested on Safari, Google Chrome, and Firefox browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPad, iPhone 8, iPhone X, and Samsung devices.
* All the links on every page were tested on all browsers to ensure they are working properly.
* Friends and family members were recruited to play on the site and inform me of any changes they felt needed to be made.

***

## **Deployment**


***

## **Credits**

### Code

* [Bootstrap 4.5.0](https://getbootstrap.com/) and [Bootstrap Flex:](https://getbootstrap.com/docs/4.0/utilities/flex/) The Bootstrap libraries were used throughout the project mainly to make the site responsive using the Bootstrap Grid System.

* [Stack Overflow:](https://stackoverflow.com/) Stack was used as coding support throughout the entire project.

### Content

* All content was written by the developer.

### Media

* All icons for this project were found using [Font Awesome.](https://www.fontawesome.com/)

### Acknowledgements 
