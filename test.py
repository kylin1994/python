# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import yaml, re, subprocess

class Metadata(object):
    def __init__(self, name):
        self.name = name

class Spec(object):
    def __init__(self, hosts, http):
        self.hosts = hosts
        self.http = http

class Http(object):
    def __init__(self, routes):
        self.route = routes

class Route(object):
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

class Destination:
    def __init__(self, svcName, subset):
        self.host = svcName
        self.subset = subset

class VirtualService(object):


    def __init__(self, svcName, sw):
        self.apiVersion = 'networking.istio.io/v1alpha3'
        self.kind = 'VirtualService'
        self.metadata = Metadata(svcName)
        routes = []
        for subset, weight in sw.items():
            dest = Destination(subset, weight)
            route = Route(dest, weight)
            routes.append(route)
        http = Http(routes)
        hosts = [svcName]
        self.spec = Spec(hosts, http)

dict = {'v1': 100, 'v2': 0}
vs = VirtualService('vouvher', dict)
std_vs = re.sub(r'!!python/object:__main__\.[a-zA-Z]*', '', yaml.dump(vs), re.M)
f = open(r'C:\Users\Thinkpad\Desktop\test.yaml','w')
print(yaml.dump(std_vs, f))
print(type(yaml.dump(vs)))
print(type('ss'))
