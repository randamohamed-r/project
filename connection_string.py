
import boto

from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['MONGODBURL'], os.environ['mongodb+srv://mongo:cu3eGs7dFAFQB7Dm@cluster0.v6erp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'])