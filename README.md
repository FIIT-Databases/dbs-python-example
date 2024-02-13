# DBS Assignment Example in Python

This repository is a simple example of a Python HTTP application based on the [FastAPI](https://fastapi.tiangolo.com/)
containerized in the Docker environment. You don't have to stick with the FastAPI for your assignments, this repository
is just a simple example of Docker build process with environments variables (which you have to use because of the
database configuration).

If you have any questions feel free to create an issue or offer a pull request.

## Content of the repository

Application contains a simple HTTP endpoint `GET /v1/hello` which will return a JSON bellow where value of the `hello`
property is from the `NAME` environment variable. Environment variables are processed using the
[BaseSettings](https://docs.pydantic.dev/usage/settings/) object of the [pydantic](https://docs.pydantic.dev/) library.

`Dockerfile` inside the repository contains all required dependencies for the Python PostgreSQL driver
[psycopg2-binary](https://pypi.org/project/psycopg2-binary/). If you want to build a `psycopg2` from source (using the
[psycopg2](https://pypi.org/project/psycopg2/) you have to install a compiler inside the container).

The `.github/workflows/publish.yml` contains a CI/CD configuration for the Docker image build and publish using the
GitHub Actions. If you wish to build and publish the image manually check the installation section specialized for the
Docker image.

## Structure

- `.github/workflows/publish.yml`: GitHub Action recipe for Docker build and publish to the GitHub Container Registry
(you probably don't need to touch this)
- `dbs_assignment`: application module
  - `endpoints`: module for HTTP endpoints
    - `hello.py`: home of the `GET /v1/hello` HTTP endpoint
  - `__init__.py`: Check Python [docs](https://docs.python.org/3/tutorial/modules.html#packages)
  - `__main__.py`: Check Python [docs](https://docs.python.org/3/library/__main__.html)
  - `config.py`: Definition of the settings object
  - `router.py`: FastAPI [router](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=#apirouter)
- `.dockerignore`: Files skipped in the Docker `COPY` command
- `.editorconfig`: Nice & shiny editor settings
- `.gitignore`: Files ignored by git
- `Dockerfile`: Docker image definition
- `requirements.txt`: Python [dependencies file](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

## Installation

### From source

These are instructions for Linux/macOS operating systems. Windows may differ depending on your system configuration.
Keep in mind that application requires presence of variables from the `config.py`. Check the Pydantic docs provided
for more information.

1. Create python virtual environment: `python -m venv venv`
2. Enter environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run application: `uvicorn dbs_assignment.__main__:app --reload`

### Docker

You can build your Docker image with name `dbs-python-example` (you have to use same name as the name of the
repository) simply by calling:

```shell
docker build -t dbs-python-example .
```

After a successful build, you can run it as a container named `dbs-python-example-container` using command bellow.
This example also pass the `NAME` environment variable with value `Dexter` and redirect ports, so you can access the
HTTP server inside the container.

```shell
docker run -p 127.0.0.1:8000:8000 --env NAME=Dexter --name dbs-python-example-container dbs-python-example
```

If the waiting time for a GitHub actions is too long, you can publish yours local build image
using [docker push](https://docs.docker.com/engine/reference/commandline/push/). Keep in mind the tester accepts only
images published inside the FIIT-Databases GitHub organisation.

Firstly you have to tag your local image according to the scheme bellow (replace curly braces):
`ghcr.io/FIIT-Databases/{your-repository-name}:{tag-name}`.

Valid command for this repository and tag name `latest` looks like this:

```shell
docker tag dbs-python-example ghcr.io/fiit-databases/dbs-python-example:latest
```

You can use tag names for different versions of your image (for example to identify assignment version). The CI/CD
pipeline creates Docker image for:

- each commit to `main` branch (will produce Docker image with `:main` tag),
- each commit to `master` branch (will produce Docker image with `:main` tag),
- each tag following sematic versioning (will produce Docker image with `:x.x.x` tag where `x.x.x` is version)

For more information check the **Publishing** section.

You can publish newly tagged image to the remote using
[docker push](https://docs.docker.com/engine/reference/commandline/push/) command.

```shell
docker push ghcr.io/fiit-databases/dbs-python-example:latest
```

## Publishing

Each assignment have to be published using via GitHub Releases. The CI/CD pipeline is configured for the [Semantic
versioning](https://semver.org/) scheme (the Docker is created for each git tag with sematic version eg. `1.0.0`).

![](docs/publish.gif)

After you submit your assignment, you can't replace a container in the registry (Docker images created after
submission deadline will be rejected).

![](docs/releases.gif)

---
![](docs/fiit.png)
