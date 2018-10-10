# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import yaml, re, subprocess, os

class Metadata(yaml.YAMLObject):
    yaml_tag = u'!Metadata'
    def __init__(self, name):
        self.name = name

class Spec(yaml.YAMLObject):
    yaml_tag = u'!Spec'
    def __init__(self, hosts, http):
        self.hosts = hosts
        self.http = http

class Http(yaml.YAMLObject):
    yaml_tag = u'!Http'
    def __init__(self, routes):
        self.route = routes

class Route(yaml.YAMLObject):
    yaml_tag = u'!Route'
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

class Destination(yaml.YAMLObject):
    yaml_tag = u'!Destination'
    def __init__(self, svcName, subset):
        self.host = svcName
        self.subset = subset

class VirtualService(yaml.YAMLObject):
    yaml_tag = u'!VirtualService'
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

def noop(self, *args, **kw):
    pass
yaml.emitter.Emitter.process_tag = noop

dict = {'v1': 100, 'v2': 0}
vs = VirtualService('vouvher', dict)
print(yaml.dump(vs))
# std_vs = re.sub(r'!!python/object:__main__\.[a-zA-Z]*\s', '', yaml.dump(vs), re.M)
# s = re.sub(r'\\', '', std_vs, re.M)
# f = open(r'./test.yaml', 'w')
# print(yaml.dump(std_vs))
