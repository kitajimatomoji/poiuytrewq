import os
import sys
import random

from cloudwatch_logger import CloudWatch_logger

try:
    ret = {"trigger":"edit_content"}
    #ret = {"trigger":"application_update"}
    ret["contentful_response_time"] = random.uniform(2, 10)
    ret["contentful_data_amount"] = random.uniform(100000, 120000)
    ret["content_building_time"] = random.uniform(5, 20)

    #str(uuid.uuid4())

    print(ret)

    log_group_name = '/aws/lambda/logging_sample_daily'
    log_stream_name = datetime.datetime.now().strftime('%Y_%m_%d')
    #log_stream_name = '2020_06_29'

    logger = CloudWatch_logger(log_group_name, log_stream_name)
    logger.log(ret)
