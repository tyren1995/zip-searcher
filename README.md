# zip-searcher
A basic Vue Quasar/Python FastAPI application which accepts a user-input for zip code and returns the city and state via the USPS API.

# Run Instructions
- Clone this repo and navigate to the root folder on your machine, run ```npm i -g @quasar/cli```
- in the api directory, run ```pip install -r requirements.txt``` and then ```uvicorn main:app --reload --host 0.0.0.0 --port 8000```
- in the ui directory run - run ```npm i```, and then ```quasar dev```
- in your browser, go to http://localhost:8080/#/ . 

- Note : this repo contains my usps api user id without concealment through an env var or other means - please don't share the info and only use this applet for review purposes - thank you!
