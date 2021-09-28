#https://pythonprinciples.com/challenges/Online-status/

def online_count(statuses):
    count = 0
    for s in statuses:
        if statuses[s] == "online":
            count = count+1
    return count
    
statuses = { 
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }
    
print(online_count(statuses))
