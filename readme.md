
## Report on the association between Covid 19 and Economic power.

#### Data Set : COVID 19 worldwide case (https://www.kaggle.com/datasets/sandhyakrishnan02/latest-covid-19-dataset-worldwide?resource=download), World Economic Outlook data set (https://www.imf.org/en/Publications/SPROLLs/world-economic-outlook-databases#sort=%40imfdate%20descending)

My primary question is about the association between economy and COVID-19 of each country. Along with the primary dataset about COVID-19, I operated several statistical analysis including dimensionality reduction, clustering analysis and regression analysis. 

In the case that you fail to make the report, I save the result file into backup folder. 

To build docker container, please follow below instruction.

1. Turn on the docker desktop. If you don't have the docker desktop, you can install it in here (https://www.docker.com/products/docker-desktop/)

2. Build docker container and run the development environment.
```{}
cd "./directory of this project"
docker build -t myapp .
```

This will create a docker container. You can use it though 
```{}
docker run -v $(pwd):/home/rstudio/ -e PASSWORD=yourpassword --rm -p 8787:8787 myapp
```

Now, please visit http://localhost:8787 via a browser on your machine to access the development environment. 

3. Now run the following command at the terminal. 
```{}
make report.html
```
Then the report will automatically made and you can see it. 

To clean the output, please run the following code at terminal

```{}
make clean
```

