# !python2.7
# coding=utf8

import os
import os.path
import MySQLdb

host = 'localhost'
user = 'root'
passwd = '111111'
port = 3306
charset = 'utf8'

try:
	conn = MySQLdb.connect(host='192.168.1.4', user='root', passwd='111111', port=3306, charset='utf8')
	conn.select_db('information_schema')
	
	cursor = conn.cursor()
	sql = r'select table_name,table_comment from tables where table_schema = "escpt"'
	cursor.execute(sql)
	results = cursor.fetchall()

	package = 'package/test/'
	if os.path.exists(package) is False:
		os.makedirs(package)
	for row in results:
		table_name = row[0]
		print table_name
		# 无法写入中文字符utf8
		#table_comment = unicode.encode(unicode(row[1].encode('utf8', 'ignore'), 'utf8'), 'utf8')
		filename = ''.join([n.capitalize() for n in table_name.split('_')])
		file = open(package+filename+'.java', 'w')
		file.write('package '+filename.lower()+';\n\n')
		file.write('/**\n * '+filename+' '+'\n * @author Anshen\n */\n')
		file.write('public class '+filename+' {\n')
		sql = r'select column_name,column_comment,data_type from columns where table_schema = "escpt" and table_name = "'+table_name+'"'
		cursor.execute(sql)
		column_results = cursor.fetchall()
		for co in column_results:
			field = co[0]
			# comment = co[1]
			data_type = co[2]
			field = ''.join([fd.capitalize() for fd in field.split('_')])
			field = field[0].lower()+field[1:len(field)]
			if 'int' in data_type:
				file.write('    private Integer '+field+'; // '+'\n')
			elif 'double' in data_type:
				file.write('    private Double '+field+'; // '+'\n')
			elif 'date' in data_type or 'time' in data_type:
				file.write('    private Date '+field+'; // '+'\n')
			else:
				file.write('    private String '+field+'; // '+'\n')
		file.write('}\n')
		file.close()
		print row

	cursor.close()
	conn.close()
except MySQLdb.Error, e:
	print "MySQL Error %d: %s" % (e.args[0], e.args[1])
