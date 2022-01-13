import requests
import json
import pymysql


# Temperature      = sensor['data']['datastreams'][4]['datapoints'][0]['value']
# Acidity          = sensor['data']['datastreams'][5]['datapoints'][0]['value']
# Conductivity     = sensor['data']['datastreams'][1]['datapoints'][0]['value']
# Generic_Sensor_0 = sensor['data']['datastreams'][7]['datapoints'][0]['value']
# Generic_Sensor_1 = sensor['data']['datastreams'][0]['datapoints'][0]['value']


def api_information():
    url = "url"
    headers = {"api-key": 'string', "Content-Type": 'application/json'}
    num = 2
    data = {'limit': num}
    receive = requests.get(url, headers=headers, params=data).text
    return receive


def request():
    sensor = json.loads(api_information())
    # sensor_data:传感器数值列表
    sensor_data = [1, 2, 3, 4, 5]
    # site:JSON下标
    site = [4, 5, 1, 7, 0]
    for i in range(0, 5):
        sensor_data[i] = sensor['data']['datastreams'][site[i]]['datapoints'][0]['value']
    return sensor_data


def mysql_insert(a, b, c, d, e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    # 打开数据库连接
    db = pymysql.connect(host='47.115.37.189', port=3306, user='root', password='123456', database='db_onenet',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 设置sql语句
    sql = 'insert into sensor(Temperature,Acidity,Conductivity,Generic_Sensor_0,Generic_Sensor_1) ' \
          'values(%s,%s,%s,%s,%s);'
    # 提交单条数据的操作
    cursor.execute(sql, [a, b, c, d, e])
    db.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    db.close()


def mysql_operation():
    # 数据库插入操作 —— 更新后端数据
    data = request()
    mysql_insert(data[0], data[1], data[2], data[3], data[4])


def test():
    data = request()
    print(data)


def main():
    api_information()
    request()
    mysql_operation()


# 主函数
if __name__ == '__main__':
    main()
