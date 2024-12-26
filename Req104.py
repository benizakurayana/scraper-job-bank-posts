class Req104:
    """
    This class represents a request configuration for sending AJAX GET requests to 104 Job Bank API.
    Each type of request requires different referer headers. The supported request types are:
        - applyRecord:
          Retrieves a 104 Job Bank member's list of applied jobs. Requires a cookie with member login information.
          Note: The cookie header is currently hard-coded and should be dynamically acquired in future updates.

        - search:
          Retrieves search results based on a given search criteria. The search criteria is currently hard-coded
          in the request URL and should be moved to the params attribute in future updates.

        - similarJobs:
          Retrieves results of jobs similar to a given job.

        - job:
          Retrieves details of a given job. The unique job ID obtained from other requests guides this request.

    Attributes:
        headers (dict): HTTP headers for the request.
        url (str): The URL endpoint for the request.

    Methods:
        __init__(req_type, search_keyword_or_job_id=None):
            Initializes the Req104 object based on the request type and optional search keyword or job ID.

    Note: Ensure to review and update the hard-coded values and configurations as needed.
    """

    def __init__(self, req_type, search_keyword_or_job_id=None):
        # HTTP headers for the request
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
            "Cookie": "luauid=1886703560; ACUD=19542e24-9f4a-49c1-9853-d7c3c1e7be57; __auc=10eb01d0185b4f475adb02aeba5; _hjSessionUser_3218023=eyJpZCI6ImYzOTg3MTNkLTdkY2MtNWMxZS1iYTI0LTUxNWNkZThjZDU1ZCIsImNyZWF0ZWQiOjE2NzM3NzcxOTUxNDMsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6NM1YTENCG=GS1.1.1673856698.1.1.1673856712.0.0.0; _hjSessionUser_601941=eyJpZCI6ImE1ZTJlMmYxLWZjNDUtNTFiZS05NjI5LTZjODQ1OWY2ZjhiZiIsImNyZWF0ZWQiOjE2NzM3NzcyMzQxMzUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_642678=eyJpZCI6ImM1M2Y3ZjY4LTA1Y2ItNTFlNS05MGI5LTRlNjlhNjcyOGRjNyIsImNyZWF0ZWQiOjE2NzM4NTcxNTY1OTAsImV4aXN0aW5nIjp0cnVlfQ==; _ga_WYQPBGBV8Z=GS1.1.1676332260.54.1.1676332269.51.0.0; _ga_9M2435MMPG=GS1.1.1678795143.1.1.1678795155.0.0.0; _ga_LQE3H5BS2W=GS1.1.1678846516.1.1.1678846576.0.0.0; dtCookie=v_4_srv_3_sn_E103AD3A1453A9CE3EB85C6C67F48D0A_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0_app-3Ae09751cb0ddc5f9d_0; TS012d3931=01180e452d2fa61998c888950c5f437f3476efbefcf74ab869985fe2af141c8292a3dce1952af06477321c05b6ea5124588dd4651e9224e97371b5286e853d708d44bdab3c; _ga=GA1.4.1007433062.1673777161; isAvatarTooltipShow=1; cmy104-ResumeExampleLight=true; TS01952b90=01180e452d6f0b3df9d57aa94a3dfe892441b49dc0857c6444178420c9a1ba53c7ebf5edad71a3e2678daffc02c483d88168b6ebf290aab208ecb453d79c09166ca17a346380d4d3b00065547f0d61d7c217a441aa8456b2a97fdd53d2ef05375774e979ac59ff631b21c11c7feb02bdf8a08a2d1e082895f65b1b6b76d0257c34b1a9db2f73dfa3e13a55b04cc641f5202c5bac1cea105cc80c167f76baf6cf34daf311ca; _ga_PKQ3ZT2828=GS1.1.1702556488.2.1.1702556501.47.0.0; EPK=8f27234a-8444-4694-ae59-005da00a3616; cmy104-overviewSettingShowTips=yes; _hjSessionUser_1342751=eyJpZCI6IjE3OTdhODhjLTA5ZTktNWFhOS04OTg3LTFkYTZlMzE5ZWY1MiIsImNyZWF0ZWQiOjE3MDQxOTEyOTUxNzYsImV4aXN0aW5nIjpmYWxzZX0=; _ga_NJF1DCGRNK=GS1.1.1704191295.1.1.1704191315.0.0.0; _hjHasCachedUserAttributes=true; resumeAnalyzeRemindPopup=true; resumeAnalyze=true; cmy104-progressBarIconFinishIsClicked=yes; _ga_W9X1GB1SVR=deleted; _hjDonePolls=829535%2C787456%2C880533; TS01d2aaa1=01180e452da39521900bd194b8cee2594c1b48c5114217f1dc562414acabe40eed045dc328bdfceea81dd449503d7eb22015e8ef24; _fbp=fb.2.1706011271596.736927674; _hp2_id.3192618648=%7B%22userId%22%3A%225234725469666068%22%2C%22pageviewId%22%3A%221463766221202277%22%2C%22sessionId%22%3A%224477571261626097%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_TTXLT7SQ8E=GS1.1.1706247485.16.0.1706247488.57.0.0; _hjMinimizedPolls=787456%2C856903%2C880533%2C869445%2C981965; _uetvid=764144d0b40711ee8c7fb9bfc71c67d9; _gcl_au=1.1.712348052.1701753606.1165794439.1706782566.1706782565; _ga_D4915X27HH=GS1.1.1706846150.14.0.1706846271.0.0.0; _ga_CBC4Z4CF01=GS1.1.1706846150.13.0.1706846271.0.0.0; AC=1707048155; TS01f8a99d=01180e452da253be01b8b9e853365216f7feb8ccd052d835ce04438fdc1702ff5e5e91ffb33b0c294494a8efaf321dabb78ef7399c90bf26961bc2900ffc4a7dc48ecf507872157c5cb909477cbc7a6abda7a272adcca3f7976ea628df69971bc8147a393a37383d9cf0589c1605c4470c570c8f20; JBCLOGIN=IJ7Anw1xrA21U5enruElJV7Vw1aVMSeDHprGdd5XqO0BQ; my_profile_team=C; _hjSessionUser_1160171=eyJpZCI6IjJjMzFhNTkyLTY0MjYtNTE2Mi04ZDI2LTdiY2UxYThmNTZhMyIsImNyZWF0ZWQiOjE2Nzg3OTUxNDM1OTMsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2628092=eyJpZCI6IjFlNmI1MzNhLTc0ODktNTgwYS05MjUwLTE2YzlmMjU1ODNjZiIsImNyZWF0ZWQiOjE3MDcxMDMzNDYwNzEsImV4aXN0aW5nIjpmYWxzZX0=; _ga_56CY78S3P8=GS1.1.1707103345.1.0.1707103354.51.0.0; _ga_8DLGGRNRT2=GS1.3.1707103295.1.1.1707103704.49.0.0; _ga_PHKF9K6Q1Q=GS1.1.1707103295.1.1.1707105359.0.0.0; _ga=GA1.1.1007433062.1673777161; _clck=1sf0hdo%7C2%7Cfj4%7C0%7C1228; c_job_view_job_info_nabi=818bg%2C2007001007; lup=1886703560.4702989186930.5035849152215.1.4640712161167; lunp=5035849152215; _clsk=5s5mzf%7C1707464603842%7C1%7C1%7Cs.clarity.ms%2Fcollect; _hjSession_3218023=eyJpZCI6ImJiNTc5MTcxLTNiN2EtNDMyMi1hZDEwLWRjYTgzMGNkYjYzMSIsImMiOjE3MDc0NjQ2MDc0MDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; bubble=77_448_120_8_0_0_0_0; _ga_W9X1GB1SVR=GS1.1.1707464607.240.1.1707464612.55.0.0; _ga_Q72RY288G8=GS1.4.1707464607.144.1.1707464612.0.0.0; _ga_FJWMQR9J2K=GS1.1.1707464607.246.1.1707464612.55.0.0",
            "Referer": ""
        }

        # URL endpoint for the request
        self.url = ""

        # Currently, params are hardcoded in url
        # self.params = ""

        if req_type == "applyRecord":
            self.url = "https://pda.104.com.tw/applyRecord/ajax/list?status=all&page="
            self.headers["Referer"] = "https://pda.104.com.tw/applyRecord"
        elif req_type == "search":
            self.url = f'https://www.104.com.tw/jobs/search/list?ro=0&jobcat=2007001000&kwop=7&keyword={search_keyword_or_job_id}&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000%2C6001002000&edu=4&order=12&asc=0&sctp=M&scmin=32000&scmax=45000&scstrict=1&scneg=1&excludeIndustryCat=1001001002%2C1001001001&s9=1&wktm=1&mode=s&jobsource=index_s&searchTempExclude=2&langFlag=0&langStatus=0&recommendJob=0&hotJob=0&page='
            self.headers["Referer"] = "https://www.104.com.tw/jobs/search/"
        elif req_type == "similarJobs":
            self.url = f'https://www.104.com.tw/job/ajax/similarJobs/{search_keyword_or_job_id}?mode=s&page='
            self.headers["Referer"] = f'https://www.104.com.tw/job/similar/{search_keyword_or_job_id}?jobsource=analysis_jobsame_b&recommendJob=0&hotJob=0'
        elif req_type == "job":
            self.url = f'https://www.104.com.tw/job/ajax/content/{search_keyword_or_job_id}'
            self.headers["Referer"] = f'https://www.104.com.tw/job/{search_keyword_or_job_id}'
        elif req_type == "searchProfile":
            self.url = f'https://api.profile.104.com.tw/profiles?kw={search_keyword_or_job_id}&pageSize=100&sort=recommend&page='
            self.headers["Referer"] = 'https://profile.104.com.tw/'
        elif req_type == "profile":
            self.url = f'https://api.profile.104.com.tw/profiles/{search_keyword_or_job_id}'
            self.headers["Referer"] = 'https://profile.104.com.tw/'
        else:
            print("Incorrect listing_type")
