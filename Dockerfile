FROM                        python:3.6.7-slim
MAINTAINER                  tech@ashe.kr

WORKDIR                     /srv

ADD                        ./nginx /srv/nginx/
ADD                        ./gunicorn /srv/gunicorn/

RUN                         pip install --upgrade pip
RUN                         pip install pipenv


RUN                         apt-get update && \
                            apt-get install -yq gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 \
                            libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 \
                            libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
                            libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 \
                            ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

ADD                        ./sources/Pipfile /srv/Pipfile
ADD                        ./sources/Pipfile.lock /srv/Pipfile.lock
RUN                         pipenv lock --requirements > requirements.txt
RUN                         pip install -r requirements.txt
RUN                         pip install gunicorn

ADD                        ./sources/app/ /srv/app/
