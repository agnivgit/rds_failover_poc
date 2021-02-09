# rds_failover_poc

This is a poc for performing a RDS failover if a RDS DB instances goes down.

Idea:

A RDS postgress DB instnace (example : agniv-db) is running from us-east-1 and a read replica of the same is running from us-east-2.
Db instnace in us-east-1 regions has been configured with a RDS Event subcription (RDSEventforDBStateChange) which invokes a SNS topic (invokeLambdaSNSTopic) during db failure.
This sns topic invokes a lambda function (invokeStepFunc.py) which kicks off a Step function (DbPromoteRRtoMaster) to do the db failover.
The Step function invokes multiple lambdas one after another to achive the same.
    1. promoteRRtoMaster.py
    2. dbInstanceStatusCheck.py
    3. dbR53CnameSwitch.py
After the db failover completion , Step function will send notification to user via SNS topics.

Diagram: will be added soon