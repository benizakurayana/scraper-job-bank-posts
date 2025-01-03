import requests
from Req104 import Req104


class Scraper104:
    """
    This class provides methods to scrape job listings and details from 104 Job Bank using AJAX GET requests.

    Attributes:
        None

    Note:
       - The 'listing_type' parameter in 'scrape_listing' can be one of: "applyRecord", "search", or "similarJobs".
       - For "applyRecord", it retrieves a 104 Job Bank member's list of applied jobs.
       - For "search", it retrieves results based on a given search criteria.
       - For "similarJobs", it retrieves results of jobs similar to a given job.

    Dependencies:
       - Requires the 'Req104' class for handling the configuration of AJAX GET requests.
    """

    @staticmethod
    def scrape_listing(listing_type, search_keyword_or_job_id=None):
        """
        Scrapes job listings based on the specified listing type and optional search keyword or job ID.

        Parameters:
            listing_type (str): Type of job listing to scrape ("applyRecord", "search", or "similarJobs").
            search_keyword_or_job_id (str, optional): Search keyword or specific job ID. Default is None.

        Returns:
            list: List of job IDs.

        Note:
            - The returned job IDs can be used to fetch detailed information about each job using 'scrape_one' method.

        """

        job_list = []
        job_id_list = []
        last_page = 1
        page_num = 1

        # Configure request based on listing type
        if listing_type == "search" or listing_type == "similarJobs" or listing_type == 'searchProfile':
            listing_req = Req104(listing_type, search_keyword_or_job_id)
        else:
            listing_req = Req104(listing_type)

        while page_num <= last_page:
            current_url = listing_req.url + str(page_num)
            response = requests.get(current_url, headers=listing_req.headers)
            response_data = response.json()

            if listing_type == "applyRecord":
                if page_num == 1:
                    # Find out total page number in the first loop
                    last_page = response_data['metadata']['pagination']['lastPage']
                    job_list = response_data['data']
                else:
                    job_list += response_data['data']
            elif listing_type == "search" or listing_type == "similarJobs":
                if page_num == 1:
                    # Find out total page number in the first loop
                    last_page = response_data['data']['totalPage']
                    job_list = response_data['data']['list']
                else:
                    job_list += response_data['data']['list']
            elif listing_type == listing_type == 'searchProfile':
                if page_num == 1:
                    # Find out total page number in the first loop
                    last_page = response_data['metadata']['pagination']['lastPage']
                    for item in response_data['data']:
                        job_id_list.append(item['key'])
                else:
                    for item in response_data['data']:
                        job_id_list.append(item['key'])

            page_num += 1

        for item in job_list:
            if listing_type == "applyRecord":
                job_id_list.append(item['analysisUrl'].split('/')[-1].split('?')[0])
            elif listing_type == "search":
                job_id_list.append(item['link']['job'].split('/')[-1].split('?')[0])
            elif listing_type == "similarJobs":
                job_id_list.append(item['link']['job'].split('/')[-1].split('?')[0])
            elif listing_type == "searchProfile":
                job_id_list.append(item[0]['key'])

        print(len(job_list))
        print(len(job_id_list))
        return job_id_list

    @staticmethod
    def scrape_one(job_id):
        """
        Scrapes details for a specific job ID.

        Parameters:
            job_id (str): The unique identifier of the job.

        Returns:
            dict: Details of the job.
        """
        req = Req104("job", search_keyword_or_job_id=job_id)
        response = requests.get(req.url, headers=req.headers)
        response_data = response.json()

        return response_data['data']

    @staticmethod
    def scrape_one_profile(profile_id):
        """
        Scrapes details for a specific profile ID.

        Parameters:
            profile_id (str): The unique identifier of the profile.

        Returns:
            dict: Details of the profile.
        """
        req = Req104("profile", search_keyword_or_job_id=profile_id)
        response = requests.get(req.url, headers=req.headers)
        response_data = response.json()
        response_data['data'].pop("sidebar")
        response_data['data'].pop("layout")
        response_data['data']["profile"].pop("themeChoose")
        return response_data['data']
