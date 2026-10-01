# https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/

FROM python:3.12-alpine3.23

RUN apk update && \
     apk add --no-cache curl \
        python3-dev \
        git \
        build-base \
        openssl-dev \
        openssl \
        bash \
        wget
        
WORKDIR /app


COPY pyproject.toml ./

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY . .

EXPOSE 8000

RUN addgroup app

USER app

CMD ["flask", "run"]