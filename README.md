# ShopRight

**Tagline**: *Shop smart, save big.*

## Overview

**ShopRight** is a simple and efficient web application designed to help users create and manage shopping to-do lists, making shopping experiences more organized and cost-effective. With ShopRight, users can:
- Create and update shopping to-do lists.
- Add items to their shopping basket along with prices.
- Automatically tally up the total cost of items as they are added to the basket.

This project is built using **Flask** for the backend, **Bootstrap** for styling, and **HTML, CSS, and JavaScript** for the frontend to provide a seamless user experience.

---

## Table of Contents
1. [Features](#features)
2. [Demo](#demo)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- **Shopping To-Do List:** Create, edit, and delete shopping lists on the go.
- **Live Shopping Basket:** Add items to a shopping basket with prices and see the total amount dynamically updated.
- **Mobile Friendly:** The app is responsive and can be used easily on mobile devices.
- **Item Search:** Search for items in your list quickly.
- **Cost Management:** Keep track of your shopping budget with a real-time tally of costs.

---

## Demo

A live demo of ShopRight is available at https://shopright.deanovo.tech/. Feel free to clone the repository and run the app locally using the [Installation](#installation) instructions below.

---

## Installation

To get started with ShopRight, follow these steps:

### 1. Clone the repository

```
git clone https://github.com/deanrobin333/shopright.git
cd shopright
```

### 2. Create a virtual environment (NECESSARY)
```
python3 -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
```

### 3. Install the required dependencies
`pip install -r requirements.txt`

### 4. Set up environment variables (VERY IMPORTANT)
Create a `.env` file in the root directory and add any necessary environment variables, and specify database
- Example -
    ```
    MONGO_URI=mongodb://localhost:27017/mydb
    SECRET_KEY='some random jumbled text'
    ```

    - replace "some random jumbled text" with your own jumbled text.

### 5. Run the application
- `flask run`
- To run the app using flask
    - In your project app, using your python environment
    - `python3 ./app.py`
- To run the app using gunicorn
    - In your project app `gunicorn -b server_ip_address:port_number -w 4 app:app`
        - If on server -- `<server_ip_address>:<port_number>`
    - if you are running on local host - `gunicorn -b localhost:8000 -w 4 app:app`

### 6. Open in your browser
Once the server is running, open your browser and go to:
`http://127.0.0.1:5000`


## Usage
- After starting the application, users can:

    - Create a new shopping to-do list by adding items and descriptions.
    - Add items to a live shopping basket with associated prices.
    - View the total cost as items are added.
    - Manage the list by marking items as bought or deleting them.

## Technologies Used

- **Backend**: Flask (Python), Gunicorn Server
- **Frontend**: Bootstrap, HTML5, CSS3, JavaScript
- **Database**: MongoDB (easy to get up and running)
- **Version Control**: Git and GitHub

## Project Structure

```
.
├── README.md
├── app.py                      # Flask application entry point
├── config.py
├── requirements.txt            # List of dependencies
└── website
    ├── __init__.py
    ├── auth.py
    ├── models.py
    ├── static                 # Contains all static files (CSS, JS, Images)
    │   ├── css
    │   │   └── style.css
    │   ├── images
    │   └── js
    │       └── index.js
    ├── templates
    │   ├── base.html
    │   ├── carts.html
    │   ├── create_cart.html
    │   ├── home.html
    │   ├── login.html
    │   ├── sign_up.html
    │   └── view_cart.html
    └── views.py
```

## Contributing

- We welcome contributions to improve ShopRight! If you'd like to contribute:

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature-branch`).
3.  Commit your changes (`git commit -am 'Add new feature'`).
4.  Push the branch (`git push origin feature-branch`).
5.  Open a Pull Request.


## License

ShopRight is open-source and available under the MIT License.

### Summary

- **Permissions**: 
  - Commercial use
  - Modification
  - Distribution
  - Private use

- **Limitations**: 
  - No liability
  - No warranty


## Contact

If you have any questions or suggestions regarding this project, feel free to reach out at \[deanrobin777@gmail.com\].

---


<br></br>
<div align="right">
    <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>