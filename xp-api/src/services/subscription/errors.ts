export class TrialAlreadyTakenException extends Error {
  constructor() {
    super("TRIAL_ALREADY_TAKEN");
  }
}
