FROM node:18-alpine

WORKDIR /frontend

EXPOSE 8001

COPY package.json package-lock.json ./

RUN npm install

COPY . ./

CMD [ "npm", "run", "dev"]
