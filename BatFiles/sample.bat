cd ..
echo %cd%
python -m pytest -s -v --env dev %cd%/TestCases/testsuites/test_sample.py --html=Reports/htmlreports/Report.html --self-contained-html --capture=sys --show-capture=log --alluredir=Reports/allurereports