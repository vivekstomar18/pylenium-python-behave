# #here we create configuration methods
# import pytest
# import json
# import os
# from datetime import datetime
# @pytest.hookimpl( tryfirst=True)
# def pytest_configure(config):
#     report_dir="reports"
#     now = datetime.now().strftime("%Y%m%d_%H-%M-%S")
#
#
# @pytest.fixture(scope='session', autouse=True)
# def setup_teardown(request):
#     print("Setting up")
#     yield
#     print("Teardown")
# @pytest.fixture
# def load_user_data():
#     json_file_path = os.path.join(os.path.dirname(__file__), "data" "user_data.json")
#     with open(json_file_path) as json_file:
#         data = json.load(json_file)
#         return data
#
