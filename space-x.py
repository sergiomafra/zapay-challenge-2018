#!/usr/bin/env python3
import argparse
import requests

class SpaceX:

    def fetch_response(self, url):
        ''' Fetch and return the url response '''

        # Try 3 times before giving up
        failed = 0
        worked = False

        while failed < 3 and not worked:
            try:
                response = requests.get(url, timeout=10)
            except requests.exceptions.Timeout as e:
                failed += 1
            except requests.exceptions.ConnectionError as e:
                failed += 1
            except requests.exceptions.RequestException as e:
                failed += 1
            else:
                worked = True

        if failed == 3:
            return ('API can\'t be reached or you are experiencing some '
                    'connectivity issues. Requests returned status code:'
                    ' {}'.format(requests.status_code))

        return response.json()

    def print_data(self, response):
        print( ('\n\tMission Name: {}\n\tRocket Name: {}\n\tDate: {}'
                '\n\tLaunch Site: {}\n\tDescription: {}'.format(
                response['mission_name'],
                response['rocket']['rocket_name'],
                response['launch_date_utc'],
                response['launch_site']['site_name_long'],
                response['details'])))


    def extract(self, url, mult=0):
        ''' Extrating information on data acquired and
            printing on the screen '''

        response = self.fetch_response(url)

        if type(response) == str:
            print(response)
            return
        elif mult == 0:
            self.print_data(response)
        elif mult == 1:
            for element in response:
                self.print_data(element)

    def run(self):
        ''' Run, Forest! Run! '''

        ## CREATING THE PARSER

        parser = argparse.ArgumentParser(description='CLI for Space X launches')

        # Creating arguments
        parser.add_argument(
                '-n',
                '--next',
                help='Shows data about the next launch',
                action='store_true')
        parser.add_argument(
                '-l',
                '--latest',
                help='Shows data about the latest launch',
                action='store_true')
        parser.add_argument(
                '-u',
                '--upcoming',
                help='Shows data about the upcoming launches',
                action='store_true')
        parser.add_argument(
                '-p',
                '--past',
                help='Shows data about the past launches',
                action='store_true')

        # Collectings args from user
        args = parser.parse_args()

        # Treating args
        if args.next:
            self.extract('https://api.spacexdata.com/v3/launches/next')
        if args.latest:
            self.extract('https://api.spacexdata.com/v3/launches/latest')
        if args.upcoming:
            self.extract('https://api.spacexdata.com/v3/launches/upcoming',
                    mult=1)
        if args.past:
            self.extract('https://api.spacexdata.com/v3/launches/past',
                    mult=1)

if __name__ == '__main__':
    spacex = SpaceX()
    spacex.run()

