## studlife

### Team Members
| Name | GitHub account | Email |
| --- | --- | --- |
| Daniyar Bashenov | [bashenov98](https://github.com/bashenov98/) | bashenov98@gmail.com |
| Damir Doskulov | [dsklff](https://github.com/dsklff/) | doskuloff@gmail.com |

### Project Description

We created a platform for social life of KBTU students. <br />
Students can write posts and comment it. <br />
Also, there is an ability to register or participate in the University organizations. <br />
Finally, you can register for the new events and discuss them. <br />

### UML Diagram
![Class Diagram](https://sun1.dataix-kz-akkol.userapi.com/cBb3TZ2p7sJRDFOi_UQZl82vTY7GvoeNatZQpA/nAuf29Tl8ns.jpg)

### Installation
1. Open the terminal and type: git clone https://github.com/bashenov98/studlife.git <br />
2. Create virtual environment: virtualenv env <br />
3. Activate it: source env/bin/activate <br />
4. Open the project folder in terminal: cd studlife <br />
5. Install all needed packages: pip install -r requirements.txt <br />
6. Make migrations: python manage.py makemigrations <br />
7. Migrate: python manage.py migrate <br />
8. Run the server: python manage.py runserver <br />