# asyncio 연습
import asyncio

import itertools
import sys
@asyncio.coroutine
def spin(msg):
    print('spin ~~~~~~~~~~')
    write, flush = sys.stdin.write, sys.stdin.flush
    for char in itertools.cycle('LOVE'):
        print('spin ~~~~~~~~~~', char)
        status = char + msg
        write(status)
        flush()
        write('\x08' + len(status))
        try:
            yield from asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
        write(' '*len(status) + '\x08' + len(status))

@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 42

@asyncio.coroutine
def supervisor():
    spinner = asyncio.ensure_future(spin('히히'))
    print('spinner object:', spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer :', result)

if __name__ == "__main__":
    main()
