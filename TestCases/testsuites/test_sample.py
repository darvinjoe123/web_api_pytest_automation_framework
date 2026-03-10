import time
import ast
import pytest
from CommonClass.api_utils.AuthToken import getCurrentSessionToken
from CommonClass.web_utils.CommonUiActions import (login,logout,notification)
from Requests.methods.PostRequests.postcommons.POST_CommonActions import post_user
from Requests.methods.PutRequests.putcommons.PUT_CommonActions import put_user
from Requests.methods.GetRequests.getcommons.GET_CommonActions import get_user


@pytest.mark.usefixtures("env_setup")
class TestSample:
# ++++++++++++++++++ sample_test_case ++++++++++++++++++ Start 
    @pytest.mark.parametrize('readPayLoadJsonWithUUID', ["Requests/Payload/Json/Sample_Payload.json"], indirect=['readPayLoadJsonWithUUID'])
    def test_sample_test_case(self,apiTestData, readPayLoadJsonWithUUID, configLogger):
        # post_user(apiTestData=apiTestData, endpointkey="testpost", configLogger=configLogger, readPayLoadJson=readPayLoadJsonWithUUID, headers=ast.literal_eval(apiTestData['Headers']['ContentTypeJson']))
        # print("\n ========================================================================================================================================================== \n")    
        # put_user(apiTestData=apiTestData, endpointkey="testput", configLogger=configLogger, readPayLoadJson=readPayLoadJsonWithUUID, headers=ast.literal_eval(apiTestData['Headers']['ContentTypeJson']))
        # print("\n ========================================================================================================================================================== \n")
        # time.sleep(2)
        get_user(apiTestData=apiTestData, endpointkey="testget",configLogger=configLogger)
        print("\n ========================================================================================================================================================== \n")
@pytest.mark.usefixtures("test_setup")
class TestSample1:
    def test_sample_ui_test_case(self,uiTestData,configLogger):
        login(uiTestData=uiTestData)
        logout
        notification