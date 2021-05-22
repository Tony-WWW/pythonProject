#coding=utf-8
import subprocess



p=subprocess.Popen(['df -h'],shell=True,stdout=subprocess.PIPE)

p1=subprocess.Popen(['grep devfs'],shell=True,stdin=p.stdout,stdout=subprocess.PIPE)
output = p1.communicate()[0]
print(output)



