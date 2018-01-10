import { IScheduledTaskArgs } from './ischeduledTaskArgs';

export class ScheduledTaskGoal implements IScheduledTaskArgs {
    goalWorkflows: string[];
	//One of these is required
	weeks: number;
	days: number;
	hours: number;
	minutes: number;
	seconds: number;
	//Start date is required, end date optional
	start_date: Date;
	end_date: Date;
	//Timezone will most likely never be used
	timezone: string;
}
