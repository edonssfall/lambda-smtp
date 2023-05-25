# lambda-smtp
# Quick Start
1. Clone code:
```sh
git clone https://github.com/edonssfall/lambda-smtp.git
```
2. Package code if change code:
```sh
sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket your-bucket-name
```
3. Deploy on AWS:
```sh
sam deploy --template-file packaged.yaml --stack-name lambda-function-name
```

## Send API(Test):
```JSON
{
 "sender": "sender@email",
 "reciever": "reciever@email",
 "subject": "subject email",
 "body": "email text",
 "smtp_server": "smtp server",
 "smtp_port": "smtp port",
 "username": "username",
 "password": "password"
}
```
