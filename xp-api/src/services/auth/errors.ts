export class UserAlreadyExistsException extends Error {
  constructor() {
    super("USER_ALREADY_EXISTS");
  }
}
