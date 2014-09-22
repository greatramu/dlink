dlink
=====

Python scripts to control dlink router. Tested on Dlink GO-RT-AC750

<h5>Dependencies</h5>
<ul>
<li>requests</li>
<li>json</li>
<li>hmac</li>
</ul>

<h5>dlink_dhcp_release_renew.py</h5>
This is a very simple python script created to release and renew the IP address of the router. This work can be further extended to automate basic router tasks. A number of services are available at disposal and can be digged using firefox firebug in router's web management. 

The script will first authenticate using the user id and password. Then the events "WAN-1.DHCP.RELEASE" and "WAN-1.DHCP.RENEW" are issued to request for a new IP address. 

Authentication is performed using simple post methods. HMAC library is used for generating the hex codes required for password encoding. Requests package is used for the get and post methods.

