FROM node:lts-alpine

WORKDIR /ui

ENV PATH /ui/node_modules/.bin:$PATH

#RUN echo "installing vue"
RUN npm install vue

COPY package.json .
COPY package-lock.json .

#RUN echo "installing dependencies for vue app"
RUN npm install

#RUN echo "Starting vue app"
CMD ["npm", "run", "dev"]