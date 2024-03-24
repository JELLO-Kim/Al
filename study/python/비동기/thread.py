import threading
import itertools
import time
import sys


# asyncio 연습
import asyncio

import itertools
import sys
@asyncio.coroutine
def a_spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    print("진입")
    for char in itertools.cycle('LOVE'):
        status = char + msg
        print(status)
        # write(status)
        # flush()
        # write('\x08' + len(status))
        try:
            time_1 = time.time()
            # print(f"[11] {time.time()}")
            # yield from asyncio.sleep(0.1)
            time_2 = time.time()
            print(f"[22-11] {time_2 - time_1}")

        except asyncio.CancelledError:
            break
        # write(' '*len(status) + '\x08' + len(status))

@asyncio.coroutine
def a_slow_function():
    time_3 = time.time()
    print(f"[33] {time_3}")
    yield from asyncio.sleep(2)
    time_4 = time.time()
    print(f"[44] {time_4}")
    print(f"[44-33] {time_4 - time_3}")
    return 42

@asyncio.coroutine
def a_supervisor():
    spinner = asyncio.ensure_future(a_spin('히히'))
    print('spinner object:', spinner)
    result = yield from a_slow_function()
    spinner.cancel()
    return result

def a_main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(a_supervisor())
    loop.close()
    print('Answer :', result)



class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('LOVE'):  # 사실상 무한루프이다
        status = char + msg
        write(status)
        flush()
        time.sleep(0.3)  # 두번째 thread sleep 그동안 메인 thread가 동작한다.
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # 입출력을 위해 장시간 기다리는것 처럼 보이게 만들기
    # 메인 thread가 sleep 그동안 두번째 thread가 동작한다
    time.sleep(3)

    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('히히', signal))
    print('spinner object:', spinner)
    a = time.time()
    spinner.start()
    t = time.time()
    print(f"[1] 2nd thread run {t - a}")
    result = slow_function()
    c = time.time()
    print(f"[2] main thread sleep after {c - t}")
    signal.go = False
    spinner.join()
    return result

def main():
    result = supervisor()
    print('Answer:', result)

if __name__ == '__main__':
    # main()
    print("----------------------------------------------------------")
    a_main()