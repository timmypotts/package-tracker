# build environment
FROM node:13.12.0-alpine as build

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm ci
RUN npm install react-scripts@4.0.1 -g
COPY . ./
RUN npm run build                

# production container
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html


COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 5000
CMD ["nginx", "-g", "daemon off;"]