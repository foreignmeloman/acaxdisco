# Lambda functions

## Hands-on

Create a lambda function with following requirements:

* Use `lambda-s3-fullaccess` role for the function, see what policies it contains
* It will be triggered by file upload to your `name-surname-upload` (add random symbols or numbers if the bucket already exists) s3 bucket
* The function must take the uploaded text file and add a new line at the end saying `Welcome to the Lambda Complex, Mr. Freeman.`
* The resulting file must be uploaded into the `processed/` directory of s3 bucket named `name-surname-store`
* Finally the original file must be deleted from `name-surname-upload`
* Recomended language: Python
