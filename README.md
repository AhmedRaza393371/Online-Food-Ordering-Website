
# Welcome to Online Food Ordering Website:

## Introduction:

The Online Food Ordering System is a web application that allows users to order food from local restaurants. Users can selct food and drink items, place orders. The system includes user authentication, order management, and the user Information is stored in SQL Server Management Studio.

<img width="926" alt="pic1" src="https://github.com/AhmedRaza393371/Online-Food-Ordering-Website/assets/145160224/721188dd-a82c-44e1-9c86-7df969783298">
<img width="934" alt="pic2" src="https://github.com/AhmedRaza393371/Online-Food-Ordering-Website/assets/145160224/e0b9c3ec-c6f7-4a3e-895a-2745dc65aefd">
<img width="928" alt="pic3" src="https://github.com/AhmedRaza393371/Online-Food-Ordering-Website/assets/145160224/927f514a-3baf-480a-a661-3442fb340766">
<img width="935" alt="pic4" src="https://github.com/AhmedRaza393371/Online-Food-Ordering-Website/assets/145160224/9c10db3b-301e-49cc-a2ea-642d4883c8ce">


## Contents:

- [Introduction](#introduction)
- [Contents](#contents)
- [Website Structure](#website-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Website Structure:

The website is divided into three main parts: the Front-end , the Back-end and the database for storing registered user Information. 


### Front-end
The front-end of the application is built using modern web technologies to ensure a responsive and intuitive user experience.

- **Technologies Used**: HTML, CSS, JavaScript 
- **Components**:
- **User Registeration**: Allows users to register themselves in food ordering website.
  - **Homepage**: The landing page with an overview of the application and featured restaurants.
  - **Menu Page**: Displays a list of food items categorized by type.
  - **Cart Page**: Shows items added to the cart, allowing users to update quantities or remove items.
  - **About Us Page**: This page contains the restaurant Information and details
  - **Customer's Review**: This page contains the Customer's review and their ratings to the restaurants service and foods.


### Back-end
The back-end is responsible for handling business logic and database interactions.

- **Technologies Used**:  Python (Django)
- **Components**:
  - **API Endpoints**: Handle requests for user authentication, menu management, order processing.
  - **Database**: Stores user information, menu items, orders, and order's details.
  - **Authentication**: Manages user sign-up, login, and authorization using hashed passwords.





### Database
The user database is stored along with restaurants food and drinks items. The user order and their details is also entertained

- **Technologies Used**:  MsSQL 
- **Components**:
  - **User Table**: it contains user name,age,gender and password for account registeration.
  - **Product Table**: It contains the details about each Product like their name,pricing and image paths.
  - **Order Table**: It contains the user Id and the total user purchase and order id.
  - **Order Details table**: It contains the order ID and Product ID and Product's quantities.


### Business Logic
The core idea behind the storing database is to claulate the restaurant's revenue generated in given days.
  - **Employee table**: Employee Table conatins its details along with its salary. 
  - **Revenue Calculation**: The profit from the Product and the Employee salary was used to Calculate the total revenue generated.
  
  ### Entity-Relationship Diagram
  palce pics here


## Usage
Follow these steps to set up and run the online food ordering system locally.

### Prerequisites
- **HTML** and **CSS** and **JavaScript** (for front-end)
- **Python** and **Django** (for Python back-end)
- **Database Server** (MsSQL)

### Demo Video

   
   
## Contributing:

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-content`).
3. Make your changes and commit them (`git commit -am 'Add new content'`).
4. Push to the branch (`git push origin feature/new-content`).
5. Create a new Pull Request.

## License:

This project is licensed under the [MIT License](LICENSE).

