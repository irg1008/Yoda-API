FROM node:14-slim

WORKDIR /app

COPY package*.json ./
COPY prisma ./prisma
COPY tsconfig.json .env ./
COPY ./ ./

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y libssl-dev

RUN npm install
RUN npm run build

EXPOSE ${PORT}
EXPOSE 3000
CMD [ "npm", "start" ]
