# Playwright---Python

Indications:

- It is necessary that the test you create initially have test_name.py written inside the test file.
  
- The file name conftest.py is demonized for the test environment configuration. If you change the file name, Playwright will not be able to recognize this configuration file.
Testing the use of Playwright with python.

```
https://playwright.dev/python/docs/intro
```

# Install the Pytest plugin:

```
pip install pytest-playwright
```

# Install the required browsers:

```
playwright install
```

# Executing test 

Run test 

```
pytest test_name.py
```

# Open codegen 

You can open the browser and with this tool select the element to obtain its locator.

```
playwright codegen https://example.com
```

* More informacion in : https://playwright.dev/python/docs/codegen-intro#running-codegen
