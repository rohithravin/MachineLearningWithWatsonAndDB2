# Create A Machine Learning Modeling Using IBM Watson Studio and IBM Db2 On Cloud

This code pattern will demonstrate a data scientist's journey in creating a machine learning model using IBM Watson Studio and IBM Db2 On Cloud. We will showcase how to these products work together seamlessly to create a more enjoyable expierence. 

## Flow

## Steps

1. [Clone The Repo](#1-clone-the-repo)
2. [Create an IBM Cloud Account](#2-create-an-ibm-cloud-account)
3. [Load Data into IBM Db2 on Cloud](#3-load-data-into-ibm-db2-on-cloud) 
4. Setup Watson Studio Project
5. Make Machine Learning Model  


### 1. Clone The Repo
Before we start anything, we need to clone the repo. The repo has our dataset and  python notebook which we will use when creating our model.

```bash
git clone https://github.com/rohithravin/MachineLearningWithWatsonAndDB2.git
```

### 2. Create an IBM Cloud Account

Go to the link below and create a free IBM on Cloud Account.

[IBM Cloud](https://cloud.ibm.com)

Creating this account will give us access to create a Db2 on Cloud and Watson Studio service. 

### 3. Load Data into IBM Db2 on Cloud
Now that we have created our IBM Cloud account. We need to create a Db2 on Cloud service. Once we have create that, we will then we able to load our data into our database. 

1. [Create Db2 on Cloud Service](#3a-create-db2-on-cloud-service)
2. [Load Data into Db2 on Cloud](#3b-load-data-into-db2-on-cloud)

#### 3a. Create Db2 on Cloud Service
Head to the [dashboard](https://cloud.ibm.com) of your IBM Cloud account and the follow the steps to create your Db2 On Cloud service.

* In the search bar at the top of your dashboard, search `Db2`.
* Although there are different database options to choose from, for the purposes of this tutorial we will be using the the `Db2` option. Click `Db2` when that option appears in the search bar.
* For the service name, enter in `Data-Science-Track`.
* Make sure you pick the region that is closest to where you currently reside.
* Scroll down to the `Pricing Plan` section and choose the `Lite` plan. 
* Click `Create`

IMPORT NOTE: In some cases you may not be able to create your db2 instance. A warning error will pop-up telling you to create a Cloud Foundary Service. Follow the directed steps to create that service and then try to create a Db2 on Cloud Service again. 

Once you created your database instance, we can head back to the dashboard and click on the `View Resources` link under the `Resource Summary` section. You should then be able to see and verify that your Db2 instance has been created under the `Cloud Foundary Services` tab.  

#### 3b. Load Data into Db2 on Cloud





## Learn more

* **Artificial Intelligence Code Patterns**: Enjoyed this Code Pattern? Check out our other [AI Code Patterns](https://developer.ibm.com/technologies/artificial-intelligence/)

## License

This code pattern is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)
