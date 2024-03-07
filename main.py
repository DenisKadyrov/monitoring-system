""" file for autoconfiguration monitoring system """

import yaml
import os

def get_prometheus_config():
    config = {}
    # Введите общие параметры
    config['global'] = {
        'scrape_interval': input("Введите интервал сбора метрик (например, 15s): "),
        'evaluation_interval': input("Введите интервал оценки правил (например, 15s): ")
    }

    # Введите конфигурацию целей
    config['scrape_configs'] = []
    targets = []
    with open("remote_hosts.txt") as hosts:
        for host in hosts.readlines():
            targets.append(host.replace("\n", "") + ":9100")
            
    config['scrape_configs'].append({
        'job_name': "node",
        'static_configs': [{'targets': targets}]
    })

    return config

def save_to_yaml(config, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(config, file)

def main():
    # prometheus_config = get_prometheus_config()
    # file_path = input("введите путь до файла prometheus.yml")
    # save_to_yaml(prometheus_config, file_path)
    # print(f"Файл конфигурации сохранен по пути: {file_path}")
    services = {"alertmanager": 0, "grafana": 0}

    for service in services.keys():
        services[service] = int(input(f"Установить {service}? 0 - нет, 1 - да: "))

    with open("docker-compose.yaml") as file:
        docker_compose = yaml.safe_load(file)

    if services['alertmanager'] == 1:
        docker_compose["services"]["alertmanager"] = {
            'image': 'prom/alertmanager',
            'container_name': 'alertmanager',
            'volumes': ['./alertmanager:/alertmanager/data', 
            './alertmanager/config:/etc/alertmanager/'],
            'command': ['--config.file=/etc/alertmanager/alertmanager.yaml'],
            'ports': ['9093:9093']
        }

        docker_compose["services"]['flask-app'] = {
            'build': '.',
            'ports': ['5000:5000'],
            'restart': 'always'
        }

        token = f'https://telepush.dev/api/inlets/alertmanager/{input("Введите токен бота: ")}'
        with open("alertmanager/config/alertmanager.yaml") as file:
            alert_file = yaml.safe_load(file)
        print(alert_file['receivers'][0]['webhook_configs'][0])

    if services["grafana"] == 1:
        docker_compose['services']['grafana'] = {
            'image': 'grafana/grafana-enterprise:latest',
            'container_name': 'grafana',
            'ports': ['3000:3000']
        }
    save_to_yaml(docker_compose, "docker-compose.yaml.demo")    
    save_to_yaml(alert_file, 'alertmanager/config/alertmanager.yaml.demo')

if __name__ == "__main__":
    main()
