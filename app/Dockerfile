FROM python:3.13-slim AS fast-base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt 

RUN adduser --disabled-password --gecos '' user && mkdir /app/logs && chown -R user:user /app/logs

FROM fast-base AS fast-server

USER user
COPY --chown=user:user . .

CMD [ "python" , "main.py" ]