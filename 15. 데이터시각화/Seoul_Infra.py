import csv
from BeautifulSoup import BeautifulSoup


#������ ���� ���������ü� ������ �б�
reader = csv.reader(open('senior_lsf.csv', 'r'), delimiter=",")
#SVG �� �б�
svg = open('seoul_map.svg', 'r').read()

senior_count={}
counts_only=[]
min_value=100;max_value=0;past_header=False
for row in reader:
    if not past_header:
        past_header=True
        continue

    try:
        unique = row[0]
        count=float(row[1].strip())
        senior_count[unique] = count
        counts_only.append(count)
    except:
        pass

#��ƼǮ������ �ε��ϱ�
soup = BeautifulSoup(svg)
#���� �ĺ��� path������ ã��
paths = soup.findAll('path')
#�򵵽ð�ȭ�� ������ ���� ����
colors = ["#F1EEF6", "#D4B9DA","#C994C7","#DF65B0","#DD1C77","#980043"]
#�򵵿� ��Ÿ�� ��Ÿ�� ����
path_style='font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

#���ο����ü��� ���� ���� ���� �����ο�
for p in paths:
    if p['id']:
        try:
            count=senior_count[p['id']]
        except:
            continue
        #������ �ο��� ���� ����
        if count>250:
            color_class=5
        elif count>200:
            color_class=4
        elif count>150:
            color_class=3
        elif count>100:
            color_class=2
        elif count>50:
            color_class=1
        else:
            color_class=0

        color=colors[color_class]
        p['style'] = path_style + color

print soup.prettify()
