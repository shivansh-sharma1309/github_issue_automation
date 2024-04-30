import requests

if __name__ == '__main__':
    token = 'your_github_token'
    username = input('Enter username : ')
    # token = input('Enter your github token : ')
    repository1 = input('Enter name of first repository : ')
    repository2 = input('Enter name of second repository : ')
    label = input('Enter the label name for check : ')
    repo_url1 = f'https://api.github.com/repos/{username}/{repository1}/issues'
    repo_url2 = f'https://api.github.com/repos/{username}/{repository2}/issues'


    headers = {'Authorization':f'token {token}'}

    response1 = requests.get(repo_url1,headers=headers)
    response2 = requests.get(repo_url2,headers=headers)

    if response1.status_code == 200 and response2.status_code == 200: 
    
        #converting response object to json format
        response1 = response1.json()
        response2 = response2.json()
        issues1 = []
        issues2 = []
        for i in range(len(response1)) : 
            data = i
            description = response1[i]['body']
            for l in response1[i]['labels'] :
                if l['name'] == label : 
                    issues1.append({'data':data,'description':description,'title':response1[i]['title']})
        
        for i in range(len(response2)) :
            data = i 
            description = response2[i]['body']
            for l in response2[i]['labels'] :
                if l['name'] == label : 
                    issues2.append({'data':data,'description':description,'title':response2[i]['title']})
        

        issues_on_x86_and_power = []
        issues_on_x86_not_on_power = []
        for i in range(len(issues1)) :
            flag = 0 
            for j in range(len(issues2)) :
                if issues1[i]['description'] == issues2[j]['description']  or issues1[i]['title'] == issues2[j]['title'] : 
                    issues_on_x86_and_power.append([issues1[i]['data'],issues2[j]['data']]) 
                    flag = 1
            if flag == 0 : 
                issues_on_x86_not_on_power.append(issues1[i]['data'])

        print('\n\n   -------------------------------------   \n\n')        

        #printing issues that are issued on x86 but not issued on power         
        if issues_on_x86_not_on_power == [] : 
            print(f'No issues of repository {repository1} has left unissued on repository {repository2}.')
        else : 
            for issue in issues_on_x86_not_on_power : 
                print(f'The issue with title ::  {response1[issue]['title']}  ::  of repository {repository1} has a not issued on repository {repository2}')
        
        print('\n\n   -------------------------------------   \n\n')

        #printing issues that are issued on both x86 and power 
        if issues_on_x86_and_power == [] : 
            print(f'No two issues of repositories {repository1} and {repository2} have same {label} label and description ')
        else : 
            for issue in issues_on_x86_and_power : 
                print(f'The issue with title ::  {response1[issue[0]]['title']}  ::  of repository {repository1} has a same {label} label or description as of issue with title ::  {response2[issue[1]]['title']}  ::  of repository {repository2}\n')
        
        print('\n\n   -------------------------------------   \n\n')
    
    else : 
    
        print('Something went wrong')
    
            
