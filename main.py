""" file for autoconfiguration monitoring system """

import yaml

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
        'static_configs': {'targets': targets}
    })

    return config

def save_to_yaml(config, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

def main():
    prometheus_config = get_prometheus_config()
    file_path = input("введите путь до файла prometheus.yml")
    save_to_yaml(prometheus_config, file_path)
    print(f"Файл конфигурации сохранен по пути: {file_path}")

if __name__ == "__main__":
    main()

