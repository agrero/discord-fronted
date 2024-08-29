
import requests
from typing import Any


class RequestHandler:

    def __init__(self, 
        json:dict,
        commands:list,
        url:str='http://0.0.0.0:8000', # database url
        headers:dict={'Content-Type':'application/json'}
    ) -> None:
        
        self.url = url
        self.json = json
        self.headers = headers
        self.commands = commands

    def assess_method(self, name:str):
        """
        this should take in whatever the name of the 
        function is and return the method.
        
        name:str = get/post/put method

        returns: post dependent upon the method specified in name
        """
        # returns the method call
        # THIS SHOULD JUST BE REQUESTS, GET/POST/ETC
        return getattr(self, name)()


    # THESE SHOULD BE WHAT I GETATTR FOR INSTEAD OF THE CLASS METHOD
    def get(self):
        post = requests.get(
            url=f'{self.url}/{'/'.join(self.commands)}',
            headers=self.headers,
            json=self.json
        )

        return post

    def put(self):
        post = requests.put(
            url=f'{self.url}/{'/'.join(self.commands)}',
            headers=self.headers,
            json=self.json
        )

        return post

    def post(self):
        post = requests.post(
            url=f'{self.url}/{'/'.join(self.commands)}',
            headers=self.headers,
            json=self.json
        )

        return post