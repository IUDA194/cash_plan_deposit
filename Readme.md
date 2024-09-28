# Money Manager

![Project Logo](readme_imgs/logo.svg)

Money Manager is an application for managing impulse spending, where clients set a daily limit for their expenses, and any remaining funds can accumulate and be used later.

## Features
- **Daily Limit Setting**: Clients can specify the amount they are willing to spend on impulse purchases each day.
- **Balance Accumulation**: If a client does not spend their entire limit for the day, the remaining funds accumulate in their balance.
- **Transactions**: Clients can log their expenses, reducing their current balance.
- **Example**: If a limit of $5 is set per day and the client does not spend any money for three days, they will have $15 accumulated in their balance.

## Technology Stack
- **Backend**: Python, Django, Django REST Framework
- **DevOps**: Jenkins, Docker, Kubernetes

## Related Microservices
A separate microservice is used for daily balance deposits:  
[Daily Balance Deposit Microservice](https://github.com/IUDA194/cash_plan_deposit)

## Project Links
- Main Project: [Money Manager](https://cash-planner.sitera.tech)
- Backend: [Money Manager Backend](https://back-cash-planner.sitera.tech)

## Changelog

### Version 1.0.0
- Project initialization

## TODO
