# rabbitmq-python-introduction

This repository introduces Python implementation of [RabbitMQ](https://www.rabbitmq.com/) with [Docker](https://www.docker.com/) for the sake of Machine Learning tasks. \
Python 3.7 is adopted in this project because some ML libraries don't support the latest versions (e.g., Python 3.8, 3.9). \
If you want to know for details, you should see the [official site](https://www.rabbitmq.com/).


## Starting docker containers
First, you build docker containers.
```bash
$ docker-compose up
```

## Starting producers
### Attaching shell

Attach the shell with:
```bash
$ docker exec -it producer bash
```

In this example,
- Sending messages to the queues from the producers
- Consumers process the messages from the queues

```bash
$ python producer.py
```

## Check it

Now go to http://localhost:15672/. \
You will see the monitoring/admin pages with `Username: guest` and `Password: guest`.


## Further information

- [Tutorials (Official)](https://www.rabbitmq.com/getstarted.html)