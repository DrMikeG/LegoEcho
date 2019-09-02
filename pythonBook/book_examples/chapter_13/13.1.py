import asyncio

@asyncio.coroutine
def make_tea(variety):
    print('Now making %s tea.' % variety)
    return '%s tea' % variety

if __name__== "__main__":
    loop = asyncio.get_event_loop()

    meta_task = asyncio.gather(
        make_tea('chamomile'),
        make_tea('green'),
        make_tea('herbal')
    )

    meta_task.done()

    loop.run_until_complete(meta_task)
    print(meta_task.done())
