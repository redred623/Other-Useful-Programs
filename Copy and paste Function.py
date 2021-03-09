import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

print('Hello please put your text into the input')
entry = input('-> ')
copy2clip(entry)