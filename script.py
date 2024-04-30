import requests

if __name__ == '__main__':
    
    token = 'your_github_token'
    username_x86 = input('Enter username of x86 repository : ')
    username_power = input('Enter username of power repository : ')
    repository_x86 = input('Enter name of x86 repository : ')
    repository_power = input('Enter name of power repository : ')
    label = input('Enter label to be checked : ')
    state = input('State of issue(all/open/closed) : ')
    url_x86 = f'https://github.ibm.com/api/v3/repos/{username_x86}/{repository_x86}/issues'
    issues_on_x86 = []
    session = requests.session() 
    session.headers.update({'Authorization':f'token {token}'})
    params = {'state':state,'labels':label}
    #fetching issues with requirred label from our repository    
    while url_x86 != '': 
        response_x86 = session.get(url_x86,params=params)
        if response_x86.status_code == 200 :
            if 'next' in response_x86.links :
                url_x86 = response_x86.links['next']['url'] 
            else : 
                url_x86 = '' 
            response_x86 = response_x86.json()
            issues_on_x86.extend(response_x86)
        else : 
            print('Something went wrong while fetching x86 issues!!')
            break 
        
    print(f'Issues with {label} label on repository {repository_x86} : ')
    print(len(issues_on_x86))
    
    print('\n   -------------------------------------   \n')        

    #printing issues that are issued on x86 with requirred label           
    for issue in issues_on_x86 : 
        print(f'The issue with title ::  {issues_on_x86[issue]['title']}  ::  of repository {repository_x86} has a not issued on repository {repository_power}')
        
    print('\n   -------------------------------------   \n')
