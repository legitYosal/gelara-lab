import sys
import os
from typing import Dict
from time import sleep
import psutil
import mysql.connector
from mysql.connector import Error
import prometheus_client as prometheus

class Collector:
    def __init__(self, ):
        self.psutil_cpu_percent = prometheus.Gauge(
            'psutil_cpu_percent', 'Cpu utilization percent'
        )
        self.psutil_virtual_memory_percent = prometheus.Gauge(
            'psutil_virtual_memory_percent', 'Memory utilization'
        )
        self.wsrep_cluster_size = prometheus.Gauge(
            'wsrep_cluster_size', 'Wsrep cluster size'
        )
        self.wsrep_cluster_status = prometheus.Gauge(
            'wsrep_cluster_status', 'Wsrep cluster status',
            labelnames=['node_status']
        )

    def collect_wsrep_stats(self) -> Dict[str, str]:
        wsrep_stats = {}
        try:
            conn = mysql.connector.connect(
                user=os.environ.get('MARIADB_USER'),
                password=os.environ.get('MARIADB_PASSWORD'),
                host=os.environ.get('MARIADB_HOST'),
                port=int(os.environ.get('MARIADB_PORT')),
            )
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute('show status like "wsrep%"')
                wsrep_stats_raw = cursor.fetchall()
                wsrep_stats = {i[0]: i[1] for i in wsrep_stats_raw}
                self.wsrep_cluster_size.set(wsrep_stats['wsrep_cluster_size'])
                self.wsrep_cluster_status.labels(
                    node_status=wsrep_stats['wsrep_cluster_status']
                ).set(1)
        except Error as e:
            print("Error while connecting ", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        return wsrep_stats

    def collect_node_stats(self, ) -> None:
        self.psutil_cpu_percent.set(psutil.cpu_percent())
        self.psutil_virtual_memory_percent.set(psutil.virtual_memory().percent)

if __name__ == '__main__':
    dbexporter_port = int(os.environ.get('DBEXPORTER_PORT', '8185'))
    prometheus.start_http_server(dbexporter_port)
    print('Started server at :' + str(dbexporter_port))
    collector = Collector()
    while True:
        collector.collect_node_stats()
        collector.collect_wsrep_stats()
        sleep(5)
