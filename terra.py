import subprocess
def terraform_run(command):    
    process=subprocess.run(command, shell=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return process.stdout.decode()
         
              


directory="C:/Users/sarth/Downloads/aws/Wanderlust-Mega-Project/terraform"
command=f'terraform -chdir={directory} init'
command1=f'terraform -chdir={directory} plan'
command2=f'terraform -chdir={directory} apply -auto-approve'
command3=f'terraform -chdir={directory} destroy -auto-approve'




output=terraform_run(command)
print(output)

 
