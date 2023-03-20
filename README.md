# Mama’s Kitchen

## Introduction

Welcome to Mama’s Kitchen. A small, family-friendly restaurant in the centre of Wexford town, Ireland. 

Able to host up to 40 customers at a time, it is open from 2pm - 9pm each day and takes bookings right up until 8pm. Mama’s Kitchen needs a booking engine that will give customers full control over editing or cancelling their bookings and they want no more than 40 customers booked per hour. 

They’d also like to give customers the opportunity to leave reviews and be able to respond to them to say thanks. 

This project was developed with Agile development principles in mind. Through incremental and iterative programming, this python web application gives both users and administrative staff the ability to create, edit or cancel restaurant bookings and reviews. Administrative staff also have the ability to reply to reviews. 

Using the django framework on the back end with Bootstrap design, it is both fully functional and user-friendly. 

The link to the live website can be found here: [Mama’s Kitchen](https://mamaskitchen.herokuapp.com/).

## Table of Contents

* [Agile Development](#agile-development)
    * [User Stories](#user-stories)
    * [Technologies Used](#technologies-used)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [Features](#features)
    * [Admin Experience](#admin-experience)
    * [Customer Experience](#customer-experience)
    * [Booking App](#booking-app)
    * [Review App](#review-app)
    * [Gallery](#gallery)
    * [Contact form](#contact-form)
* [Testing](#testing)
* [Errors & Bugs](#errors)
* [Unfixed Bugs](#unfixed-bugs)
* [Future Features](#future-features)
* [Validator Testing](#validator-testing)
* [PageSpeed Insights](#pagespeed-insights)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Media](#media)
    * [Reference Material](#reference-material)
    * [Other Code](#other-code)
    * [Acknowledgements](#acknowledgements)
   

## Agile Development

Agile methodology is focused on flexibility, collaboration, and rapid iteration. Its principles include working collaboratively with clients to understand their needs, breaking down work into small pieces that can be completed quickly, and being open to change throughout the development process.

This project was built following Agile development principles. I started by identifying the client's needs and breaking down the work into small, manageable pieces that could be completed in short iterations.

## User Stories

The following requirements were determined based on User Stories that can be found on our project board - [Mama’s Kitchen](https://github.com/users/Roybin0/projects/4/views/1)

* Customers need to be able to book a table on a future date of their choice. 
* Customers need the ability to access their booking, edit details such as date, time or party size and cancel the booking completely if necessary. 
* Customers need the ability to leave reviews online.
* Administrative staff need the ability to add, edit and cancel bookings from a secure admin area. 
* Administrative staff need the ability to reply to reviews, or delete where inappropriate language is used. 


## Technologies Used

HTML, Bootstrap CSS, Javascript, Python+Django, Postgres.
   
## Scope

* Website features
    * Responsive design for multiple screen sizes
    * Visually pleasing and clear structure
    * Booking app 
    * Review app
	* Gallery of images
	* Admin site
    
    <br>
   
* Content features
    * Accessible
	* Downloadable menus
	* View and access bookings
   
## Structure

* Clear layout with intuitive navigation and fully responsive design thanks to Bootstrap. 
* Colours, fonts and images are accessible for all users.
* Navigation and footer on every page. 
* Booking pages allow for creating, editing and cancelling bookings.
* Reviews page allows for creating reviews. 
* Responsive gallery to showcase meals. 
* The admin site allows Admin users to create, edit or delete bookings and reviews. It also allow Admin users to upload new images to the gallery. 

## Skeleton

Figma was used to create wireframes of the initial website design and customer booking and review flows. The full wireframe can be viewed [here](https://www.figma.com/file/CcXjARl3FEmeH39ts1r9Ia/Mama's-Kitchen?node-id=0%3A1&t=KeBQEVR6kLYJsAum-1).

## Surface 

* Colour scheme was chosen with accessibility in mind. 
* A single [Google Font](https://fonts.google.com/) is present throughout the website - Itim. It’s a fun, easy to read font. 

## Features

* The site is laid out over five main pages - Home, Menu, Bookings, Gallery and Reviews. It also offers pages for account sign-up, account log in/log out, contact and a privacy policy.
* Each page contains a header, navigation bar and footer. 
* The home page contains a brief "About Us" of Mama's Kitchen and a Google Map to easily locate the business.

## Admin Experience

The admin is a native django admin app that allows authenticated staff member to add bookings, edit or delete bookings and view, edit, delete or reply to reviews. 

## Customer Experience

The home page includes a hero image that fits nicely with the overall colour scheme of the website. It also has an About Us section and a Google Map for easy access to the restaurant location. 
![home page](https://github.com/Roybin0/mamaskitchen00/blob/main/static/images/homepage.png?raw=true)

Customers can view or download the Dining Menu and the Drinks Menu from the Menu tab. 

![menu page](https://github.com/Roybin0/mamaskitchen00/blob/main/static/images/menupage.png?raw=true)

## Booking App

The booking form has been created from the database model for Bookings. It includes a hidden field of booking reference which is generated immediately when a customer books a table. This is then sent to the customer in an email. 

![booking form](https://github.com/Roybin0/mamaskitchen00/blob/main/static/images/bookingpage.png?raw=true) 

## Review App

The review app allows customers to leave a review once they have signed into or signed up for an account.

## Gallery

The gallery contains a selection of images as example of the type of dishes that are on offer at Mama’s Kitchen. 

## Contact Form

The contact page gives customers details of phone and email and also offers a contact form for quick and easy submission. 

## Footer

The footer is found on every page and contains links to the Contact page, the Privacy Policy and social media pages. It also contains a copyright section. 

## Testing

### Content testing

The website content has been thoroughly tested using multiple devices (laptop, phone and tablets) on multiple browsers (Chrome, Safari and Firefox). 

* The links are navigating to the correct pages. 
* Login and logout is successful with the user being asked to confirm logout first. 
* The sign up page functions as expected. 
* Form submit buttons are expected to send, update or delete data from the database and are working as expected. 
* The gallery is fully responsive. 
* Reviews appear when the form is submitted and disappear when the user is deleted.

### App testing 

Python testing was applied via django’s built in Test module. You can find a list of tests in the links below: 

<b>Model testing</b>
	* [Booking model tests](https://github.com/Roybin0/mamaskitchen00/blob/main/bookings/test_models.py)

<b>View testing</b>
	* [Booking view tests](https://github.com/Roybin0/mamaskitchen00/blob/main/bookings/test_views.py)

<b>Form testing</b>
* [Booking form tests](https://github.com/Roybin0/mamaskitchen00/blob/main/bookings/test_forms.py)

## Errors & Bugs

* On deployment, emails would not send to customers booking a table. The issue was found to be with using a Gmail client. To resolve this, the email client was changed to Outlook. 


## Unfixed bugs

* On deployment, the URLs visible in the browser are showing incorrectly, even though the correct view is rendering. I have been unable to determine the cause of this and this is something I would like to investigate further. 
* Error raised during testing bookings.forms: ValueError: The empty_permitted and use_required_attribute arguments may not both be True. Cause has been determined to be an issue with Django forms. 
* Issues raised with collectstatic - See copy of [build log](https://docs.google.com/document/d/1V9y-PxtaA68VI3sfhwtnM-YMJgePwsC5_C3s5NXx4z4/edit?usp=sharing) - Needs full investigation.


## Future Features 

In future iterations, I would like to give customers the option to edit and/or delete their reviews entirely. Currently, this is only possible by Admin users. 

## Validator Testing

### Wave Web Accessibility 

[Home page](https://wave.webaim.org/report#/https://mamaskitchen.herokuapp.com/) - Some errors regarding missing links - these are the social media links which are placeholders. 
[Menu](https://wave.webaim.org/report#/https://mamaskitchen.herokuapp.com/menu) - Missing table headers which is expected
[Gallery](https://wave.webaim.org/report#/https://mamaskitchen.herokuapp.com/gallery/) - Alt text missing from images added via cloudinary
[Reviews](https://wave.webaim.org/report#/https://mamaskitchen.herokuapp.com/reviews/) - No unexpected errors
[Booking](https://wave.webaim.org/report#/https://mamaskitchen.herokuapp.com/booking/) - No unexpected errors

### HTML 

HTML was tested using the W3 Nu HTML Checker. No unexpected errors found. Reports are available for each main page: 

[Home page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmamaskitchen.herokuapp.com)
[Menu](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmamaskitchen.herokuapp.com%2Fmenu) 
[Gallery](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmamaskitchen.herokuapp.com%2Fgallery) - Flagged for missing alt text on images
[Reviews](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmamaskitchen.herokuapp.com%2Freviews) 
[Booking](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmamaskitchen.herokuapp.com%2Fbooking) 


### CSS 

CSS was tested using the W3C CSS Validation Service. No errors found:
 ![](https://github.com/Roybin0/mamaskitchen00/blob/main/static/images/cssvalid.png?raw=true)


## Mobile Friendly

The website passes Google’s Mobile Friendly test. Results [here](https://search.google.com/test/mobile-friendly/result?id=DxpRXA3QvV2lW_3bouCmkQ). 

## PageSpeed Insights

The lowest score is 52 for Best Practices. This is due to incorrect image aspect ratio and image sizing that could be reduced. This has been noted for future updates. 

## Deployment 

This project was deployed to Heroku.
Steps to deploy:

1. Clone this repository.
2. Create a new Heroku app.
3. Link the Heroku app to the repository.
4. Click Deploy.


## Credits 

## Media 

Images from iStock, Pexels, Unsplash and Getty Images.  

## Acknowledgements 

* Huge thanks are due to Nicholas & Jamie for the ongoing support
* John, Cara, Charlotte and Mario for endless testing and bug finding



