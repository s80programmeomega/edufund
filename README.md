# EduFund
EduFund is a crowdfunding platform that helps financially struggling secondary school students in Nigerian (public) schools raise funds for school fees and essential learning materials.


## How to run the project

#### 1. Install python into your system (version 9 to 11)

#### 2. Create a virtual environment like this:
    python -m venv <Your virtual environment name>
    example: python -m venv .venv

#### 3. Activate your virtual environment:
    --For Windows users:
        .\.venv\Scripts\activate
    __For Linux users:
        source .venv/bin/activate

#### 4. Clone this project and move into the project directory
    git clone https://github.com/s80programmeomega/edufund.git
    cd <path/to/the/project/directory>

#### 5. Install project requirements
    pip install -r requirements.txt

#### 6. Run the server
    python manage.py runserver

#### 7. Go to http://localhost:8000/
