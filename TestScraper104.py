from PersistenceExcel import PersistenceExcel
from Scraper104 import Scraper104


class TestScraper104:
    """
    This class contains test methods for Scraper104 and PersistenceExcel functionality and demonstrates saving scraped
    job details to Excel.

    Dependencies:
        - Requires the 'Scraper104' class for scraping job details.
        - Requires the 'PersistenceExcel' class for saving job details to an Excel file.
    """

    @staticmethod
    def test_similar_job_save_to_excel():
        # Scrape
        job_id_list = Scraper104.scrape_listing("similarJobs", "7zz8h")
        job_list = []
        for item in job_id_list:
            job = Scraper104.scrape_one(item)
            job_list.append(job)

        # Save results to Excel
        PersistenceExcel.save(job_list, "similar_job_list")

    @staticmethod
    def test_applied_job_save_to_excel():
        # Scrape
        job_id_list = Scraper104.scrape_listing("applyRecord")
        job_list = []
        for item in job_id_list:
            job = Scraper104.scrape_one(item)
            job_list.append(job)

        # Save results to Excel
        PersistenceExcel.save(job_list, "applied_job_list")

    @staticmethod
    def test_search_job_save_to_excel():
        # Scrape
        job_id_list = Scraper104.scrape_listing("search", "java")
        job_list = []
        for item in job_id_list:
            job = Scraper104.scrape_one(item)
            job_list.append(job)

        # Save results to Excel
        PersistenceExcel.save(job_list, "search_job_list")

    @staticmethod
    def test_search_profile_save_to_excel():
        # Scrape
        profile_id_list = Scraper104.scrape_listing("searchProfile", "遊戲企劃")
        profile_list = []
        for profile_id in profile_id_list:
            profile = Scraper104.scrape_one_profile(profile_id)
            profile_list.append(profile)

        # Save results to Excel
        PersistenceExcel.save(profile_list, "search_profile_list")


if __name__ == "__main__":
    # TestScraper104.test_similar_job_save_to_excel()
    # TestScraper104.test_applied_job_save_to_excel()
    # TestScraper104.test_search_job_save_to_excel()
    TestScraper104.test_search_profile_save_to_excel()
