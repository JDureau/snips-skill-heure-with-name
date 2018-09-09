import os
os.system("git add action-heure.py")
os.system("git commit -m 'more logs'")
os.system("git push")
os.system("sam install actions")
os.system("sam service log snips-skill-server")