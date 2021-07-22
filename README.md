# netpyfile
netpyfile is a pure python 3 file transfer program
<br>
it allows for file transfer 2 computers
<br>
with this, you can choose a directory to serve and configure the ip and port
<br>
and configure the client to connect to your server

# configuring and using the server
to use the server you need to have your servers ip and the port
<br>
run this in a terminal:
```
ip a
```
and get your servers ip by finding the network interface you use
<br>
once you have your server ip, open the `server.py` file and look for a string thats called `myip` and edit that to your ip
<br>
you may also change the port by editing the `port` integer if needed
<br>
to change what directory the server serves, edit the `serverpath` string
<br>
after you are done run the python file:
```
python server.py
```
## enabling authentication (optional)
first set `authenabled` to 1 in `server.py`
<br>
then you need to generate a md5 hash
<br>
to do that run `passgen.py`
```
python passgen.py
```
after running that follow the steps and you will have a md5 hash
<br>
put that md5 hash in string called `authhash` in `server.py`
# configuring and using the client
to use the client, you need to have your servers ip and port
<br>
once you have this, configure the client by opening the python file and changing `connip` to the server ip and `connport` to the port
<br>
after that, run the python file and you should be connected within a couple of seconds:
```
python client.py
```
## authors
* **DebianProgrammer** - *Initial work* - [DebianProgrammer](https://github.com/DebianProgrammer)

