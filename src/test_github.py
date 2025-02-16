from github import Github, Auth
from typing import TypedDict


url = 'https://github.com'
app_id=1121547
install_id=60185608
ssh_keyfile='/home/arestlel/Downloads/arestlel-github-app-ansible.2025-01-23.private-key.pem'
jwt_expiry=600
github_api_url='https://api.github.com'
repo = 'arestlelansibletest/private_project'


# Read the private key from the file
# private_key=pem.parse_file(ssh_keyfile)

class MaybeBaseURLKwarg(TypedDict, total=False):
    """Schema for optional PyGitHub ``base_url`` keyword argument."""

    base_url: str


with open(ssh_keyfile, 'r') as file:
    private_rsa_key = file.read()

token_permissions = {
}
auth = Auth.AppAuth(app_id, private_rsa_key).get_installation_auth(install_id, None)
g = Github(auth=auth, base_url=github_api_url)

print (auth.token)


## Strongly typed version.
auth = Auth.AppAuth(
    app_id=int(app_id),
    private_key=private_rsa_key,
).get_installation_auth(installation_id=int(install_id))

extra_gh_args: MaybeBaseURLKwarg = {
    'base_url': github_api_url,
} if github_api_url else {}
Github(  # Generate a GitHub App authentication token 
    auth=auth,
    **extra_gh_args,
)

token = f'x-access-token:{auth.token}'
print(token)

print(f'git clone https://{token}@github.com/{repo}')
