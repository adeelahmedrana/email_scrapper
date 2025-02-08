# Selenium Email Scraper

A simple **Python** script that uses **Selenium** (headless Chrome) to scrape a website for email addresses. This is particularly useful for websites protected by JavaScript-based anti-bot measures or captcha checks, which makes traditional `requests`-based scraping difficult or impossible.

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Example Script](#example-script)  
6. [Example Output](#example-output)  
7. [Troubleshooting](#troubleshooting)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## Overview

**Selenium Email Scraper** is a Python tool for:

- Launching a headless (invisible) Chrome browser  
- Accessing a target URL  
- Locating the page with “Contact Us” or related contact info  
- Extracting email addresses from the rendered HTML

It’s helpful when you need to scrape websites that rely on JavaScript to display content or employ anti-bot measures that prevent libraries like `requests` or `cloudscraper` from succeeding.

---

## Features

- **Headless Chrome**: Runs without opening a visible browser window.  
- **Contact Page Detection**: Searches for links containing “contact” in the link text or URL.  
- **Email Extraction**: Uses a regular expression to find emails on the rendered page.  
- **Customizable**: Change the base URL or skip detection and directly open a known contact page.

---

## Installation

1. **Clone or Download** the Repository

   ```bash
   git clone https://github.com/yourusername/selenium-email-scraper.git
   cd selenium-email-scraper
