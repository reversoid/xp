export class NoActiveExperimentException extends Error {
  constructor() {
    super("NO_ACTIVE_EXPERIMENT");
  }
}

export class AlreadyStartedExperimentException extends Error {
  constructor() {
    super("EXPERIMENT_ALREADY_STARTED");
  }
}
