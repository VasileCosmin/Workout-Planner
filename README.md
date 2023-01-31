# Workout Planner

#### Video Demo:    
https://www.youtube.com/watch?v=Lzs-igBBdYE

#### Description:   
Welcome! This is a web app for planning your workout. First thing first, you have to register, then you will be redirected to the home page and get some instructions on how to use it. After, you can go read an article on the subject: why is good to workout (i got the text from: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/exercise/art-20048389). There is the exercises page, where you can select form a dropdown menu the muscle you want to work, after you select the muscle press the button and it will give you 10 exercises for the muscle you selected. Read the instructions and add the exercise that you like to your workout. After you added exercises go to the page called My Workout and you will see all the exercises you selected, you can remove any exercise you want. 
  app.py contains all the functions for the application. the login function, register, delete exercise, add exercise and all the templates for the html pages. And it contains the werkzeug functions genereate_password_hash and check_password_hash. It also imports cs50 sql and flask_session. The add function adds a new exercise in the database; the delete function deletes an exercise from the database; workout function returns the exercises from the database; index function returns index.html same for info function; exercises function gets the exercises corresponding to the select element; login function checks if the data inserted in the form is corresponding to the database and returns errors if the data is not good; register function adds a new user to the database and returns errors if fields are empty or passwords don't match; signout function clears the session and redirects to the login page.
  helpers.py contains the login_required function and get_exercise function that is calling the api and loads it into json.
  exercises.html contains the html code for the exercises page and javascript for the readmore button; index.html contais the homepage; info.html contains the text and elements for the why you should workout page. layout.html contains the layout of the page, the navigatoin and footer and the javascript for the navigation to become a little opaque and the functionality for the button of the mobile menu; login.html contains the login page data form and image for register; workout.html display all the exercises from the database that are corresponding to the user_id.
  styles.css contains all the styles for every html file.

#### Screenshots:
![Login Page](/screenshots/1.png)
![Register Page](/screenshots/2.png)
![Home Page](/screenshots/3.png)
![Why you should workout Page](/screenshots/4.png)
![[Why you should workout Page](/screenshots/5.png)
![Exercises Page](/screenshots/6.png)
![Selected muscle exercises Page](/screenshots/7.png)
![My wourkout Page](/screenshots/8.png)
![Mobile login Page](/screenshots/9.png)
![Mobile home Page](/screenshots/10.png)
![Mobile menu Page](/screenshots/11.png)
![Mobile exercises Page](/screenshots/12.png)
![MObile my workout Page](/screenshots/13.png)
