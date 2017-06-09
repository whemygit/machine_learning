#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import json

reload(sys)
sys.setdefaultencoding("utf-8")



# with open('D://jsontest','r') as fr:
#     lines=fr.readlines()
#     for line in lines:
#         json_text=eval(line)
#         print json_text
#         print json_text.keys()


root='D://town_tag'
for i in os.listdir('D://town_tag'):
    if i == 'urls':
        continue
    with open(root+'/'+i,'r') as fr, open('D://town_xpath_rules/'+i,'w') as fw:
        lines = fr.readlines()
        rule_dict = {}
        for line in lines:
            line=line.strip().split('\x01')
            rule_dict['area']=line[0]
            # print line[0]
            url_list=[]
            url_list.append(line[1])
            rule_dict['url']=url_list
            rule_dict['category_id']=i.split('-')[0]
            rule_dict['category_pid'] = i.split('-')[1]
            rule_dict['position']={'url': '......../@href'}
            rule_dict['type']='xpath'
            rule_dict['children_position']={'content':'content','news_date':'newsdata','text_f':'text_f','title':'title'}
            # print rule_dict
            # print type(json.dumps(rule_dict))
            fw.write(json.dumps(rule_dict, indent=4)+'\n')





# if __name__ == '__main__':
#     pass