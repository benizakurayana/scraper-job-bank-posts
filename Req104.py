from ReqHeaders104 import ReqHeaders104


class Req104:
    def __init__(self, req_type, search_keyword_or_job_id=None):
        self.headers = ReqHeaders104(req_type)
        self.url = ""
        self.params = ""

        if req_type == "applyRecord":
            self.url = "https://pda.104.com.tw/applyRecord/ajax/list?status=all&page="
        elif req_type == "search":
            self.url = f'https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword={search_keyword_or_job_id}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&mode=s&jobsource=n_my104_search_h&langFlag=0&langStatus=0&recommendJob=0&hotJob=0&page='
        elif req_type == "similarJobs":
            self.url = f'https://www.104.com.tw/job/ajax/similarJobs/{search_keyword_or_job_id}?mode=s&page='
            self.headers.referer = f'https://www.104.com.tw/job/similar/{search_keyword_or_job_id}?jobsource=analysis_jobsame_b&recommendJob=0&hotJob=0'
        elif req_type == "job":
            self.url = "https://www.104.com.tw/job/ajax/content/"
        else:
            print("Incorrect listing_type")


# if __name__ == '__main__':
#     listingReq = ListingReq104("search")
