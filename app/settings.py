# fill this out and rename to settings.py
AUTH_ENABLED = True    # set to True to enable LDAP SSL auth.
                        # Note: when set to False you will only be able to
                        # login as TESTUSER

DEBUG = True            # set to False in production

DB_PATH = '/Users/james.denness/virtualenv/graphite-boards/graphite-boards/db/db.db'              # full path to a sqllite db. this will be created
                        # automatically on first start

LDAP_SERVER = ""        # fqdn for ldap server
LDAP_BASEDN = ""        # basedn e.g. "c=gb,dc=mycompany,dc=com"
LDAP_OU = ""            # search ou for user e.g. "ou=People"
LDAP_CERTIFICATE  = ""  # full path to your LDAP ssl certificate
LDAP_ENABLED = False    # Enable LDAP based auth
