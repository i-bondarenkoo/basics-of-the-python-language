# Enum - это класс, который содержит константы и методы работы с ними
# Позволяет ограничить выбор пользователя, помогает пользователю понять возможные варианты
# позволяет легко добавлять и удалять значения

# 1) мы не можем ограничить пользователя (при вводе)
# 2) документация не всегда актуальна
# 3) изменения в нескольких местах

from enum import Enum, auto


class TrafficLight(Enum):
    # константы пишем капсом
    # auto используется, если не нужно значение, заглушка
    # например RED = 1
    RED = 'stop'
    GREEN = 'go'
    YELLOW = 'wait'


#сигналы светофора
def allowed_action(traffic_light: TrafficLight) -> str:
    
    return traffic_light.value

if __name__ == '__main__':
    print(allowed_action(TrafficLight.RED))
    print(allowed_action(TrafficLight.GREEN))
    print(allowed_action(TrafficLight.YELLOW))

