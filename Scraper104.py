import requests
from Req104 import Req104


class Scraper104:

    @staticmethod
    def scrape_listing(listing_type, search_keyword_or_job_id=None):
        job_list = []
        job_id_list = []
        last_page = 1
        page_num = 1
        if listing_type == "search" or listing_type == "similarJobs":
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

            page_num += 1

        for item in job_list:
            if listing_type == "applyRecord":
                job_id_list.append(item['analysisUrl'].split('/')[-1].split('?')[0])
            elif listing_type == "search":
                job_id_list.append(item['link']['job'].split('/')[-1].split('?')[0])
            elif listing_type == "similarJobs":
                job_id_list.append(item['link']['job'].split('/')[-1].split('?')[0])

        # print(len(job_list))
        # print(len(job_id_list))
        return job_id_list

    @staticmethod
    def scrape_one(job_id):
        req = Req104("job", search_keyword_or_job_id=job_id)
        response = requests.get(req.url, headers=req.headers)
        response_data = response.json()

        return response_data['data']
