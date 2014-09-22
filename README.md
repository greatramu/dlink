dlink
=====

python scripts to control dlink router. Tested on Dlink GO-RT-AC750

<h5>dlink_dhcp_release_renew.py</h5>
This simple python script will first authenticate using the user id and password. Then the events WAN-1.DHCP.RELEASE and WAN-1.DHCP.RENEW are used to request for a new IP address

Authentication is performed using simple post methods. HMAC library is used for generating the hex codes required for password encoding. Requests package is used for the get and post methods.

