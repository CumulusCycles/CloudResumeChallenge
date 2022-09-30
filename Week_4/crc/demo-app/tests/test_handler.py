import os
import re
import json
from unittest import mock

from function import app

with open('crc/template.yaml', 'r') as f:
    TABLENAME = re.search(r'TableName: (.*)?', f.read()).group(1)

@mock.patch.dict(os.environ, {"TABLENAME": TABLENAME})
def test_lambda_handler():
    # Check AWS creds
    assert "AWS_ACCESS_KEY_ID" in os.environ
    assert "AWS_SECRET_ACCESS_KEY" in os.environ

    ret = app.lambda_handler("", "")

    # Assert return keys
    assert "statusCode" in ret
    assert "headers" in ret
    assert "body" in ret

    # Check for CORS in Headers
    assert "Access-Control-Allow-Origin"  in ret["headers"]
    assert "Access-Control-Allow-Methods" in ret["headers"]
    assert "Access-Control-Allow-Headers" in ret["headers"]

    # Check status code
    if ret["statusCode"] == 200:
        assert "visit_count" in ret["body"]
        assert json.loads(ret["body"])["visit_count"].isnumeric()
    else:
        assert json.loads(ret["body"])["visit_count"] == -1

    return