"""
Developed by Alex Ermolaev (Abionics)
Email: abionics.dev@gmail.com
Part of Evertrace project (https://ever.ninja), private code source
"""

__version__ = '2.0.0'

from tvmbase.models.network import NetworkFactory, Network

NetworkFactory.add_custom(Network(
    name='red',
    endpoints=['net.ton.red'],
    everlive_domain='net.ton.red',
    everscan_domain='',
))
