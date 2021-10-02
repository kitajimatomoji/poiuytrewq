import json
import boto3
import time

class CloudWatch_logger:

    def __init__(self, log_group_name, log_stream_name):
        self.log_group_name = log_group_name
        self.log_stream_name = log_stream_name
        self.logs_client = boto3.client('logs')

        # search a log group and get its information.
        res = self.logs_client.describe_log_groups(
            logGroupNamePrefix = self.log_group_name
        )

        if len(res['logGroups']) == 0:
            # log group has not existed. create it.
            self.logs_client.create_log_group(
                logGroupName = self.log_group_name
            )

        # search a log stream and get its information.
        res = self.logs_client.describe_log_streams(
            logGroupName = self.log_group_name,
            logStreamNamePrefix = self.log_stream_name
        )

        if len(res['logStreams']) == 0:
            # log stream has not existed. create it.
            self.logs_client.create_log_stream(
                logGroupName = self.log_group_name,
                logStreamName = self.log_stream_name
            )


    def log(self, message_json):
        seq_token = None

        # search a log stream and get its information.
        res = self.logs_client.describe_log_streams(
            logGroupName = self.log_group_name,
            logStreamNamePrefix = self.log_stream_name
        )

        if res['logStreams'][0].get('uploadSequenceToken'):
            # this log stream has logs. need to point its uploadSequenceToken.
            res = self.logs_client.put_log_events(
                logGroupName = self.log_group_name,
                logStreamName = self.log_stream_name,
                logEvents=[
                    {
                        'timestamp': int(time.time()) * 1000,
                        'message': json.dumps(message_json)
                    },
                ],
                sequenceToken=res['logStreams'][0]['uploadSequenceToken']
            )
        else:
            # log stream has no log then does not have uploadSequenceToken.
            res = self.logs_client.put_log_events(
                logGroupName = self.log_group_name,
                logStreamName = self.log_stream_name,
                logEvents=[
                    {
                        'timestamp': int(time.time()) * 1000,
                        'message': json.dumps(message_json)
                    }
                ]
            )
