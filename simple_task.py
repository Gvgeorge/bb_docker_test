import time
from buildbot.process import buildstep
from buildbot.process import Remote


class MyStep(buildstep.Remote, buildstep.BuildStep):
    import time
    from twisted.internet import defer

    @defer.inlineCallbacks
    def run(self):

        import time
        counter = 0
        while True:
            print('counting: ', counter)
            time.sleep(2)
            counter += 1
            yield counter
            if counter > 20:
                break
        return  0