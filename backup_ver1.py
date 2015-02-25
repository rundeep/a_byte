import os
import time

source = ['/home/bob/src/py', '/home/bob/cisco']
target_dir = '/home/bob/backup'
target = target_dir + os.sep + \
        time.strftime('%Y%m%d%H%M%S')

if not os.path.exists('target_dir'):
    os.mkdir('target_dir')

zip_command = 'zip -r {0} {1}'.format(target,
                                        ' '.join(source))

print 'Zip command is:'
print zip_command
print 'Running:'
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
