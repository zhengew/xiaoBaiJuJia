import os
os.makedirs('glance/api')
os.makedirs('glance/cmd')
os.makedirs('glance/db')
l = []
l.append(open('glance/__init__.py','w'))
l.append(open('glance/api/__init__.py','w'))
l.append(open('glance/api/policy.py','w'))
l.append(open('glance/api/versions.py','w'))
l.append(open('glance/cmd/__init__.py','w'))
l.append(open('glance/cmd/manage.py','w'))
l.append(open('glance/db/models.py','w'))
map(lambda f:f.close() ,l)