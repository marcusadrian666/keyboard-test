import keyboard
import threading
import time

class KeyboardChecker:
    def __init__(self):
        self.running = True
        self.key_press_times = {}  # 记录按键按下的时间戳
        self.key_release_times = {}  # 记录按键释放的时间戳
        self.key_press_count = {}  # 记录按键按下次数

    def start(self):
        print("开始检测键盘按键，请按下或释放任意键。")
        self.listener_thread = threading.Thread(target=self._keyboard_listener)
        self.listener_thread.start()

    def stop(self):
        print("检测结束。")
        self.running = False
        self.listener_thread.join()

    def _keyboard_listener(self):
        while self.running:
            key_event = keyboard.read_event(suppress=True)
            key_name = key_event.name

            if key_event.event_type == keyboard.KEY_DOWN:
                print(f"按键 {key_name} 被按下。")
                self.key_press_times[key_name] = time.time()

                # 统计按键按下次数
                self.key_press_count[key_name] = self.key_press_count.get(key_name, 0) + 1

            elif key_event.event_type == keyboard.KEY_UP:
                print(f"按键 {key_name} 被释放.")
                self.key_release_times[key_name] = time.time()

    def display_statistics(self):
        print("\n按键统计信息：")
        for key, count in self.key_press_count.items():
            press_time = self.key_press_times.get(key, "N/A")
            release_time = self.key_release_times.get(key, "N/A")
            print(f"按键 {key}: 按下次数 {count}, 最后按下时间 {press_time}, 最后释放时间 {release_time}")

if __name__ == "__main__":
    checker = KeyboardChecker()

    try:
        checker.start()
        # 在这里可以执行其他操作

        time.sleep(10)  # 示例：让程序运行一段时间，模拟其他操作
    except KeyboardInterrupt:
        pass
    finally:
        checker.stop()
        checker.display_statistics()
