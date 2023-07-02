FROM node:18.6

# ENV PORT 80
EXPOSE 80

WORKDIR /src
COPY . /src/
RUN npm install
RUN npm run build
CMD ["node", "-r", "dotenv/config", "build"]

# CMD ["npm", "run", "dev"]