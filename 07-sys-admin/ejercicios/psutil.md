# psutil — Process and system utilities

- Biblioteca multiplataforma para recuperar información sobre procesos en ejecución y utilización del sistema (CPU, memoria, discos, red, sensores) en Python
- Implementa muchas funcionalidades que ofrecen las herramientas clásicas de línea de comandos de UNIX como `ps`, `top`, `iotop`, `lsof`, `netstat`, `ifconfig`, `free` y otras

<small><a href="https://psutil.readthedocs.io/en/latest/">Documentación oficial</a></small>

#### Instalación


```python
! pip install psutil
```

    Requirement already satisfied: psutil in /mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/lib/python3.8/site-packages (5.8.0)
    [33mWARNING: You are using pip version 21.1.1; however, version 21.1.2 is available.
    You should consider upgrading via the '/mnt/c/Users/alicia/workspace/eoi/eoi-administracion-sistemas/.venv/bin/python3 -m pip install --upgrade pip' command.[0m


## CPU


```python
import psutil

# https://psutil.readthedocs.io/en/latest/index.html?highlight=cpu_times#psutil.cpu_count
psutil.cpu_count()
```




    12




```python
# https://psutil.readthedocs.io/en/latest/index.html?highlight=cpu_times#psutil.cpu_times
psutil.cpu_times()
```




    scputimes(user=16.38, nice=0.0, system=49.05, idle=69481.99, iowait=1.93, irq=0.0, softirq=1.67, steal=0.0, guest=0.0, guest_nice=0.0)




```python
psutil.cpu_stats()
```




    scpustats(ctx_switches=4746097, interrupts=955112, soft_interrupts=1239296, syscalls=0)




```python
for x in range(3):
    print(psutil.cpu_percent(interval=1))
```

    0.1
    0.0
    0.0



```python
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))
```

    [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]



```python
for x in range(3):
    print(psutil.cpu_times_percent(interval=1, percpu=False))
```

    scputimes(user=0.0, nice=0.0, system=0.1, idle=99.8, iowait=0.1, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
    scputimes(user=0.1, nice=0.0, system=0.1, idle=99.8, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
    scputimes(user=0.0, nice=0.0, system=0.0, idle=100.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)


## Memoria RAM


```python
psutil.virtual_memory()
```




    svmem(total=13184966656, available=12711305216, percent=3.6, used=276357120, free=12823138304, active=215101440, inactive=25030656, buffers=10919936, cached=74551296, shared=69632, slab=47034368)




```python
psutil.swap_memory()
```




    sswap(total=4294967296, used=0, free=4294967296, percent=0.0, sin=0, sout=0)



## Discos


```python
psutil.disk_partitions()
```




    [sdiskpart(device='/dev/sdb', mountpoint='/', fstype='ext4', opts='rw,relatime,discard,errors=remount-ro,data=ordered', maxfile=255, maxpath=4096)]




```python
psutil.disk_usage('/')
```




    sdiskusage(total=269490393088, used=2709807104, free=253019914240, percent=1.1)




```python
psutil.disk_io_counters(perdisk=False)
```




    sdiskio(read_count=1637, write_count=10221, read_bytes=55085056, write_bytes=4321062912, read_time=879, write_time=22573, read_merged_count=1591, write_merged_count=2276, busy_time=32750)



## Network


```python
psutil.net_io_counters(pernic=True)
```




    {'sit0': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
     'bond0': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
     'lo': snetio(bytes_sent=7093806, bytes_recv=7093806, packets_sent=6039, packets_recv=6039, errin=0, errout=0, dropin=0, dropout=0),
     'eth0': snetio(bytes_sent=61250, bytes_recv=6461268, packets_sent=761, packets_recv=1339, errin=0, errout=0, dropin=0, dropout=0),
     'dummy0': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0)}




```python
psutil.net_connections(kind='tcp')
```




    [sconn(fd=60, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=8888), raddr=addr(ip='127.0.0.1', port=32882), status='ESTABLISHED', pid=240),
     sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=32882), raddr=addr(ip='127.0.0.1', port=8888), status='ESTABLISHED', pid=None),
     sconn(fd=4, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=8888), raddr=(), status='LISTEN', pid=240),
     sconn(fd=32, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=49972), raddr=addr(ip='127.0.0.1', port=33537), status='ESTABLISHED', pid=240),
     sconn(fd=64, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=44762), raddr=addr(ip='127.0.0.1', port=51727), status='ESTABLISHED', pid=240),
     sconn(fd=39, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=44779), raddr=addr(ip='127.0.0.1', port=33700), status='ESTABLISHED', pid=340),
     sconn(fd=42, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=35719), raddr=addr(ip='127.0.0.1', port=48520), status='ESTABLISHED', pid=361),
     sconn(fd=42, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=33700), raddr=addr(ip='127.0.0.1', port=44779), status='ESTABLISHED', pid=240),
     sconn(fd=11, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=57827), raddr=(), status='LISTEN', pid=340),
     sconn(fd=15, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=53721), raddr=(), status='LISTEN', pid=361),
     sconn(fd=43, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=48211), raddr=addr(ip='127.0.0.1', port=58196), status='ESTABLISHED', pid=316),
     sconn(fd=39, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=43958), raddr=addr(ip='127.0.0.1', port=54739), status='ESTABLISHED', pid=240),
     sconn(fd=11, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=37585), raddr=(), status='LISTEN', pid=316),
     sconn(fd=39, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=37585), raddr=addr(ip='127.0.0.1', port=39366), status='ESTABLISHED', pid=316),
     sconn(fd=44, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=47570), raddr=addr(ip='127.0.0.1', port=43989), status='ESTABLISHED', pid=240),
     sconn(fd=70, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=48520), raddr=addr(ip='127.0.0.1', port=35719), status='ESTABLISHED', pid=240),
     sconn(fd=58, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=33514), raddr=addr(ip='127.0.0.1', port=44779), status='ESTABLISHED', pid=240),
     sconn(fd=63, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=44758), raddr=addr(ip='127.0.0.1', port=51727), status='ESTABLISHED', pid=240),
     sconn(fd=22, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=38401), raddr=(), status='LISTEN', pid=316),
     sconn(fd=15, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=48211), raddr=(), status='LISTEN', pid=316),
     sconn(fd=13, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=35719), raddr=(), status='LISTEN', pid=361),
     sconn(fd=68, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=52554), raddr=addr(ip='127.0.0.1', port=53721), status='ESTABLISHED', pid=240),
     sconn(fd=41, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=44779), raddr=addr(ip='127.0.0.1', port=33514), status='ESTABLISHED', pid=340),
     sconn(fd=30, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=58190), raddr=addr(ip='127.0.0.1', port=48211), status='ESTABLISHED', pid=240),
     sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=33042), raddr=addr(ip='127.0.0.1', port=8888), status='TIME_WAIT', pid=None),
     sconn(fd=36, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=53721), raddr=addr(ip='127.0.0.1', port=52544), status='ESTABLISHED', pid=361),
     sconn(fd=40, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=50977), raddr=addr(ip='127.0.0.1', port=57612), status='ESTABLISHED', pid=361),
     sconn(fd=22, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=41961), raddr=(), status='LISTEN', pid=340),
     sconn(fd=42, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=54739), raddr=addr(ip='127.0.0.1', port=43778), status='ESTABLISHED', pid=340),
     sconn(fd=17, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=54739), raddr=(), status='LISTEN', pid=340),
     sconn(fd=22, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=33959), raddr=(), status='LISTEN', pid=361),
     sconn(fd=62, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=52544), raddr=addr(ip='127.0.0.1', port=53721), status='ESTABLISHED', pid=240),
     sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=60606), raddr=addr(ip='127.0.0.1', port=8888), status='ESTABLISHED', pid=None),
     sconn(fd=38, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=53595), raddr=addr(ip='127.0.0.1', port=44646), status='ESTABLISHED', pid=316),
     sconn(fd=35, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=58196), raddr=addr(ip='127.0.0.1', port=48211), status='ESTABLISHED', pid=240),
     sconn(fd=40, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=48211), raddr=addr(ip='127.0.0.1', port=58190), status='ESTABLISHED', pid=316),
     sconn(fd=17, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=53595), raddr=(), status='LISTEN', pid=316),
     sconn(fd=26, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=44646), raddr=addr(ip='127.0.0.1', port=53595), status='ESTABLISHED', pid=240),
     sconn(fd=30, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=60465), raddr=(), status='LISTEN', pid=316),
     sconn(fd=37, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=51727), raddr=addr(ip='127.0.0.1', port=44758), status='ESTABLISHED', pid=361),
     sconn(fd=30, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=43913), raddr=(), status='LISTEN', pid=340),
     sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=33044), raddr=addr(ip='127.0.0.1', port=8888), status='TIME_WAIT', pid=None),
     sconn(fd=13, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=33537), raddr=(), status='LISTEN', pid=316),
     sconn(fd=25, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=44642), raddr=addr(ip='127.0.0.1', port=53595), status='ESTABLISHED', pid=240),
     sconn(fd=38, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=51727), raddr=addr(ip='127.0.0.1', port=44762), status='ESTABLISHED', pid=361),
     sconn(fd=40, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=43989), raddr=addr(ip='127.0.0.1', port=47570), status='ESTABLISHED', pid=340),
     sconn(fd=17, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=51727), raddr=(), status='LISTEN', pid=361),
     sconn(fd=66, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=57612), raddr=addr(ip='127.0.0.1', port=50977), status='ESTABLISHED', pid=240),
     sconn(fd=59, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=43778), raddr=addr(ip='127.0.0.1', port=54739), status='ESTABLISHED', pid=240),
     sconn(fd=28, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=39366), raddr=addr(ip='127.0.0.1', port=37585), status='ESTABLISHED', pid=240),
     sconn(fd=11, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=50977), raddr=(), status='LISTEN', pid=361),
     sconn(fd=40, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=35066), raddr=addr(ip='127.0.0.1', port=57827), status='ESTABLISHED', pid=240),
     sconn(fd=36, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=54739), raddr=addr(ip='127.0.0.1', port=43958), status='ESTABLISHED', pid=340),
     sconn(fd=38, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=57827), raddr=addr(ip='127.0.0.1', port=35066), status='ESTABLISHED', pid=340),
     sconn(fd=36, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=53595), raddr=addr(ip='127.0.0.1', port=44642), status='ESTABLISHED', pid=316),
     sconn(fd=30, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=59365), raddr=(), status='LISTEN', pid=361),
     sconn(fd=41, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=33537), raddr=addr(ip='127.0.0.1', port=49972), status='ESTABLISHED', pid=316),
     sconn(fd=13, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=43989), raddr=(), status='LISTEN', pid=340),
     sconn(fd=15, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=44779), raddr=(), status='LISTEN', pid=340),
     sconn(fd=23, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=8888), raddr=addr(ip='127.0.0.1', port=60606), status='ESTABLISHED', pid=240),
     sconn(fd=41, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='127.0.0.1', port=53721), raddr=addr(ip='127.0.0.1', port=52554), status='ESTABLISHED', pid=361)]




```python
psutil.net_if_addrs()
```




    {'lo': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None),
      snicaddr(family=<AddressFamily.AF_INET6: 10>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),
      snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:00:00:00:00', netmask=None, broadcast=None, ptp=None)],
     'eth0': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='172.17.46.150', netmask='255.255.255.240', broadcast='172.17.46.159', ptp=None),
      snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::215:5dff:fec3:43f6%eth0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
      snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:15:5d:c3:43:f6', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)],
     'bond0': [snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='c2:3e:6b:32:c9:eb', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)],
     'dummy0': [snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='7a:a8:dc:45:68:bc', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)],
     'sit0': [snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:00:00:00:00', netmask=None, broadcast=None, ptp=None)]}




```python
psutil.net_if_stats()
```




    {'sit0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1480),
     'bond0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=65535, mtu=1500),
     'lo': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=65536),
     'eth0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=10000, mtu=1500),
     'dummy0': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500)}


