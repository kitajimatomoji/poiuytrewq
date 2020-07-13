from cloudwatch_logger import CloudWatch_logger

ret = {"trigger":"edit_content"}
#ret = {"trigger":"application_update"}
ret["contentful_response_time"] = 123
ret["contentful_data_amount"] = 1230
ret["content_building_time"] = 12

log_group_name = '/aws/lambda/logging_sample_daily'
log_stream_name = '2020_06_25'

logger = CloudWatch_logger(log_group_name, log_stream_name)
logger.log(ret)
