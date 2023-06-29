## Table Of Contents:
1. [Validator Testing](#vadilidator-testing)
    * [Html](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Lighthouse](#lighthouse)
2. [User Story Testing](#user-story-testing)
3. [Responsiveness Testing](#responsivness-testing)
4. [Manual Testing](#manual-testing)
5. [Bugs](#bugs)

## Validator Testing

### W3C HTML validator
The site pages were run through the [W3C validator](https://validator.w3.org/) to check for any issues and HTML syntax errors. 
Given the presence of Django template code in the HTML templates, the rendered HTML was copied from the Chrome browser by right clicking, selecting 'view page source' for each page of the site and then pasting directly into the HTML validator.
No errors or warnings were to be found.

![W3C HTML](readme-docs/images/w3c-html.png)

### CSS
- The CSS stylesheet was put through the [W3C validator](https://jigsaw.w3.org/css-validator/)  to check for errors.
- No errors were to be found.

![W3C CSS](readme-docs/images/w3c-css.png)  

### JavaScript
- The Javascript file was put through the [Jshint](https://jshint.com/) to check for errors. 
- No errors were to be found.

![JS Validator screenshot](readme-docs/images/jshint.png)

### Python

### Python
- Issues with the custom python code were fixed on an ongoing basis during development using the pycodestyle tool, which was installed to the IDE, GitPod.  
- The code was also tested to check for errors using **Code Institutes pep8 online** website, [PEP8](https://pep8ci.herokuapp.com/). No errors returned as you can see from the screenshots below.

#### Blog App

<details>
    <summary>admin.py</summary>  
    
![Admin PEP8 validator](readme-docs/images/admin-pep8.png)  
</details>
  
<details>
    <summary>forms.py</summary>  
    
![Forms PEP8 validator](readme-docs/images/forms-pep8.png)  
</details>  

<details>
    <summary>models.py</summary>  
    
![Models PEP8 validator](readme-docs/images/models-pep8.png)
</details>  
  
<details>
    <summary>urls.py</summary>  
    
![Urls PEP8 validator](readme-docs/images/urls-pep8.png)
</details>  

<details>
    <summary>views.py</summary>  
    
![Views PEP8 validator](readme-docs/images/views-pep8.png)
</details>  

[Back to the top](#table-of-contents)
- - - 


### Lighthouse

Lighthouse in chrome dev tools was used to generate a report that tests the sites for **Performance**, **Accessibility**, **Best Practices** and **Seo**. 

<details>
    <summary>Home</summary>  
    
![Home Lighthouse Test](readme-docs/images/home-lighthouse.png)
</details>

<details>
    <summary>Recipes</summary>  
    
![Recipes Lighthouse Test](readme-docs/images/recipes-lighthouse.png)
</details>

<details>
    <summary>Add Recipe</summary>  
    
![Add Recipes Lighthouse Test](readme-docs/images/add-recipe-lighthouse.png)
</details>

<details>
    <summary>Register</summary>  
    
![Register Lighthouse Test](readme-docs/images/register-lighthouse.png)
</details>

<details>
    <summary>Login</summary>  
    
![Login Lighthouse Test](readme-docs/images/signin-lighthouse.png)
</details>

<details>
    <summary>Logout</summary>  
    
![Logout Lighthouse Test](readme-docs/images/signout-lighthouse.png)
</details>

---
[Back to the top](#table-of-contents)


## User Story Testing
---
[Back to the top](#table-of-contents)


## Responsiveness Testing

The responsive design tests were carried out manually throughout the build using Google Chrome Dev Tools. As this is primarily a browser based platform I based the main design around a desktop view, adding responsive design for tablet and mobile devices as well. 

During the testing process I also used the [Responsive Design Checker](https://www.responsivedesignchecker.com/) website to simulate the website on several other devices. Here are my findings:

### Mobile Devices

||<p>iPhone 6/6s/7</p><p>375 x 667</p>|<p>Samsung Galaxy S5/6/7</p><p>360 x 640</p>|<p>Google Pixel/Nexus 5</p><p>411 x 731</p>|
| :- | :-: | :-: | :-: |
|Render|Pass |Pass|Pass|
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

### Tablet Devices

||<p>Amazon Kindle Fire</p><p>768 x 1024</p>|<p>Samsung Galaxy Tab 10</p><p>800 x 1280</p>|<p>Apple iPad Pro</p><p>1366 x 1024</p><p></p>|
| :- | :-: | :-: | :-: |
|Render|Pass|Pass|Pass |
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

### Desktop Devices

||<p>24“ Desktop</p><p>1920 x 1200</p>|<p>19” Desktop</p><p>1440 x 900</p>|<p>10” Notebook</p><p>1024 x 600</p>|
| :- | :-: | :-: | :-: |
|Render|Pass|Pass|Pass|
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

### Browser Compatibility 

Happening was tested on the following browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

Appearance and functionality appear to be consistent throughout all browsers. The site loads correctly on Firefox but it doesn't seem to be able to connect with the backend API and get the data. This is something I need to look at for the future to make sure that Firefox users can view my site properly.

---
[Back to the top](#table-of-contents)

