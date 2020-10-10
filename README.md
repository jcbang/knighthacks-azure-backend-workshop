# knighthacks-azure-backend-workshop

## Setting this up
- Please follow my slides here https://docs.google.com/presentation/d/10Of0NQ-5KmFdixxoxN-K04-LyT8vbQJfrXZ96AH0d8U/edit?usp=sharing in order to learn how to set this up!
- Please replace the ```ENDPOINT``` and ```KEY``` variables in upload_database_data/__init__.py in order to ensure the upload_database_data script runs properly! Information on how to get the ENDPOINT and KEY variables can be found in my slides as well.

## Understanding this Code
- I tried to comment the three functions that exist in this repository
- The file structure for this repository (and all other Azure Functions Apps by default) is [function name]/__init__.py, where __init__.py contains the code that runs the function, and the folder name is what the function is named when you deploy it

## Testing this Code
1. Deploy this Code to your own Azure Functions App on Azure (through the steps found in my slides)
2. Grab the URL of the function you want to test (I recommend you start with 'simple_test_function')
3. Install a Web API Tester (I use Postman, but other apps like ARC also exist out there)
4. Paste the URL and test it out!
