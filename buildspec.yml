version: 0.2
phases:
  install:
    runtime-versions:
      python: 3.7
  build:
    commands:
      - pip install --upgrade awscli
      - python -m unittest discover tests
      - aws lambda update-function-code --function-name  Hello_World --zip-file fileb://deployment_package.zip
artifacts:
  files:
    - '**/*'
