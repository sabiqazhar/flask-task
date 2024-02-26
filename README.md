
# Flask Task
This is a project to send an email depending on the user specifying the date and send it automatically


## API Reference

#### Get all mail

```http
  GET /mail
```

#### Save email and schedule sended

```http
  POST /mail/save
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required**. Email of recheiver |
| `subject`    | `string` | **Required**. Subject of mail |
| `content`    | `string` | **Required**. Content body of mail |
| `date`    | `timestamp` | **Required**. date for the sender |




## Running Tests project

install pdm first

```bash
  pip install --user pdm
```

install pdm dependencies

```bash
  pdm install
```

setup flask db for the first time
```bash
  pdm run flask db init
```

create first migration
```bash
  pdm run flask db migrate -m "Initial migration."
```

creating first table on db
```bash
  pdm run flask db upgrade
```

run the app
```bash
  pdm run flask run
```

run task schedule
```bash
   pdm run celery -A app.tasks.celery_init.app beat --loglevel=INFO
```