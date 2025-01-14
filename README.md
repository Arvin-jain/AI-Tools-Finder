# AI Tools Finder
 Find the cheapest price for your tool by sending an image or part number

![Description of Image](https://media.licdn.com/dms/image/v2/D4E22AQECeswkzjYicQ/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1732655706008?e=1740009600&v=beta&t=IJAJPFXPEMPCs9OVQ3DwFXFsSeegYH21nknpnN_Furs)

![Description of Image](https://media.licdn.com/dms/image/v2/D4E22AQF7Tofk6QTyZw/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1732655706564?e=1740009600&v=beta&t=AEwkRzswkSQOvu9_vVbAeoQt5Nbd3eWVdd6qoWj8sbY)

![image 3](https://media.licdn.com/dms/image/v2/D4E22AQH-lG5emog6pg/feedshare-shrink_20/feedshare-shrink_20/0/1732655705086?e=1740009600&v=beta&t=3BYUBz_Mn40FlEyn_H2BcEy664olWv0SmnsmpOovAYc)

![image 4](https://media.licdn.com/dms/image/v2/D4E22AQHctizbqEWd4A/feedshare-shrink_20/feedshare-shrink_20/0/1732655705172?e=1740009600&v=beta&t=cIxPfG4RALLWkpMaj8Jn2q0GS2qY51cMSoLBvfjjCuw)


Developed a web app that allows users to search for tool data by uploading an image or entering a part number. The app retrieves results from a MongoDB database and Weaviate.

Flask-based REST API: Created an API to process image-based queries in Weaviate, which returns results to a Node.js server for front-end rendering. Built a Python script that converts images into vectors using Weaviate libraries, requests, and PIL, enabling image-based searches.

Web Scraping: Implemented a web scraping script with JavaScript and Puppeteer to gather product data from three different online sellers, storing it in MongoDB.

Node.js Server: Developed a Node.js server using Express.js and CORS, which functions as a REST API that queries MongoDB for the cheapest price from multiple online sellers and serves the results to the front-end.

