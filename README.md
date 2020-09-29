## daizu-online-judge-backend

[![Actions Status](https://github.com/SoyBeansLab/daizu-online-judge-backend/workflows/CI/badge.svg?branch=develop)](https://github.com/SoyBeansLab/daizu-online-judge-backend/actions)

## Development

### Installing dependent packages

If you do not have poetry installed, then execute the following command.
```bash
$ pip install poetry
```

```bash
$ poetry shell
$ poetry install
```

### Running the application

```bash
$ poetry run python app.py
```

### Exceuting Lint and Test

```bash
# Check only
$ poetry run black . --check -l 80
# Formatting with black
$ poetry run black . -l 80
```

```bash
$ poetry run pytest
```

## Environment variables
Please set the environment variables of the table to .env, etc.

| name                        | default value | 
| :-------------------------- | :------------ | 
| DAIZU\_DATABASE\_HOST       | localhost     | 
| DAIZU\_DATABASE\_NAME       | doj           | 
| DAIZU\_DATABASE\_USERNAME   | daizu         | 
| DAIZU\_DATABASE\_PASSWOWRD  | soybeanslab   | 
| DAIZU\_LOG\_STREAM          |               | 
| DAIZU\_LOG\_FILE            |               | 
| DAIZU\_AUTH0\_DOMAIN        |               | 
| DAIZU\_AUTH0\_API\_AUDIENCE |               | 

## Author
SoyBeansLab

## License
MIT License
