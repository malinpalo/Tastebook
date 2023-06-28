# Tastebook

![Am i responsive image](readme-docs/images/responsive.png)

[Live Site](https://8000-malinpalo-tastebook-w4zdo3wqn0p.ws-eu94.gitpod.io/) 

## Table Of Contents:
1. [Project Goals](#project-goals)
    * [CRUD functionality](#crud-functionality)
2. [UX Design](#ux-design)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)    
3. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [footer](#footer)
    * [Home Page](#home-page)
    * [Recipes Page](#recipes-page)
    * [Recipe Details](#recipe-details)
    * [Add Recipe Page](#add-recipe-page)
    * [Edit Recipe Page](#edit-recipe-page)
    * [Delete Recipe Page](#delete-recipe)
    * [Edit Comment Page](#edit-comment-page)
    * [Register Page](#register-page)
    * [Login Page](#login-page)
    * [Logout Page](#logout-page)

4. [Future Features](#future-features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

## Project Goals
Tastebook is a website built using the Django Full Stack framework for my Portfolio Project 4. Tastebook allows users to view and share their favourite recipes of food and drinks. Users are able to comment underneath recipes and like them. Users can also delete and edit their own recipes and comments. Users need to be logged in to get the full functionality of the site.

### CRUD functionality

Tastebook features a data store with full Create, Read, Update and Delete functionality.

- Create - users can create a user account, and authenticated users can create a profile, collaboration requests and messages to their approved collaborators.
- Read - users can view the profiles and posts of other users. Authenticated users can read messages sent to them.
- Update - authenticated users can update their profiles and save the changes. They can approve collaboration requests sent to them wich results in a new many-to-many relationship in the database.
- Delete - authenticated users can delete their profile and pending collaboration requests, chosing to cancelling, rejecting or approving them. Authenticated users can also delete messages sent by or to them, the message is not deleted from the database until both the sending and receiving users have marked them as deleted.

## UX Design:

### Wireframes
Wireframes that where created in [Balsamiq](https://balsamiq.com/) for this project are displayed below. The wireframes were  created in the planning phase of the project. Please note that the wireframes might not be exactly a copy of the project due to the fact that the site has changed during development.

![Wireframes](readme-docs/images/wireframes.png)

### User Stories
Users stories were implemented one by one after the firts planning phase. The wireframes created became the base for the User stories. 

Individual user stories were categorised according to whether they had to be implemented to produce a Minimum Viable Product (MVP), with priority for development to be given to those that were part of the MVP specification. 

The user stories that where created can be found [here](https://github.com/users/malinpalo/projects/9) and are added below.

### Agile Methodology
GitHub issues, milestones and projects were used to document and track an agile development approach.
An issue was created for each user story. These were labelled as 'MVP' if they were part of the MVP spec. All user stories were then added to a 'Product Backlog' milestone  [Link to product backlog]().

Development was divided into iterations with a timebox of four working days, each with a total value of 16 story points. The duration in calendar days was variable during development, due to fitting the four working days around work and other commitments. A milestone and a GitHub project board (a Kanban board) were created for each iteration, and user stories moved from the Product Backlog and into iterations as each cycle of work began. They were labelled as 'must have', 'could have' or 'should have' goals for the iteration, and assigned story point values. Story points for 'must have' user stories never exceeded 9 (60%).

A project Kanban board was used to track progress, with user stories moved between 'Todo', 'In Progress' and 'Done' columns as appropriate. For example, the iteration 3 project board was captured near the start, mid-way through the iteration and at the end:

![Kanban in progress]()

There was consideable uncertainty as to how many story point to allocate to each task. Therefor the first iteration had tasks exceeding 16 storie points in total. Tasks that didn't finish in time where to be moved in to the next iteration.

### Typography

### Colour Scheme

![Colour](readme-docs/images/colours.png)

### Database Diagram

![ERD](readme-docs/images/diagram.png)

## Testing

### Lighthouse

* This is the read from lighthouse:

![image](static/images/testhomepage.png)


### Validator testing

* I tested it through the python validator and no errors were shown. Everything works perfectly. 
*  All the code has been run through the W3C html validator, the W3C CSS validator and the JavaScript JSHint validator. The code passed the W3C Validator barring all the django template tags. No errors where found.

* All code passed through the pep8-validator came out clean, looking like this:

![Pep8-validator](static/images/pep8views.png)

## Technologies 

* [GitHub](https://github.com/) - to host the repositories.
* [Gitpod](https://www.gitpod.io/) - as the IDE for the application.
* [Elephantsql](https://www.elephantsql.com/) - for the postgresql
* [Python](https://docs.python.org/3/contents.html) - primary language of the application.
* [HTML](https://www.w3schools.com/html/) - Structure/skeleton of the page
* [CSS](https://www.w3schools.com/css/) - extra styling of the webpage
* [Javascript](https://www.w3schools.com/js/) - the apply some extra button functions that I wanted
* [Stack overflow](https://stackoverflow.com/) - basic explaining 
* [Bootstrap 5](https://www.w3schools.com/bootstrap5/bootstrap_get_started.php) - for design and placement
* [PEP8](http://pep8online.com/) - for testing and validating the code.
* [Google Fonts](https://fonts.google.com/about) - for the font of the text