import requests

'''
OAuth 2.0
code=8HjcFecN3mY80EcfUabPst6NDdUaM6MPtKESX4qWXZMBvAWahnMoA3JhT31qEhtC_eu-N
Permanent token:
eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjM3NzYwNDcsXCJpXCI6NzAzMzgxMyxcImNcIjo0NjE4OTEyLFwidVwiOjgxODQ2NzQsXCJyXCI6XCJVU1wiLFwic1wiOltcIldcIixcIkZcIixcIklcIixcIlVcIixcIktcIixcIkNcIixcIkRcIixcIkFcIixcIkxcIl0sXCJ6XCI6W10sXCJ0XCI6MH0iLCJpYXQiOjE1ODgzMzc5MjR9.bqG2yUjBWFBb48Tq5YcD5PC0jyYbYVCpSoLdGVcktwE

List of available spaces
Title            ID
---------------------------
Team , IEADTHRPI4O6BGBK
Personal , IEADTHRPI4O6BFEN
Software Dev Team , IEADTHRPI4O6BGCJ

List of available folders
Title            ID
---------------------------
Root , IEADTHRPI7777777
Recycle Bin , IEADTHRPI7777776
0. How-to Guide , IEADTHRPI4O6BGCK
1. Current Sprint , IEADTHRPI4O6BGCL
2. Backlog , IEADTHRPI4O6BGCM
3. Completed Sprints , IEADTHRPI4O6BGCN
4. Incoming Bugs , IEADTHRPI4O6BGCO
5. Team Meetings , IEADTHRPI4O6BGCP
6. Templates , IEADTHRPI4O6BGCQ
7. Product Initiatives , IEADTHRPI4O6BGCR
Personal , IEADTHRPI4O6BFEN
Retrospective Notes: Sprint 0 , IEADTHRPI4O6BGC3
Retrospective Notes: Sprint 1 , IEADTHRPI4O6BGC4
Software Dev Team , IEADTHRPI4O6BGCJ
Sprint 00 , IEADTHRPI4O6BGCZ
Sprint 01 , IEADTHRPI4O6BGC2
Sprint 02 , IEADTHRPI4O6BGCY
Standalone Project Templates , IEADTHRPI4O6BGDB
Story Templates , IEADTHRPI4O6BGDC
Team , IEADTHRPI4O6BGBK
TestProject , IEADTHRPI4O6DO2C   <---  MY TEST FOLDER

List of available tasks
Title                    ID                   Status
-----------------------------------------------------
Setup OAuth via Python , IEADTHRPKQO6DQRC , Active
Research Wrike API , IEADTHRPKQO6DSHM , Active
Prepare for interview , IEADTHRPKQO6KJ6K , Active
'''

permanent_token = "eyJ0dCI6InAiLCJhbGciOiJIUzI1NiIsInR2IjoiMSJ9.eyJkIjoie1wiYVwiOjM3NzYwNDcsXCJpXCI6NzAzMzgxMyxcImNcIjo0NjE4OTEyLFwidVwiOjgxODQ2NzQsXCJyXCI6XCJVU1wiLFwic1wiOltcIldcIixcIkZcIixcIklcIixcIlVcIixcIktcIixcIkNcIixcIkRcIixcIkFcIixcIkxcIl0sXCJ6XCI6W10sXCJ0XCI6MH0iLCJpYXQiOjE1ODgzMzc5MjR9.bqG2yUjBWFBb48Tq5YcD5PC0jyYbYVCpSoLdGVcktwE"
tasks_url = 'https://www.wrike.com/api/v4/tasks'
headers = {'Authorization': 'Bearer '+permanent_token}


def list_spaces():
    url = f"https://www.wrike.com/api/v4/spaces/"
    res = requests.get(url, headers=headers)
    data = res.json()
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("List of available spaces")
    print("Title            ID")
    print("---------------------------")
    for d in data["data"]:
        print(d["title"], ", "+d["id"])


def list_folders():
    url = f"https://www.wrike.com/api/v4/folders/"
    res = requests.get(url, headers=headers)
    data = res.json()
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("List of available folders")
    print("Title            ID")
    print("---------------------------")
    for d in data["data"]:
        print(d["title"], ", "+d["id"])


def get_tasks(folder_id):
    url = f"https://www.wrike.com/api/v4/folders/{folder_id}/tasks"
    res = requests.get(url, headers=headers)
    data = res.json()
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("List of available tasks")
    print("Title                    ID                   Status")
    print("-----------------------------------------------------")
    for d in data["data"]:
        print(d["title"], ", "+d["id"], ", "+d['status'])


def get_task(task_id):
    url = f"https://www.wrike.com/api/v4/tasks/{task_id}"
    res = requests.get(url, headers=headers)
    data = res.json()
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("List of available tasks")
    print("Title                    ID                   Status")
    print("-----------------------------------------------------")
    for d in data["data"]:
        print(d["title"], ", "+d["id"], ", "+d['status'])
        print(d['dates'])


def create_task(folder_id, title):
    url = f"https://www.wrike.com/api/v4/folders/{folder_id}/tasks"
    headers = {
        'Authorization': 'Bearer ' + permanent_token,
               }
    params = {
        'title': str(title)
    }
    res = requests.post(url, headers=headers, params =params)
    data = res.json()['data'][0]
    print("Created task, titled: "+title+", with ID: "+data['id'])


def update_task(task_id, description, status):
    url = f"https://www.wrike.com/api/v4/tasks/{task_id}"
    headers = {
        'Authorization': 'Bearer ' + permanent_token,
    }
    params = {
        'description': str(description),
        'status': status
    }
    res = requests.put(url, headers=headers, params=params)
    data = res.json()['data'][0]
    print(data['description'])


def delete_task(task_id):
    url = f"https://www.wrike.com/api/v4/tasks/{task_id}"
    headers = {
        'Authorization': 'Bearer ' + permanent_token,
    }
    res = requests.delete(url, headers=headers)
    print("task deleted")

list_spaces()
list_folders()
get_tasks('IEADTHRPI4O6DO2C')
get_task('IEADTHRPKQO6DQRC')

create_task('IEADTHRPI4O6DO2C', 'TestTask1')
update_task('IEADTHRPKQO6ONHE', 'Some dummy description', 'Active')
delete_task('IEADTHRPKQO6ONHE')