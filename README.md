# KudosFeedback APP
Is an employee recognition platform that helps to provide a positive workplace culture by enabling peer-to-peer recognition. It allows employees, managers, customers and other stakeholders to acknowledge individual or team contributions through messages/ sending a in form of kudos.

## Requirements and Dependencies:
* Docker
* Python [Django]
* React

## Cloning Repository:
*   [gitHub](https://github.com/igorklepuszewski/commwell.git)

## Environment setup:
Run command: `docker-compose up --build`

## Accessing the environment:
Once you done with setup, good to go with base url: `http://127.0.0.1:8001/api`

## Endpoints:
* /user
    * GET : list of registerd user.
    * POST: Registed a new user.
* /kudos
    * GET : list of kudos.
    * POST: send kudos.
* /feedback
    * GET : list of feedback.
    * POST: send feedback.
* /badge
    * GET : list of badge.
    * POST: send badge.
* /kudoscategory
    * GET : list kudos category.
    * POST: create new kudos category.
* /feedbackcategory
    * GET : list feedback category.
    * POST: create feedback kudos category.


## Limitations:
* Right now we can send or received kudos or feedback within the platform privately.
* We don't have feature, what will do with the kudos points.