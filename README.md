# Homework 3 and 4 for software QA

## Objective:
Develop testing and deployment plans that enable continuous deployment of an existing
software system that is extended for web access. Create automated acceptance tests (end-to-end
testing) and integration (regression) tests.

## Scenario:
You have been asked to create a web interface for the application you created for Assignment2. The VP of Engineering at your firm also wants to ensure that you can continuously deploy
new features, bug fixes, and changes to the application. She also wants to ensure the quality of
the overall system by adopting a quality assurance and test plan.
You will augment the existing application and make it accessible via a web interface and build
& document a deployment pipeline for the system using various tools and cloud infrastructure.

## Requirements.
Web Interface - Add a web interface to your command line app and make it accessible via the
Google Cloud Platform (e.g., container engine [vm], Google App Engine, etc.).

Deployment Pipeline - Setup a deployment pipeline using continuous integration and delivery
tools (can make your GitHub project public).

## Features of my app

### Web Interface

I used the web framework Flask for my python app. I mixed in css within the index.html file so no external css file is referenced.

### Deployment pipeline

Source control - ... 🙄 that's this right here.

Continuous integration - well seeing as I'm the only one writing the code and pushing it to github, requirement accomlished.

Static analysis - flake8 is used via a github action on all pushes to the main branch to test all .py files and output the linting results.

Unit testing in python with unittest - these are automatically ran with github actions on push to github.

Code coverage - I used a github action to run the unit tests and other tests in my code to test the functions. This action finds the code and test coverage and comments on each commit with the percent hit/missed as well as some other statistics. See latest commit to view the message.

Continuous deployment to heroku - upon a push, herou will wait for the unittests to pass, if they pass, it will then deploy the new app to the staging server. I can then go into the heroku dashboard and manually choose to deploy this to the production server.

Manual push to production - within the heroku app, I have to go into the dashboard and deploy the updated webpage resulting from a commit, push, and succesful test, from the staging server to the production server.

![""](https://cdn.discordapp.com/attachments/809989018582253568/832122310676578324/unknown.png)
