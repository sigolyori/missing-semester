most_recent_mtime = 10000
for file in directory:
	mtime = file.get_mtime()
	if mtime < most_recent_mtime:
		most_recent_mtime = mtime
		
