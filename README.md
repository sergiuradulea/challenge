# Challenge
[![CircleCI](https://circleci.com/gh/sergiuradulea/challenge.svg?style=svg&circle-token=a3ee0161f2d0e3991f62fba1d7ad31d93d8e9105)](<https://github.com/sergiuradulea/challenge>)

## Steps

* Build
    * Packaging artifacts and make some persist to the workspace
* Test-UI
    * Install PyTest and Selenium
        * I have used Selenium IDE to record my test and exported it to Python pytest.
        * The test checks if the button is clicked and my name is displayed. It doesn’t accept other name besides something that contains “Sergiu”
    * Stand up an HTTP Server on 8000 in the background
    * Test the change. The process fails if this test does not pass.
* Deploy
    * I chose to deploy this to S3 using Static Website Hosting
    * I am installing AWS CLI and boto3
    * Setting AWS Credentials
        * Used environment variables in the CircleCI project
    * Testing S3 Configuration
        * Python script to test 
            * if S3 Bucket Versioning is enabled
            * as further tests you can check the bucket policy, access control lists and the hosting capability to make sure that website works as expected
        * Deploy the webpage to S3



