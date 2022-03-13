from src.orgs import Org
from src.repos import Repo


class UsersAPI:
    """
    This exposes the Users API and returns User objects that can be interacted with.

    Errors from the request are propagated up.
    """

    def __init__(self, _github_api):
        self._github_api = _github_api

    def me(self):
        ret = self._github_api.make_request("GET", "user")
        json = ret.json()
        return User(self._github_api, **json)

    def my_orgs(self):
        ret = self._github_api.make_request("GET", "user/orgs")
        json = ret.json()
        return [Org(self._github_api, **j) for j in json]

    def get(self, username: str):
        ret = self._github_api.make_request("GET", f"users/{username}")
        if ret.status_code == 404:
            return None
        json = ret.json()
        return User(self._github_api, **json)


class User:
    """
    This class represents an instance of a user.
    """

    def __init__(self, _github_api, **kwargs):
        self._github_api = _github_api
        self.login = kwargs["login"]
        self.id = kwargs["id"]
        self.public_repo_count = kwargs["public_repos"]
        # Can only get for /me
        self.private_repo_count = kwargs.get("total_private_repos")
        self.json = kwargs

    def get_orgs(self):
        ret = self._github_api.make_request("GET", f"users/{self.login}/orgs")
        if ret.status_code == 404:
            return None
        json = ret.json()
        return [Org(self._github_api, **j) for j in json]

    def get_repos(self):
        ret = self._github_api.make_request("GET", f"users/{self.login}/repos")
        if ret.status_code == 404:
            return None
        json = ret.json()
        return [Repo(self._github_api, **j) for j in json]

    def _repr_html_(self):
        return """
        <h1>User</h1>
        <table>
            <tr>
                <th>Key</th><th>Value</th>
            </tr>
            <tbody>
                <tr>
                    <td>Login</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>id</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td># of Public Repos</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td># of Private Repos</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>Additional fields</td>
                    <td><a title="{}">{} additional fields</a></td>
                </tr>
        
    """.format(self.login,
               self.id,
               self.public_repo_count,
               self.private_repo_count, ",".join(self.json.keys()), len(self.json.keys()))
