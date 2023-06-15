import requests
from bs4 import BeautifulSoup

"""
Reminder
Steps of web scraping:
1. request (might need to bypass obstacles like login, confirmation button, javascript, etc)
2. make soups (if there are many pages)
3. analyze html tags, extract one sample
4. scrape & save
"""
# TODO:
#   learn csv module, use csv functions to write the file
#   try using 'a' mode when appending new lines to the file
#   why .strip('\t') doesn't work while .replace('\t', '') work?
#   further scrape each job post page


def main():
    # URL prefix, page number and suffix
    url_prefix = "https://www.104.com.tw/jobs/search/?ro=1&keyword=data%20engineer&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=15&asc=0&page="
    url_suffix = "&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    page_num = 1
    # Open txt file and write column titles
    with open("output/posts.txt", 'w', encoding="utf-8") as f:
        f.write("index\tjob_link\tjob_title\tjob_company\tjob_industry\tjob_update\tjob_location\tjob_exp\tjob_edu\t"
                "job_brief\tjob_applicants\tjob_tags_salary\tjob_tags_tse_otc\tjob_tags_fc\tjob_tags_emp\t"
                "job_tags_remote\tjob_tags_metro\n")
        # Get 50 pages
        for i in range(50):
            url = url_prefix + str(page_num) + url_suffix
            response = requests.get(url)
            html_text = response.text
            soup = BeautifulSoup(html_text, 'lxml')
            # Scrape
            scrape(soup, f)
            page_num += 1


def sample(soup):
    """
    This function extract one sample of data and print.
    :param soup: html content
    """
    # print prettify to check the html structures
    # print(soup.body.prettify())
    # Job info is in article tags with this class
    job = soup.find("article", class_="b-block--top-bord job-list-item b-clearfix js-job-item")
    # Get the items in different html tags and classes
    job_link = job.find("a", {"data-qa-id": "jobSeachResultTitle"})["href"]
    job_title = job.find("a", {"data-qa-id": "jobSeachResultTitle"}).text.strip()
    job_company = job["data-cust-name"].strip().strip("\r")
    job_industry = job["data-indcat-desc"].strip()
    job_update = job.find("span", class_="b-tit__date").text.strip()
    job_location = job.select('ul.b-list-inline.b-clearfix.job-list-intro.b-content > li')[0].text.strip()
    job_exp = job.select('ul.b-list-inline.b-clearfix.job-list-intro.b-content > li')[1].text.strip()
    job_edu = job.select('ul.b-list-inline.b-clearfix.job-list-intro.b-content > li')[2].text.strip()
    job_brief = job.find("p", class_="job-list-item__info b-clearfix b-content").text.strip().strip("\n").strip("\r").strip("\r\n")
    job_applicants = job.find("a", class_="b-link--gray gtm-list-apply").text
    # These items hide in these divs with this class
    job_tag_sec = job.find("div", class_="job-list-tag b-content")
    job_tags_salary = ""
    job_tags_tse_otc = ""
    job_tags_fc = ""
    job_tags_emp = ""
    job_tags_remote = ""
    job_tags_metro = ""
    for child in job_tag_sec.children:
        if child != ' ':
            if "薪" in child.text or "待遇面議" in child.text:
                job_tags_salary = child.text
            elif "上市上櫃" in child.text:
                job_tags_tse_otc = child.text
            elif "外商" in child.text:
                job_tags_fc = child.text
            elif "員工" in child.text:
                job_tags_emp = child.text
            elif "遠端工作" in child.text:
                job_tags_remote = child.text
            elif "距捷運" in child.text:
                job_tags_metro = child.text
            else:
                print("A new tag appears!")  # Just in case if job bank adds a new kind of job tag
    # Print the items scraped
    print(f'{job_link} {job_title} {job_company} {job_industry} {job_update} {job_location} {job_exp} {job_edu} {job_brief} {job_applicants} '
          f'{job_tags_salary} {job_tags_tse_otc} {job_tags_fc} {job_tags_emp} {job_tags_remote} {job_tags_metro}')


def scrape(soup, f):
    """
    This function iterates through all jobs in one page and scrape the desired items.
    :param soup: html content
    :param f: file pointer
    """
    # Job info is in article tags with this class
    jobs = soup.find_all("article", class_="b-block--top-bord job-list-item b-clearfix js-job-item")
    d = {}
    # Iterate through all jobs in a page
    for job in jobs:
        # Get the items in different html tags and classes
        d['job_id'] = job['data-job-no']
        d['link'] = job.find("a", {"data-qa-id": "jobSeachResultTitle"})["href"]
        d['title'] = job.find("a", {"data-qa-id": "jobSeachResultTitle"}).text.strip()
        d['company'] = job["data-cust-name"].strip().replace("\t","")
        d['industry'] = job["data-indcat-desc"].strip()
        # d['update'] = job.find("span", class_="b-tit__date").text.strip()
        d['location'] = job.select('ul.b-list-inline.b-clearfix.job-list-intro.b-content > li')[0].text.strip()
        # d['exp'] = job.select('ul.b-list-inline.b-clearfix.job-list-intro.b-content > li')[1].text.strip()
        # d['edu'] = job.select('ul.b-list-inline.b-clearfix.job-list-intro.b-content > li')[2].text.strip()
        if job.find("p", class_="job-list-item__info b-clearfix b-content"):
            d['brief'] = job.find("p", class_="job-list-item__info b-clearfix b-content").text.strip().replace("\t","").replace("\n","").replace("\r","").replace("\r\n","")
        else:
            d['brief'] = "NONE"
        # job_applicants = job.find("a", class_="b-link--gray gtm-list-apply").text
        # These items hide in these divs with this class
        job_tag_sec = job.find("div", class_="job-list-tag b-content")
        d['salary'] = ""
        d['tse_otc'] = ""
        d['fc'] = ""
        d['emp'] = ""
        d['remote'] = ""
        d['metro'] = ""
        for child in job_tag_sec.children:
            if child != " ":
                if "薪" in child.text or "待遇面議" in child.text:
                    d['salary'] = child.text
                elif "上市上櫃" in child.text:
                    d['tse_otc'] = child.text
                elif "外商" in child.text:
                    d['fc'] = child.text
                elif "員工" in child.text:
                    d['emp'] = child.text
                elif "遠端工作" in child.text:
                    d['remote'] = child.text
                elif "距捷運" in child.text:
                    d['metro'] = child.text
        # Write the items scraped to file
        f.write(f'{job_link}\t{job_title}\t{job_company}\t{job_industry}\t{job_update}\t{job_location}\t'
                f'{job_exp}\t{job_edu}\t{job_brief}\t{job_applicants}\t{job_tags_salary}\t{job_tags_tse_otc}\t'
                f'{job_tags_fc}\t{job_tags_emp}\t{job_tags_remote}\t{job_tags_metro}\n')
    # Print scraping status
    print(f'{index} job posts scraped on this page')


if __name__ == '__main__':
    main()
