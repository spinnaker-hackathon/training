# Armory Spinnaker AWS Quickstart 
## Deploy to EC2 AutoScale Groups

1. Create Application called "**YourName**" by clicking "**Applications**" tab > "**Action**" (top right) > "**Create New App**" with the following Settings

![No CREATE Permission](/New-App.png)
  
2. Go into Application "**YourName**" and create first pipeline to deploy and EC2 instance
3. Click **Add Stage +** and search for a **Bake** stage to bake AMI
4. Select the AWS Region you would like to deploy in
5. Click **Add Server Group** and configure basic AMI bake settings (Account, Region, Subnet, Instance Type, and AWS SSH key)
6. Click **Done** and then **Save Changes** in the bottom right corner
7. Click **Add Stage** and add another stage called **Deploy** for AWS EC2
8. Click the "**Back to Execution**" button on the top left of the Pipeline Name
9. Run your Pipeline and Validate!  The end result will be an Auto Scaling Group build within your AWS subnet.

### EC2 Pipeline and deployment

![No CREATE Permission](/Deploy-to-EC2.png)

### Note - Don't mind the red dot in the Bake Stage.  It's informational suggesting a CI Trigger should be configured for a Bake Stage to ensure you are deploying the latest code and artifacts

![No CREATE Permission](/AutoScale-Group.png)
