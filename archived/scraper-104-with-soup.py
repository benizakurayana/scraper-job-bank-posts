import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    # URL prefix, page number and suffix
    url_prefix = "https://www.104.com.tw/jobs/search/?ro=1&kwop=7&keyword=RPA&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page="
    url_suffix = "&mode=s&jobsource=n_my104_search&langFlag=0&langStatus=0&recommendJob=0&hotJob=0"
    page_num = 1

    job_ids = []

    # Get 50 pages
    for i in range(50):
        url = url_prefix + str(page_num) + url_suffix
        response = requests.get(url)
        html_text = response.text
        soup = BeautifulSoup(html_text, 'lxml')
        # Scrape
        scrape(soup, job_ids)
        page_num += 1
    print(job_ids)
    print(len(job_ids))

    # [Get job details by soup]
    # Iterate through all job IDs
    job_details_list = []
    for job_id in job_ids:
        job_details = get_job_details_by_soup(job_id)
        if job_details:
            job_details_list.append(job_details)

    # Convert the list of dictionaries to a DataFrame
    job_details_df = pd.DataFrame(job_details_list)

    # Save the DataFrame to an Excel file
    job_details_df.to_excel('job_details.xlsx', index=False)


def scrape(soup, job_ids):
    """
    This function iterates through all jobs on one page and scrapes the link to the job page.
    """
    # Job info is in article tags with this class
    jobs = soup.find_all("article", class_="b-block--top-bord job-list-item b-clearfix js-job-item")

    # Iterate through all jobs on a page
    for job in jobs:
        link = job.find("a", {"data-qa-id": "jobSeachResultTitle"})["href"].split('//')[1]

        # Extract the job ID from the URL
        job_id = link.split('/')[-1].split('?')[0]
        job_ids.append(job_id)


def get_job_details_by_soup(job_id):
    # Fetch job details
    url_prefix = 'https://www.104.com.tw/job/'
    url_suffix = job_id
    url = url_prefix + url_suffix
    response = requests.get(url)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')

    # Extract relevant information from soup
    job_url = url
    id = job_id

    # ol.breadcrumb-list
    breadcrumb_items = soup.select('.breadcrumb-list__item')
    company = breadcrumb_items[1].find('a').text.strip()
    company_link = breadcrumb_items[1].find('a')['href']
    title = breadcrumb_items[2].find('span')['title']
    date_updated = soup.select_one('.job-header__title span[title]')['title']

    # div.job-description
    description = soup.select_one('p.job-description__content').text.strip()
    categories = [category.text.strip() for category in soup.select('.category-item u')]
    salary = soup.select_one('.list-row__head > h3:-soup-contains("工作待遇")').find_next('p',
                                                                                    class_='text-primary').text.strip()
    type = soup.select_one('.list-row__head > h3:-soup-contains("工作性質")').find_parent().find_next_sibling().get_text().strip()
    location = soup.select_one('.job-address').text.strip()
    location_map_url_element = soup.select_one('.job-address a')
    location_map_url = location_map_url_element['href'] if location_map_url_element else None
    supervisor = soup.select_one('.list-row__head > h3:-soup-contains("管理責任")').find_parent().find_next_sibling().get_text().strip()
    expatriate = soup.select_one('.list-row__head > h3:-soup-contains("出差外派")').find_parent().find_next_sibling().get_text().strip()
    working_hours = soup.select_one('.list-row__head > h3:-soup-contains("上班時段")').find_parent().find_next_sibling().get_text().strip()
    day_off = soup.select_one('.list-row__head > h3:-soup-contains("休假制度")').find_parent().find_next_sibling().get_text().strip()
    on_board = soup.select_one('.list-row__head > h3:-soup-contains("可上班日")').find_parent().find_next_sibling().get_text().strip()
    head_count = soup.select_one('.list-row__head > h3:-soup-contains("需求人數")').find_parent().find_next_sibling().get_text().strip()

    # div.job-requirement
    experience = soup.select_one('.list-row__head > h3:-soup-contains("工作經歷")').find_parent().find_next_sibling().get_text().strip()
    degree = soup.select_one('.list-row__head > h3:-soup-contains("學歷要求")').find_parent().find_next_sibling().get_text().strip()
    major = soup.select_one('.list-row__head > h3:-soup-contains("科系要求")').find_parent().find_next_sibling().get_text().strip()
    language = soup.select_one('.list-row__head > h3:-soup-contains("語文條件")').find_parent().find_next_sibling().get_text().strip()
    tools = soup.select_one('.list-row__head > h3:-soup-contains("擅長工具")').find_parent().find_next_sibling().get_text().strip()
    skills = soup.select_one('.list-row__head > h3:-soup-contains("工作技能")').find_parent().find_next_sibling().get_text().strip()
    others = soup.select_one('.list-row__head > h3:-soup-contains("其他條件")').find_parent().find_next_sibling().get_text().strip()

    # div.job-contact-table
    contact_element = soup.select_one('.job-contact-table__head h3:-soup-contains("聯絡人")')
    contact = contact_element.find_parent().find_next_sibling().get_text().strip() if contact_element else None

    email_element = soup.select_one('.job-contact-table__head h3:-soup-contains("E-mail")')
    email = email_element.find_parent().find_next_sibling().get_text().strip() if email_element else None

    phone_element = soup.select_one('.job-contact-table__head h3:-soup-contains("電洽")')
    phone = phone_element.find_parent().find_next_sibling().get_text().strip() if phone_element else None

    contact_remarks_element = soup.select_one('.job-contact-table__head h3:-soup-contains("其他")')
    contact_remarks = contact_remarks_element.find_parent().find_next_sibling().get_text().strip() if contact_remarks_element else None

    extracted_data = {
        'job_url': job_url,
        'id': id,
        'title': title,
        'company': company,
        'company_link': company_link,
        'date_updated': date_updated,
        'description': description,
        'categories': categories,
        'salary': salary,
        'type': type,
        'location': location,
        'locationMapUrl': location_map_url,
        'supervisor': supervisor,
        'expatriate': expatriate,
        'workingHours': working_hours,
        'dayOff': day_off,
        'onBoard': on_board,
        'headCount': head_count,
        'experience': experience,
        'degree': degree,
        'major': major,
        'language': language,
        'tools': tools,
        'skills': skills,
        'others': others,
        'contact': contact,
        'email': email,
        'phone': phone,
        'contactRemarks': contact_remarks
    }

    return extracted_data


def get_job_details_by_requests(job_id):
    url = f'https://www.104.com.tw/job/ajax/content/{job_id}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
        'Referer': f'https://www.104.com.tw/job/{job_id}'
    }

    r = requests.get(url, headers=headers)

    data = r.json()
    return data['data']


if __name__ == '__main__':
    main()
