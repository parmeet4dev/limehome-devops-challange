## Task
Imagine you would join our team and put in charge of securing our AWS infrastructure. What are the first three things that you check, to limit the risk of a breach? Explain why.

#### Assumptions
- I have access to the root account of the organization.
I have the authority to spin up some services to analyze the status of the organization

## Introduction

Considering this is to be the first time I will get access to AWS, I will follow the security pillar triad,  **CIA** wiz *Confidentiality Integrity and Authentication* this will help me profiling the security posture of the account.

#### Confidentiality
This pillar adheres to make sure that the data is secured and private. This means that only authorized individuals/systems can have access to sensitive or classified information. The data-in-transit should not be accessed by unauthorized individuals.
To make sure these requirements are met, I will check the following:

- **Identity Access Management(IAM)** - IAM is a service that securely manages identities and access to AWS services. 
  - I will first **check if MFA is enabled** for all users to ensure confidentiality.
  - I will then check the IAM policies and remove the policies that give permission to do everything in every resource and use condition-based policies with the least access.
  
- **Network Security and Encryption** - I will check the network and encryption services to ensure that data-in-transit or data-at-rest is protected.
  - I will analyze the existing security groups and ACLs to ensure that they are well planned and are not opening any open ports to allow the malicious actor to access the network.
  - I will check proper encryption is used whenever possible especially for S3 buckets.


#### Integrity

This pillar focuses on ensuring the data is trustworthy and free from tampering. The integrity of your data is maintained only if the data is authentic, accurate, and reliable.  

To make sure these requirements are met, I will check the following:
Ideally, we should **follow the principle of Least Privilege** by granting only the specific permissions required to perform specific tasks. In IAM I will check the **IAM Access Analyser** (if enabled) to check the status of the users/roles that are in use and if they are following the principle of Least-Privlage or not. Or I will download the **Credential report** to find the unused and unwanted access
- I will check if there are multiple accounts, then they are part of AWS Organizations and they have required Service Control Policies (SCPs) which allows us to control which AWS service actions are accessible to principals in the accounts of your organization and thus reduce the blast radius of potential attacks.
- I will check AWS Config to find any non-compliant resources in the account.

#### Availability

This means that the network should be readily available to its users and all resources are regularly updated and should have backups in case of fail-over. Outdated resources provide a backdoor to malicious actors and thus compromise the network.

To make sure these requirements are met, I will check the following:
- **Monitoring and Logging** - Enabling CloudTrail, CloudWatch, and AWS Config supports availability by providing insights into the system's health, performance, and compliance. These services help detect and respond to incidents promptly, minimizing downtime.
- I will also enable Guarduty service and this can help to continuously monitor for malicious activities and potential security threats.
  

-----

## Conclusion

To summarise, Cloud security involves addressing various aspects to reduce the risk of a breach and hence I will use AWS services like IAM, VPC, KMS, Guardduty etc to identify the potential security threats.