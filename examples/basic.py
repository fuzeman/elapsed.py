import elapsed
import logging
import random
import time


class Example(object):
    @elapsed.clock
    def run(self):
        for x in xrange(25):
            self.one()

        for x in xrange(25):
            self.two()

    @elapsed.clock
    def one(self):
        time.sleep(float(random.randint(0, 250)) / 1000)

        for x in xrange(3):
            self.three()

    @classmethod
    @elapsed.clock
    def two(cls):
        time.sleep(float(random.randint(0, 250)) / 1000)

        with elapsed.clock(Example, 'two:sub'):
            for x in xrange(3):
                time.sleep(float(random.randint(0, 250)) / 1000)

    @elapsed.clock
    def three(self):
        time.sleep(float(random.randint(0, 250)) / 1000)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    elapsed.setup(enabled=True)

    app = Example()
    app.run()

    elapsed.print_report()

    print 'Done'
