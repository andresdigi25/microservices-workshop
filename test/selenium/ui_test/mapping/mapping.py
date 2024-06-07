environment = {'dev': 'http://localhost/svelte/non-sso-login',
               'test': 'http://localhost/svelte/non-sso-login',
               'uat': 'http://localhost/svelte/non-sso-login',
               'prod': 'http://localhost/svelte/non-sso-login'}


def map_environment(env):
    return environment[env]

