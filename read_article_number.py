from config import *

def re_ArtNo(url):

    pattern = re.compile(r'\w{6}-\d{3}')
    return pattern.findall(url)[0]

if __name__ == '__main__':
    start=time()
    url = "https://www.nike.com/kr/ko_kr/t/men/fw/basketball/CI2667-001/kyoi71/pg-3-nasa-ep"
    url="https://www.nike.com/kr/launch/t/men/fw/nike-sportswear/BQ7541-001/uyfu11/air-force-1-07-skeleton-qs"
    print(re_ArtNo(url))
