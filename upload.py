import schedule
import time
import requests
import mysql.connector


def upload_to_thingsboard():
    # 连接到数据库
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1111',
        database='thingsborad'
    )
    cursor = connection.cursor()
    # 查询ID最大的行
    cursor.execute("SELECT ripe, immaturity FROM tomato ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        ripe, immaturity = result
        data = {"ripe": ripe, "immaturity": immaturity}
        # 发送数据到 ThingsBoard
        url = "http://localhost:25567/api/v1/0hLrUQ5EfNCbef64csQb/telemetry"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        print("Data uploaded:", response.text)


def main():
    # 设置每10秒执行一次上传函数
    schedule.every(10).seconds.do(upload_to_thingsboard)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
    #从本地MySQL数据库中定期读取最新的番茄成熟度数据。
    #将读取到的数据以JSON格式上传到本地运行的ThingsBoard物联网平台。
    #实现数据的自动化收集和上传，确保ThingsBoard平台能够实时接收到最新的番茄成熟度数据，以便进行监控和分析。