# Individual_Project
 Individual Project for Generation UK

# Project Background
My client has launched a pop-up cafe and is offering to deliver home-made lunches and refreshments to the surrounding offices. They requested for a piece of software that will help them log and track their orders.
# Client requirements
* They want to maintain a collection of products and couriers.
* When a customer makes a new order, they need to create this on the system
* They need to be able to update the status of an order i.e: preparing, out-for-delivery, delivered.
* When they exit the app, they need all data to be persisted and not lost.
* When they start the app, it needs to load all persisted data.
* They need to be sure my app has been tested and proved to work well.
* They need to receive regular software updates.
# How did your design go about meeting the project's requirements?
My application is able to add, update and delete persisting objects within a database. Upon opening and exiting the application the database is called to import and export data respectively. I have also made sure to periodically run the program and test all the functions and feature to iron out any bugs or issues.
I also sat down with the client (Instructor) and went over some of the specifics of the requirements, such as what data will be stored int "products", "couriers" and "orders"
# How did you guarantee the project's requirements?
I have tested the application by sending it to be reviewed by peers and doing group code reviews. On an earlier version of the project I had some unit testing however after a large change in the applications structure the tests became invalid.
# If you had more time, what is one thing you would improve upon?
Unit testing. I would like to add more unit testing to the application to make sure functions are working as intended.
# What did you most enjoy implementing?
It is difficult to choose a particular part of the project I enjoyed as it has overall been a fun problem solving task, However I would say I most enjoyed implementing the modules containing different functions. My application was initially all on a single file that resulted in me needing to scroll down to see code. Splitting that all up into different files meant that I could easily find what code I needed and made it easier for others to review.
