########################################################################################################################
# LDAP Authentication Settings
########################################################################################################################

import ldap
import os
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

LDAP_SERVER = 'ipa.hqvfx.auth'
AUTH_LDAP_SERVER_URI = 'ldap://' + LDAP_SERVER

AUTH_LDAP_BIND_DN = 'uid=admin,cn=users,cn=accounts,dc=hqvfx,dc=auth'
AUTH_LDAP_BIND_PASSWORD = os.environ.get('MY_PASS')
AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,cn=users,cn=accounts,dc=hqvfx,dc=auth'

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail'
}

AUTH_LDAP_GROUP_BASE = "cn=groups,cn=accounts,dc=hqvfx,dc=auth"
AUTH_LDAP_GROUP_FILTER = "(objectClass=groupOfNames)"
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(AUTH_LDAP_GROUP_BASE,
                                    ldap.SCOPE_SUBTREE, AUTH_LDAP_GROUP_FILTER)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_staff': 'cn=ipausers,' + AUTH_LDAP_GROUP_BASE,
    'is_support': 'cn=ipausers,' + AUTH_LDAP_GROUP_BASE,
    'is_superuser': 'cn=ipausers,' + AUTH_LDAP_GROUP_BASE,
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
