# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup

**[TODO 05/01/2018 @vanessa-cooper]:** _It's been a while since anyone ran a fresh copy of this repo. I think it's worth documenting the steps needed to install and run the repo on a new machine?_

**Install docker**
Check if installation was done correctly using the following

```
docker -v
docker-compose -v
```
If all good then cd in the cloned project directory and run

`docker-compose -up`

If Docker is working correctly, the backend should be running and able to connect to your local database.

Test this by pointing your browser to http://localhost:3000/api/ping

Now, it’s time to check the frontend and make sure it’s connected to the backend.

If everything is working properly, you’ll be able to create a new user on http://localhost:3001/register