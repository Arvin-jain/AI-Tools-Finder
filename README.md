# AI Tools Finder
 Find the cheapest price for your tool by sending an image or part number
![1732655706564 (1)](https://github.com/user-attachments/assets/bb884fe2-d225-4cec-b6ee-8a4544727dcc)
![1732655705172 (1)](https://github.com/user-attachments/assets/a7eae17c-e5bd-4c88-8deb-abf38c51b763)
![1732655705086 (1)](https://github.com/user-attachments/assets/f67de1ad-a37d-4d35-b5f1-6ac75032ae5c)
![1732655706008 (1)](https://github.com/user-attachments/assets/839a9930-b9ff-4432-b5ac-1a2f2ba11eed)

Developed a web app that allows users to search for tool data by uploading an image or entering a part number. The app retrieves results from a MongoDB database and Weaviate.

Flask-based REST API: Created an API to process image-based queries in Weaviate, which returns results to a Node.js server for front-end rendering. Built a Python script that converts images into vectors using Weaviate libraries, requests, and PIL, enabling image-based searches.

Web Scraping: Implemented a web scraping script with JavaScript and Puppeteer to gather product data from three different online sellers, storing it in MongoDB.

Node.js Server: Developed a Node.js server using Express.js and CORS, which functions as a REST API that queries MongoDB for the cheapest price from multiple online sellers and serves the results to the front-end.

