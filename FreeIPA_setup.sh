FreeIPA setup


# we need ipa-server and ipa-server-dns rpm to set up our FreeIPA server
yum install ipa-server
yum install ipa-server-dns


yum install ipa-client 
yum install ipa-admintools

echo 192.168.0.168 ipa.hqvfx.auth >> /etc/hosts
echo ipa.hqvfx.auth > /etc/hostname


#FIREWALL
firewall-cmd --permanent --add-service=dns 
firewall-cmd --permanent --add-service=ntp
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --permanent --add-service=ldap
firewall-cmd --permanent --add-service=ldaps
firewall-cmd --permanent --add-service=kerberos
firewall-cmd --permanent --add-service=kpasswd
firewall-cmd --reload



# START SETUP
ipa-server-install --setup-dns

# To obtain a ticket-granting ticket, run the following command:
kinit admin




