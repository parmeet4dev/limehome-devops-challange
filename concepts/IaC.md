## Task
Infrastructure as Code
What is it? Why would I want it? Are there any alternatives?


## What is Infrastructure as Code:

IaC as the name implies is a concept to document all the computer network infrastructure as code. 

To better understand the concept, let's assume we are living in the **world without IaC**.

**Scenario:**

Let's consider Alice is an Admin who is tasked to create and maintain a cloud infrastructure environment for the new application the company is planning to launch. 
For creating the env there are Usually three main activities involved:
1. Provisioning the servers
2. Configuring the servers
3. Deploying the application

Now, Alice has created some Servers, databases and a block storage for hosting the application.
Then he configured the servers and database to comply with the applications.
And lastly, he deployed the code in the environment.

This went well initially for the application and the application gained huge popularity and attracted unexpected visitors. And with this popularity, the company made good money and hired more people to support the environment.

Now to sustain the traffic Alice has to recreate the environment from scratch. But, this generated some problems:

- Alice has to devote man-hours additionally to plan the exact number of visitors on the website
- Again create the servers and configure them
- He cannot recall all the exact configs he added while creating the environments initially.
- With new developers, many human errors were introduced as there is no transparency and auditing involved.
- Alice no longer has visibility on what the team is introducing within the environment as there is no version control involved
- If any server dies, it is difficult to revert to previous versions.
 
These problems led to downtime of the application and it failed to cater to the growing userbase thus the company has to bear losses every minute passed.

**Solution**

With IaC we can resolve all the above issues, you can define your infrastructure as code by using a **simple, human-readable language** and then use popular tools like Terraform to provision and configure your infrastructure, across multiple cloud providers such as AWS, Microsoft Azure and Google Cloud Platform. 

## Why would I want it:

Benefits of using Infrastructure as code:
- **Automation**: As you can code your infra, this gives you the power to automate repetitive/mundane tasks with or without human intervention, thus reducing human errors.
- **Human readable code**: with tools like Terraform/AWS CloudFormation you can define your code in simple JSON/YAML formats which are easy to define and understand. Or you can use AWS CDK to define the code in a programming language of your choice.
- **Scaling**: Once you can define your requirements it is easy to scale up/down this gives acceleration to your development pipelines 
- **Version Control**: IaC provides the additional benefit of introducing version control to your codebase and you can have finer control, visibility and auditing capabilities about your changes. This also helps in reverting to previous versions in case of failure. *IaC also _serves as _a _source__ of truth_ for your infra*
- **Integration**: IaC tools are built to integrate with your DevOps pipelines, you can test, continuously integrate and deploy your code swiftly.  

With the above benefits along with others, IaC also has some common issues associated:

- **Learning and maintaining yet another tool**: You have to learn to code your infra, although this is human readable language as the complexity grows this can be overwhelming. And you have to maintain one or more tools for IaC.
- **Configuration Drifts**: IaC comes with a risk of configuration drift. This happens if the developers make ad-hoc changes to the server configurations outside the IaC template without using change management tools
  

## Are there any alternatives?

An alternative to IaC is traditional infrastructure management which has been a go-to approach for many years.