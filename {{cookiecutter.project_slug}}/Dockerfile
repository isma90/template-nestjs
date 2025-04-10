FROM node:18-alpine

ENV PRISMA_CLIENT_ENGINE_TYPE='binary'

WORKDIR /app

COPY package.json.jinja2 ./package.json
COPY ./dist ./dist
COPY ./node_modules ./node_modules

EXPOSE 3000
CMD [ "yarn", "start:prod" ]
