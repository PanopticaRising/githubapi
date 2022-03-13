from src.helpers import dict_to_td


class RepoAPI:

    def __init__(self, github_api):
        self._github_api = github_api

    def get(self, owner: str, name: str):
        ret = self._github_api.make_request("GET", f"repos/{owner}/{name}")
        if ret.status_code == 404:
            return None
        json = ret.json()
        return Repo(self._github_api, **json)


class Repo:

    def __init__(self, github_api, **kwargs):
        self._github_api = github_api
        self.name = kwargs["name"]
        self.id = kwargs["id"]
        self.desc = kwargs.get("description")
        self.json = kwargs

    def _repr_html_(self):
        return """
            <table>
                {}
            </table>
        """.format(dict_to_td(self.json))
