from behave import *
import common.config as cfg
from common.dropbox_tester import DropBoxTester

tester= DropBoxTester(cfg.ACCESS_TOKEN, cfg.FILE_TO_UPLOAD, f'common/resources/{cfg.FILE_TO_UPLOAD}')



@given('we upload file')
def file_upload(context):
    assert tester.file_upload().ok



@when('we check file name')
def file_getmetadata(context):
    response = tester.file_getmetadata()
    assert response.json()['name'] == cfg.FILE_TO_UPLOAD
    assert response.ok


@then('we remove file')
def file_delete(context):
    assert tester.file_delete().ok