# -*- coding: cp949 -*-
import urllib2
def get_html(url, maxbuf = 10485760):
 res = urllib2.urlopen(url)
 html = res.read(maxbuf)
 res.close()
 # HTML을 파일로 저장
 with open('melon_weekly.html', 'w') as f:
  f.write(html)
 # 파일로 저장된 HTML을 로딩
 with open('melon_weekly.html', 'r') as f:
  html = f.read()
 return html

if __name__ == '__main__':
 charturl = {'daily':
'http://www.melon.com/chart/day/index.htm', \
 'weekly':
'http://www.melon.com/static/cds/chart/web/chartdaily_list.html', \
 'monthly':
'http://www.melon.com/static/cds/chart/web/chartmonthly_list.html'}
 html = get_html(charturl['daily'])
