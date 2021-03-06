import { Argument } from '../playbook/argument';

export class WorkflowResult {
	/**
	 * UUID of the given action execution, unique for all individual executions of this action.
	 */
	uid: string;
	/**
	 * UUID of the given action that is executing as stored in the workflow.
	 */
	action_uid: string;
	/**
	 * Name of the action to be executed as it is stored in the workflow.
	 */
	action_name: string;
	timestamp: string;
	/**
	 * Status of result. e.g. "Success" or "InvalidArguments"
	 */
	status: string;
	/**
	 * List of arguments used as inputs.
	 */
	arguments: Argument[];
	/**
	 * Result returned by the action executed.
	 */
	result: any;
}
