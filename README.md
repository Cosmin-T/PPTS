# PPTS

## Project Overview

The eMag Product Tracker is a comprehensive tool designed for tracking product prices, managing product data, and analyzing historical price trends for products listed on the eMag retail platform. Built with Python, it leverages a modular architecture incorporating web scraping, data storage, and interactive user interfaces through Streamlit. The application consists of several scripts handling specific aspects such as user interaction (via Streamlit), data handling, web navigation (using Selenium), and configuration management.

## Key Features

- Interactive search feature for finding products on eMag.
- Reformat and multi-product search capabilities.
- Data tracking for price changes and product history.
- Interactive data tables for a clear display of products and prices.
- User-friendly Streamlit interface for easy navigation.
- Automated web scraping for up-to-date product information.
- Captcha solving integration to bypass security measures on websites.
- Data storage and management with Deta for persistence.

# Setup and Installation

To set up the eMag Product Tracker, follow these steps:

## Environment Preparation

Ensure you have Python 3.x installed on your machine. It's also recommended to use a virtual environment.

Create a virtual environment:

```bash
python3 -m venv myenv
```

Activate the virtual environment:
On Windows:

```bash
myenv\Scripts\activate
```

On macOS and Linux:

```bash
source myenv/bin/activate
```

## Clone the Repository

Use Git to clone the repository to your local system:

```bash
git clone https://github.com/your-username/eMag-Product-Tracker.git
```

## Install Dependencies

With your virtual environment activated, install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Configuration Files

You will need to configure the `config_ini.py` to specify the path for your configuration settings then, create a `config.ini` file in the 'logic directory of the project with the following content:

```ini
[DEFAULT]
API_KEY = your_api_key_here
DETA_KEY = your_deta_key_here
```
