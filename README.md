# Dukan
this in my eyantra hackathon project hosting on python anywhere
URL::<  "vsvai.github.io"  >,<  "vsvai.pythonanywhere.com"  >
This is the documentation with reference to the Web Based Application DUKAN.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DESCRIPTION
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This Documentation Provides All the necessary Inforamation about the COVID-19.

The Government of India  have posed a lockdown in the entire country to reduce the spread of the deadly virus novel COVID-19. Social Distancing has been suggested and is considered to be the key to minimise its effect on the society. However, it has not been implemented to its full stretch as purchase of daily essential goods is still being carried out and it cannot be avoided. Long queues are visible outside stores of essential goods and products, people do try 
to maintain gaps while in the line but that doesn’t really help. Many people have hoarded goods in their houses leading to shortage for the others who didn’t get enough time to do so. Some even started stocking goods before the lockdown was announced.
A lot of times people have returned home due to the unavailability of goods. 
To reduce the number of people on road and to support the government’s suggestion of social distancing  we have come up with a web based solution which would help in easy  purchase of goods without much hassle and this will also make sure that the people don’t get out of their houses unnecessarily.

The name of our project is : DUKAN

Dukan comes with features like :- 
1. Knowing beforehand whether the required commodity is available at a particular shop.
2. Making an appointment with the shopkeeper to collect their respective goods to avoid waiting in long queues which’ll result in keeping up with the concept of social distancing.
3. This site will provide latest and important  updates and news about the COVID-19 epidemic and it’ll always have the measures listed that can be taken to avoid it.
4. All the stores will register themselves on this site giving all the necessary details like : shopkeepers number, email, name of store, address of store, and the type of store.
5. Customers can easily search for a particular stores and warehouses  and then place an order which will be confirmed by the shopkeeper only if the items are available (only important items will be available.)
6. Customers will be given a time interval during which they can collect their goods .
7. Contact details of both: the customer and shopkeeper,  will be available to ease the communication between the two and this site also promises the security of data with an easy to use interface.

This will make selling and buying essential goods and services easier in this situation of a global pandemic. As citizens of this country it is our responsibility to look for ways that can make this situation less chaotic than what it already is. We should practice social distancing and stay inside as much as possible and also keep suggesting others to do the same because it is not just one person’s job to follow the suggestions and decisions of the government.Even after the pandemic this site can be used for everyday purchases as this saves time of the buyer along the seller. This is a time efficient process of buying and selling essential goods. 


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
HARDWARE AND SOFTWARE REQUIREMNETS
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. 
2.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PROCESS FLOW
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Users will be directed to the Home page , where he/she can latest update on COVID-19 and some helpful informataions regarding it.
Then he/she can go to the Shops page where he can select nearby shop and place order regarding his necessities. He/she can contact with the shop owner personal . He has to provide all the necessary details asked.
He can also see the helpline numbers in the Contact tab .

The Project contains:

App Folder which contains templates.

Templates contain the basic Html pages of the project.

Also App folder contains many python file such as forms.py, models.py, shops.db, tests.py, views.py .

Forms.py contains authentication forms.
Models.py contains django models for connecting with sqlite database.
shops.db is the database.
views.py contains the functions for all the url connected pages.

More in project is the urls.py file which contains all the urls pages.
Next there are some databases.
Important databases are:
shops.db
register table for all the shops.
customer table to store the database for customers.
Booking tableo j   for all the bookings made by customers to the shops.

Customer Reference.

Customers can upload  an image given by the doctors for the medicines.
Also they can pickup the appointment time on the shops website.

All things are made easy to use for the customers by keeping customers perspective in the mind also .
There will not be any data damage,leakage.

![Dataflowdiagram.JPG](Dukan/Dataflowdiagram.jpg)
