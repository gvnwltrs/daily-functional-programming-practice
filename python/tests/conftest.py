import warnings

def pytest_configure(config):
    # Ignore specific warning
    warnings.filterwarnings("ignore", message="verify_ssl is deprecated, use ssl=False instead", category=DeprecationWarning)
