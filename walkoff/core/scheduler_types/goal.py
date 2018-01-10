from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.util import datetime_repr, timedelta_seconds

class GoalTrigger(IntervalTrigger):
    def __init__(self, goalWorkflows=[], weeks=0, days=0, hours=0, minutes=0, seconds=0, start_date=None, end_date=None, timezone=None, jitter=None):
        super(GoalTrigger, self).__init__(weeks, days, hours, minutes, seconds, start_date, end_date, timezone, jitter)
        self.goalWorkflows = goalWorkflows

    def _goal_completed(self):
        from walkoff.controller import controller
        playbook_workflows = controller.playbook_store.get_workflows_by_uid(self.goalWorkflows)
        for playbook, workflows in playbook_workflows.items():
            for workflow in workflows:
                controller.execute_workflow(playbook, workflow)
        return False

    def get_next_fire_time(self, previous_fire_time, now):
        if not self._goal_completed():
            return super(GoalTrigger, self).get_next_fire_time(previous_fire_time, now)
        else:
            return None


    def __getstate__(self):
        output = super(GoalTrigger, self).__getstate__()
        output["goalWorkflows"] = self.goalWorkflows
        return output

    def __setstate__(self, state):
        super(GoalTrigger, self).__setstate__(state)
        self.goalWorkflows = state["goalWorkflows"]

    def __str__(self):
        result = "workflows: " + str(self.goalWorkflows)
        result += super(GoalTrigger, self).__str__()
        return result

    def __repr__(self):
        options = ['workflows=%s' % self.goalWorkflows, 'interval=%r' % self.interval, 'start_date=%r' % datetime_repr(self.start_date)]
        if self.end_date:
            options.append("end_date=%r" % datetime_repr(self.end_date))
        if self.jitter:
            options.append('jitter=%s' % self.jitter)

        return "<%s (%s, timezone='%s')>" % (
            self.__class__.__name__, ', '.join(options), self.timezone)
