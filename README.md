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

A live demo of ShopRight will be available soon. For now, feel free to clone the repository and run the app locally using the [Installation](#installation) instructions below.

---

## Installation

To get started with ShopRight, follow these steps:

### 1. Clone the repository

```
git clone https://github.com/yourusername/shopright.git
cd shopright
```

### 2. Create a virtual environment (optional but recommended)
```
python3 -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
```

### 3. Install the required dependencies
`pip install -r requirements.txt`

### 4. Set up environment variables
Create a .env file in the root directory and add any necessary environment variables

### 5. Run the application
`flask run`

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

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap, HTML5, CSS3, JavaScript
- **Database**: MySQL (for robust data storage)
- **Version Control**: Git and GitHub

## Project Structure

```
shopright/
│
├── app.py                   # Flask application entry point
├── static/                  # Contains all static files (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   └── img/
├── templates/               # HTML templates
│   ├── base.html
│   └── index.html
│   └── login.html
│   └── signup.html
│   └── logout.html
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
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


## Contact

If you have any questions or suggestions regarding this project, feel free to reach out at \[deanrobin777@gmail.com\].

---


<br></br>
<div align="right">
    <sub style="font-style: italic"> Dean Robin Otsyeno - deanrobin777@gmail.com</sub>
</div>