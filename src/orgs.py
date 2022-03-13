from src.helpers import dict_to_td
from src.repos import Repo


class OrgAPI:
    def __init__(self, github_api):
        self._github_api = github_api

    def get(self, name):
        ret = self._github_api.make_request("GET", f"orgs/{name}")
        if ret.status_code == 404:
            return None
        json = ret.json()
        return Org(self._github_api, **json)


class Org:

    def __init__(self, github_api, **kwargs):
        self._github_api = github_api
        self.login = kwargs["login"]
        self.desc = kwargs["description"]
        self.json = kwargs

    def get_repositories(self):
        ret = self._github_api.make_request("GET", f"orgs/{self.login}/repos")
        arr = ret.json()
        return [Repo(self._github_api, **j) for j in arr]

    # TODO: Add a table with all the URLs.
    def _repr_html_(self):
        return """
            <div>
                <h1>{}<h1>
                <p>{}</p>
            </div>
            <table>
                {}
            </table>
        """.format(self.login, self.desc, dict_to_td(self.json))
